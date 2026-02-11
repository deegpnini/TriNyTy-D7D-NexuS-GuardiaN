#!/bin/bash
# Pin Repositories Script
# 
# This script uses the GitHub CLI and GraphQL API to pin repositories to the
# authenticated user's GitHub profile.
#
# Usage: ./scripts/pin-repos.sh "owner/repo1,owner/repo2,owner/repo3"
#
# Requirements:
# - GitHub CLI (gh) must be installed
# - NEXUS_PAT environment variable must be set with a valid GitHub PAT
# - PAT must have 'user' scope to manage pinned repositories
# - DRY_RUN environment variable controls whether to actually pin (false) or just validate (true)
#
# TODO: Add support for unpinning repositories
# TODO: Add support for reordering pinned repositories
# TODO: Add validation to check if repository exists before attempting to pin
# TODO: Add support for batch operations with better error recovery

set -o pipefail

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Configuration
LOG_FILE="docs/pin-repos-log.txt"
TIMESTAMP=$(date -u +"%Y-%m-%d %H:%M:%S UTC")

# Initialize log file
echo "==================================================" > "$LOG_FILE"
echo "Pin Repositories Script - Execution Log" >> "$LOG_FILE"
echo "Timestamp: $TIMESTAMP" >> "$LOG_FILE"
echo "==================================================" >> "$LOG_FILE"
echo "" >> "$LOG_FILE"

# Function to log messages
log() {
    local level="$1"
    shift
    local message="$*"
    echo -e "${level}: ${message}" | tee -a "$LOG_FILE"
}

# Function to log info messages
log_info() {
    log "${BLUE}INFO${NC}" "$@"
}

# Function to log success messages
log_success() {
    log "${GREEN}SUCCESS${NC}" "$@"
}

# Function to log warning messages
log_warning() {
    log "${YELLOW}WARNING${NC}" "$@"
}

# Function to log error messages
log_error() {
    log "${RED}ERROR${NC}" "$@"
}

# Check if repos argument is provided
if [ -z "$1" ]; then
    log_error "No repositories provided. Usage: $0 'owner/repo1,owner/repo2'"
    exit 1
fi

REPOS_INPUT="$1"
log_info "Repositories to pin: $REPOS_INPUT"
echo "Repositories: $REPOS_INPUT" >> "$LOG_FILE"

# Check if running in dry run mode
if [ "${DRY_RUN:-true}" = "true" ]; then
    log_info "🏃 Running in DRY RUN mode - no actual pinning will occur"
    echo "Mode: DRY RUN" >> "$LOG_FILE"
else
    log_info "🚀 Running in LIVE mode - repositories will be pinned"
    echo "Mode: LIVE" >> "$LOG_FILE"
    
    # Check if NEXUS_PAT is set for live mode
    if [ -z "$NEXUS_PAT" ]; then
        log_error "NEXUS_PAT environment variable is not set"
        log_error "This is required for pinning repositories"
        echo "Error: NEXUS_PAT not set" >> "$LOG_FILE"
        exit 1
    fi
    
    # Authenticate gh CLI with the PAT
    echo "$NEXUS_PAT" | gh auth login --with-token 2>/dev/null
    if [ $? -ne 0 ]; then
        log_error "Failed to authenticate with GitHub CLI using NEXUS_PAT"
        echo "Error: Authentication failed" >> "$LOG_FILE"
        exit 1
    fi
    log_success "Authenticated with GitHub CLI"
fi

echo "" >> "$LOG_FILE"

# Convert comma-separated list to array
IFS=',' read -ra REPOS_ARRAY <<< "$REPOS_INPUT"

# Track success/failure counts
SUCCESS_COUNT=0
FAILURE_COUNT=0

log_info "Processing ${#REPOS_ARRAY[@]} repositories..."
echo "Processing ${#REPOS_ARRAY[@]} repositories:" >> "$LOG_FILE"

# Process each repository
for repo in "${REPOS_ARRAY[@]}"; do
    # Trim whitespace
    repo=$(echo "$repo" | xargs)
    
    log_info "Processing: $repo"
    
    # Validate format (should be owner/repo)
    if [[ ! "$repo" =~ ^[^/]+/[^/]+$ ]]; then
        log_warning "Invalid repository format: $repo (expected: owner/repo)"
        echo "  ⚠️  $repo - SKIPPED (invalid format)" >> "$LOG_FILE"
        FAILURE_COUNT=$((FAILURE_COUNT + 1))
        continue
    fi
    
    # Extract owner and repo name
    OWNER=$(echo "$repo" | cut -d'/' -f1)
    REPO_NAME=$(echo "$repo" | cut -d'/' -f2)
    
    if [ "${DRY_RUN:-true}" = "true" ]; then
        log_info "  [DRY RUN] Would pin: $OWNER/$REPO_NAME"
        echo "  ✓ $repo - DRY RUN (validated)" >> "$LOG_FILE"
        SUCCESS_COUNT=$((SUCCESS_COUNT + 1))
    else
        # TODO: First check if repository exists using gh api
        # TODO: Get repository node ID using GraphQL query
        
        log_info "  Attempting to pin: $OWNER/$REPO_NAME"
        
        # Get repository ID first
        REPO_ID=$(gh api graphql -f query='
          query($owner: String!, $name: String!) {
            repository(owner: $owner, name: $name) {
              id
            }
          }
        ' -f owner="$OWNER" -f name="$REPO_NAME" --jq '.data.repository.id' 2>/dev/null)
        
        if [ -z "$REPO_ID" ]; then
            log_error "  Failed to get repository ID for $repo (repository may not exist)"
            echo "  ❌ $repo - FAILED (repository not found)" >> "$LOG_FILE"
            FAILURE_COUNT=$((FAILURE_COUNT + 1))
            continue
        fi
        
        log_info "  Repository ID: $REPO_ID"
        
        # GitHub's pinning API requires updating the entire list of pinned repositories (max 6).
        # First, get currently pinned repositories
        CURRENT_PINNED=$(gh api graphql -f query='
          query {
            viewer {
              pinnedItems(first: 6, types: REPOSITORY) {
                nodes {
                  ... on Repository {
                    id
                  }
                }
              }
            }
          }
        ' --jq '.data.viewer.pinnedItems.nodes[].id' 2>/dev/null | tr '\n' ',' | sed 's/,$//')
        
        # Build the new list of repository IDs (current + new one)
        if [ -z "$CURRENT_PINNED" ]; then
            NEW_PINNED_LIST="\"$REPO_ID\""
        else
            # Check if already pinned
            if echo "$CURRENT_PINNED" | grep -q "$REPO_ID"; then
                log_warning "  ⚠️  Repository is already pinned: $OWNER/$REPO_NAME"
                echo "  ⚠️  $repo - SKIPPED (already pinned)" >> "$LOG_FILE"
                SUCCESS_COUNT=$((SUCCESS_COUNT + 1))
                continue
            fi
            
            # Convert comma-separated IDs to JSON array format
            IFS=',' read -ra PINNED_ARRAY <<< "$CURRENT_PINNED"
            NEW_PINNED_LIST=$(printf '\"%s\",' "${PINNED_ARRAY[@]}")
            NEW_PINNED_LIST="${NEW_PINNED_LIST}\"$REPO_ID\""
            
            # Check if we're at the limit (6 repositories)
            PINNED_COUNT=$(echo "$CURRENT_PINNED" | tr ',' '\n' | wc -l)
            if [ "$PINNED_COUNT" -ge 6 ]; then
                log_error "  ❌ Cannot pin: Already at maximum (6 pinned repositories)"
                echo "  ❌ $repo - FAILED (maximum pinned repositories reached)" >> "$LOG_FILE"
                FAILURE_COUNT=$((FAILURE_COUNT + 1))
                continue
            fi
        fi
        
        log_info "  Pinning repository (updating pinned items list)..."
        
        # Pin the repository using GraphQL mutation
        RESULT=$(gh api graphql -f query="
          mutation {
            updatePinnedRepositories(input: {
              repositoryIds: [$NEW_PINNED_LIST]
            }) {
              clientMutationId
            }
          }
        " 2>&1)
        
        if [ $? -eq 0 ]; then
            log_success "  ✅ Successfully pinned: $OWNER/$REPO_NAME"
            echo "  ✅ $repo - SUCCESS" >> "$LOG_FILE"
            SUCCESS_COUNT=$((SUCCESS_COUNT + 1))
        else
            log_error "  ❌ Failed to pin: $OWNER/$REPO_NAME"
            log_error "  Error: $RESULT"
            echo "  ❌ $repo - FAILED (pinning error)" >> "$LOG_FILE"
            echo "     Error: $RESULT" >> "$LOG_FILE"
            FAILURE_COUNT=$((FAILURE_COUNT + 1))
        fi
    fi
    
    # Small delay between requests to avoid rate limiting
    sleep 0.5
done

echo "" >> "$LOG_FILE"
echo "==================================================" >> "$LOG_FILE"
echo "Summary:" >> "$LOG_FILE"
echo "  Total: ${#REPOS_ARRAY[@]}" >> "$LOG_FILE"
echo "  Success: $SUCCESS_COUNT" >> "$LOG_FILE"
echo "  Failures: $FAILURE_COUNT" >> "$LOG_FILE"
echo "==================================================" >> "$LOG_FILE"

log_info ""
log_info "=================================================="
log_info "Summary:"
log_info "  Total: ${#REPOS_ARRAY[@]}"
log_success "  Success: $SUCCESS_COUNT"
if [ $FAILURE_COUNT -gt 0 ]; then
    log_error "  Failures: $FAILURE_COUNT"
else
    log_info "  Failures: $FAILURE_COUNT"
fi
log_info "=================================================="
log_info "Log saved to: $LOG_FILE"

# Exit with error if any failures occurred
if [ $FAILURE_COUNT -gt 0 ]; then
    exit 1
fi

exit 0
