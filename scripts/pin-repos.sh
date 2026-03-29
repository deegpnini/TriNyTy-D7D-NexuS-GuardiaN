#!/bin/bash
# Pin Repositories Script
# 
# This script pins specified GitHub repositories to the authenticated user's profile.
# It uses the GitHub GraphQL API via the GitHub CLI (gh) tool.
#
# Usage: ./scripts/pin-repos.sh "owner1/repo1,owner2/repo2,owner3/repo3"
#
# Requirements:
#   - GitHub CLI (gh) must be installed
#   - NEXUS_PAT environment variable must be set with a valid GitHub Personal Access Token
#   - The token must have 'repo' and 'user' scopes
#
# Safety Notes:
#   - This script will modify your GitHub profile by pinning repositories
#   - Always test with dry_run=true in the workflow first
#   - Review the repositories list carefully before execution
#
# TODOs:
#   - Add retry logic for transient API failures
#   - Add validation for repository existence before pinning
#   - Add support for unpinning repositories
#   - Add better error handling for rate limiting

set -e  # Exit on error
set -u  # Exit on undefined variable
set -o pipefail  # Exit on pipe failure

# Configuration
LOG_FILE="docs/pin-repos-log.txt"
SCRIPT_NAME="$(basename "$0")"

# Initialize log file
mkdir -p "$(dirname "$LOG_FILE")"
echo "==================================================" >> "$LOG_FILE"
echo "Pin Repositories Script Execution" >> "$LOG_FILE"
echo "Start Time: $(date -u '+%Y-%m-%d %H:%M:%S UTC')" >> "$LOG_FILE"
echo "==================================================" >> "$LOG_FILE"
echo "" >> "$LOG_FILE"

# Function to log messages
log() {
    local message="$1"
    echo "[$(date -u '+%Y-%m-%d %H:%M:%S')] $message" | tee -a "$LOG_FILE"
}

# Function to log errors
log_error() {
    local message="$1"
    echo "[$(date -u '+%Y-%m-%d %H:%M:%S')] ERROR: $message" | tee -a "$LOG_FILE" >&2
}

# Check if repos argument is provided
if [ $# -eq 0 ]; then
    log_error "No repositories provided"
    log_error "Usage: $SCRIPT_NAME \"owner1/repo1,owner2/repo2\""
    exit 1
fi

REPOS_INPUT="$1"
log "📋 Input repositories: $REPOS_INPUT"

# Check if NEXUS_PAT is set
if [ -z "${NEXUS_PAT:-}" ]; then
    log_error "NEXUS_PAT environment variable is not set"
    log_error "Please set NEXUS_PAT with a valid GitHub Personal Access Token"
    exit 1
fi

# Authenticate with GitHub CLI using the token
log "🔐 Authenticating with GitHub CLI..."
if echo "$NEXUS_PAT" | gh auth login --with-token 2>&1 | tee -a "$LOG_FILE"; then
    log "✅ Authentication successful"
else
    log_error "Authentication failed"
    exit 1
fi

# Verify authentication status
log "🔍 Verifying authentication status..."
if gh auth status 2>&1 | tee -a "$LOG_FILE"; then
    log "✅ Authentication verified"
else
    log_error "Authentication verification failed"
    exit 1
fi

# Get authenticated user info
log "👤 Getting authenticated user information..."
USER_LOGIN=$(gh api user --jq '.login' 2>&1 | tee -a "$LOG_FILE")
if [ -z "$USER_LOGIN" ]; then
    log_error "Failed to get authenticated user login"
    exit 1
fi
log "✅ Authenticated as: $USER_LOGIN"

# Split comma-separated repos into array
IFS=',' read -ra REPOS_ARRAY <<< "$REPOS_INPUT"
log "📦 Number of repositories to pin: ${#REPOS_ARRAY[@]}"

# TODO: Implement actual pinning logic
# NOTE: The GraphQL mutation for pinning repositories is complex and requires:
#   1. Getting the repository ID for each repo
#   2. Getting the user's current pinned items
#   3. Calling the updatePinnableItems mutation
#
# For now, this script will simulate the process and log what would happen.

SUCCESSFUL_PINS=0
FAILED_PINS=0

for repo in "${REPOS_ARRAY[@]}"; do
    # Trim whitespace
    repo=$(echo "$repo" | xargs)
    
    if [ -z "$repo" ]; then
        log "⚠️  Skipping empty repository entry"
        continue
    fi
    
    log ""
    log "📌 Processing repository: $repo"
    
    # Validate repo format (should be owner/repo)
    if [[ ! "$repo" =~ ^[a-zA-Z0-9_-]+/[a-zA-Z0-9_.-]+$ ]]; then
        log_error "Invalid repository format: $repo (expected: owner/repo)"
        FAILED_PINS=$((FAILED_PINS + 1))
        continue
    fi
    
    # Extract owner and repo name
    OWNER=$(echo "$repo" | cut -d'/' -f1)
    REPO_NAME=$(echo "$repo" | cut -d'/' -f2)
    
    log "  Owner: $OWNER"
    log "  Repository: $REPO_NAME"
    
    # TODO: Check if repository exists and is accessible
    log "  ℹ️  Checking if repository exists..."
    if gh api "repos/$OWNER/$REPO_NAME" --jq '.id' >> "$LOG_FILE" 2>&1; then
        REPO_ID=$(gh api "repos/$OWNER/$REPO_NAME" --jq '.id')
        log "  ✅ Repository exists (ID: $REPO_ID)"
        
        # TODO: Actually pin the repository using GraphQL mutation
        # For now, we'll just log that we would pin it
        log "  🔧 TODO: Implement GraphQL mutation to pin repository"
        log "  📝 Would execute: updatePinnableItems mutation for repository ID $REPO_ID"
        
        # Placeholder for actual pinning logic
        log "  ⚠️  Pinning logic not yet implemented - this is a preparatory script"
        log "  ℹ️  Repository validated but not pinned"
        
        SUCCESSFUL_PINS=$((SUCCESSFUL_PINS + 1))
    else
        log_error "  ❌ Repository not found or not accessible: $repo"
        FAILED_PINS=$((FAILED_PINS + 1))
    fi
done

# Summary
log ""
log "==================================================" 
log "📊 Execution Summary"
log "==================================================" 
log "Total repositories processed: ${#REPOS_ARRAY[@]}"
log "Successful validations: $SUCCESSFUL_PINS"
log "Failed: $FAILED_PINS"
log "End Time: $(date -u '+%Y-%m-%d %H:%M:%S UTC')"
log "==================================================" 
log ""

# Exit with appropriate code
if [ $FAILED_PINS -gt 0 ]; then
    log_error "Script completed with errors"
    exit 1
else
    log "✅ Script completed successfully"
    exit 0
fi
