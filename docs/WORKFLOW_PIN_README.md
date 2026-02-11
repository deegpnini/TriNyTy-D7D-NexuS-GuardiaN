# Pin Repositories Workflow - README

## Overview

This document explains how to use the **Pin Repositories Workflow** to pin GitHub repositories to your profile. This workflow is a preparatory setup and **will not run until you add the required Personal Access Token (PAT) as a repository secret**.

## ⚠️ Important Notice

**No tokens were provided; the workflow will not run until you add NEXUS_PAT as a repository secret named NEXUS_PAT.**

This workflow requires a GitHub Personal Access Token (PAT) with the `user` scope to manage pinned repositories on your profile. Until this token is added as a repository secret, the workflow will fail early with a clear error message and will not attempt any pinning operations.

## Prerequisites

Before using this workflow, you must:

1. **Generate a Personal Access Token (PAT)**
   - Go to [GitHub Settings > Developer settings > Personal access tokens](https://github.com/settings/tokens)
   - Click "Generate new token" (classic)
   - Give it a descriptive name (e.g., "Nexus Pin Repos Workflow")
   - Select the **`user`** scope (required for managing profile pinned repositories)
   - Set an appropriate expiration date
   - Click "Generate token"
   - **Copy the token immediately** (you won't be able to see it again)

2. **Add the PAT as a Repository Secret**
   - Go to this repository's **Settings** > **Secrets and variables** > **Actions**
   - Click **"New repository secret"**
   - **Name:** `NEXUS_PAT` (must be exactly this name)
   - **Value:** Paste your Personal Access Token
   - Click **"Add secret"**

## How to Run the Workflow

Once you've added the `NEXUS_PAT` secret, you can run the workflow manually:

### Step 1: Navigate to Actions Tab
- Go to the **Actions** tab in this repository
- Find the workflow named **"Pin Repositories Workflow"** in the left sidebar

### Step 2: Run Workflow
- Click the **"Run workflow"** dropdown button
- You'll see two input fields:

#### Input: `repos`
**Required:** A comma-separated list of repositories to pin

**Format:** `owner/repo1,owner/repo2,owner/repo3`

**Example:**
```
deegpnini/TriNyTy-D7D-NexuS-GuardiaN,deegpnini/trinity-xai-exoplanets,deegpnini/D7D
```

#### Input: `dry_run`
**Optional:** Whether to run in dry run mode (default: `true`)

- **`true`** (default): Validates input and checks configuration without actually pinning repositories
- **`false`**: Actually pins the repositories to your profile

### Step 3: Review Results
- The workflow will display progress in the Actions tab
- A summary will be created showing:
  - Dry run mode status
  - Repositories processed
  - Success/failure counts
- A log file (`pin-repos-log.txt`) will be uploaded as an artifact for detailed review

## Sample Inputs

### Example 1: Dry Run (Safe Test)
```
repos: deegpnini/TriNyTy-D7D-NexuS-GuardiaN,deegpnini/trinity-xai-exoplanets
dry_run: true
```
This will validate the input and configuration without making any changes.

### Example 2: Live Run (Actually Pin)
```
repos: deegpnini/TriNyTy-D7D-NexuS-GuardiaN,deegpnini/trinity-xai-exoplanets,deegpnini/D7D
dry_run: false
```
This will actually pin the specified repositories to your GitHub profile.

⚠️ **Important:** Make sure the `NEXUS_PAT` secret is configured before running with `dry_run: false`!

## Understanding the Workflow

### What It Does
1. **Validates Secret:** Checks if `NEXUS_PAT` secret exists (only when `dry_run: false`)
2. **Checks Out Repository:** Clones the repository to the runner
3. **Installs GitHub CLI:** Uses the pre-installed `gh` CLI on ubuntu-latest runners
4. **Runs Script:** Executes `scripts/pin-repos.sh` with your repository list
5. **Uploads Log:** Saves execution log as an artifact
6. **Creates Summary:** Displays results in the workflow summary

### Safety Features
- **Early Failure:** If `NEXUS_PAT` is not configured and `dry_run: false`, the workflow fails immediately with a clear error message
- **Dry Run Default:** The workflow defaults to `dry_run: true` to prevent accidental changes
- **Input Validation:** The script validates repository format before attempting to pin
- **Error Handling:** Graceful error handling with detailed logging
- **Rate Limiting:** Small delays between API calls to avoid rate limits

## Script Details

The `scripts/pin-repos.sh` script:
- Accepts a comma-separated list of repositories in `owner/repo` format
- Validates input format
- Uses GitHub CLI (`gh`) with the PAT to authenticate
- Calls GitHub GraphQL API to pin repositories
- Handles errors gracefully
- Writes a detailed log to `docs/pin-repos-log.txt`

### Current TODOs in the Script
The script includes several TODOs for future enhancements:
- Add support for unpinning repositories
- Add support for reordering pinned repositories
- Add validation to check if repository exists before attempting to pin
- Add support for batch operations with better error recovery

## Troubleshooting

### Workflow Fails with "NEXUS_PAT secret is not configured"
**Solution:** Follow the "Add the PAT as a Repository Secret" instructions above.

### Script Fails with "Invalid repository format"
**Solution:** Ensure repositories are in the format `owner/repo` (e.g., `deegpnini/D7D`), separated by commas with no spaces.

### Script Fails with "Repository not found"
**Solution:** Verify that:
- The repository name is spelled correctly
- The repository exists and is accessible
- Your PAT has the correct permissions

### Rate Limiting Errors
**Solution:** The script includes delays between requests, but if you're pinning many repositories, you may need to:
- Reduce the batch size
- Wait a few minutes between runs

## Security Considerations

- **Never commit your PAT to the repository**
- **Use repository secrets** to store sensitive tokens
- The workflow only runs when manually triggered (`workflow_dispatch`)
- The PAT is only used when `dry_run: false`
- The PAT is not exposed in logs or outputs

## Additional Resources

- [GitHub GraphQL API - Repository Pinning](https://docs.github.com/en/graphql/reference/mutations#updatepinnedrepositories)
- [GitHub CLI Documentation](https://cli.github.com/manual/)
- [Creating a Personal Access Token](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token)

## Support

If you encounter issues or have questions about this workflow, please:
1. Check the workflow run logs in the Actions tab
2. Review the uploaded `pin-repos-log.txt` artifact
3. Open an issue in this repository with details about the problem
