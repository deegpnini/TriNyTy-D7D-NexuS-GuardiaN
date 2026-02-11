# Pin Repositories Workflow Documentation

## Overview

This workflow allows you to pin GitHub repositories to your profile using GitHub Actions. It provides a safe, automated way to manage your pinned repositories.

## ⚠️ Important Prerequisites

**This workflow will NOT run until you complete the setup steps below.**

The workflow requires a Personal Access Token (PAT) to be configured as a repository secret. Without this token, the workflow will fail immediately.

## Setup Instructions

### Step 1: Create a Personal Access Token (PAT)

1. Go to GitHub Settings: [https://github.com/settings/tokens](https://github.com/settings/tokens)
2. Click **"Generate new token"** → **"Generate new token (classic)"**
3. Give your token a descriptive name, e.g., "Nexus Pin Repos Workflow"
4. Set an appropriate expiration date (recommended: 90 days)
5. Select the following scopes:
   - ✅ `repo` (Full control of private repositories)
   - ✅ `user` (Update user data)
6. Click **"Generate token"** at the bottom of the page
7. **IMPORTANT**: Copy the token immediately - you won't be able to see it again!

### Step 2: Add Token to Repository Secrets

1. Go to your repository settings:
   ```
   https://github.com/deegpnini/TriNyTy-D7D-NexuS-GuardiaN/settings/secrets/actions
   ```
2. Click **"New repository secret"**
3. Set the name to: `NEXUS_PAT`
4. Paste the token value you copied in Step 1
5. Click **"Add secret"**

### Step 3: Verify Setup

After adding the secret, the workflow will be able to run. You can verify the setup by running the workflow in dry-run mode (see below).

## How to Use the Workflow

### Running the Workflow

1. Go to the **Actions** tab in your repository:
   ```
   https://github.com/deegpnini/TriNyTy-D7D-NexuS-GuardiaN/actions
   ```

2. Select the **"Pin Repositories"** workflow from the left sidebar

3. Click the **"Run workflow"** button (on the right side)

4. Fill in the workflow inputs:

### Workflow Inputs

#### `repos` (Required)
- **Description**: Comma-separated list of repositories to pin
- **Format**: `owner/repo` format
- **Example**: `deegpnini/TriNyTy-D7D-NexuS-GuardiaN,deegpnini/D7D,deegpnini/trinity-xai-exoplanets`

#### `dry_run` (Optional)
- **Description**: Run in dry-run mode (safe testing)
- **Default**: `true`
- **Options**: 
  - `true`: Shows what would happen without making changes
  - `false`: Actually pins the repositories (requires NEXUS_PAT secret)

### Example Usage

#### Example 1: Dry Run (Safe Testing)

**Inputs:**
```
repos: deegpnini/TriNyTy-D7D-NexuS-GuardiaN,deegpnini/D7D
dry_run: true
```

This will show you what the workflow would do without actually pinning any repositories.

#### Example 2: Actually Pin Repositories

**Inputs:**
```
repos: deegpnini/TriNyTy-D7D-NexuS-GuardiaN,deegpnini/D7D,deegpnini/trinity-xai-exoplanets
dry_run: false
```

This will actually pin the specified repositories to your profile (requires NEXUS_PAT secret).

## How the Workflow Works

1. **Checkout**: Checks out the repository code
2. **Install GitHub CLI**: Verifies gh CLI is available
3. **Check Secret**: Verifies that NEXUS_PAT secret exists
4. **Dry Run Mode**: If enabled, prints what would happen and exits
5. **Verify Secret**: If dry_run is false, ensures secret exists before proceeding
6. **Execute Script**: Runs `scripts/pin-repos.sh` with your repository list
7. **Upload Logs**: Uploads execution logs as an artifact

## Script Details

The `scripts/pin-repos.sh` script:
- Authenticates with GitHub using the NEXUS_PAT token
- Validates each repository in the list
- Checks if repositories exist and are accessible
- Logs all actions to `docs/pin-repos-log.txt`
- **Note**: Current implementation is preparatory and includes TODOs for full pinning logic

## Logs and Debugging

After a workflow run:
1. Go to the workflow run details
2. Download the **"pin-repos-logs"** artifact
3. Extract and view `pin-repos-log.txt` for detailed execution information

## Security Considerations

- ✅ The NEXUS_PAT token is stored securely in GitHub Secrets
- ✅ The token is never exposed in logs or outputs
- ✅ Dry-run mode allows safe testing without making changes
- ⚠️ Only grant the minimum required scopes to the token
- ⚠️ Rotate tokens regularly (every 90 days recommended)
- ⚠️ Revoke tokens immediately if compromised

## Troubleshooting

### "NEXUS_PAT secret is not configured"
- **Solution**: Follow Step 2 in Setup Instructions to add the secret

### "Authentication failed"
- **Cause**: Token is invalid, expired, or doesn't have required scopes
- **Solution**: Generate a new token with correct scopes and update the secret

### "Repository not found or not accessible"
- **Cause**: Repository doesn't exist or token doesn't have access
- **Solution**: Verify repository name format (owner/repo) and token permissions

## Current Limitations

This is a **preparatory implementation** with the following known limitations:

- 🔧 **TODO**: Full GraphQL pinning mutation not yet implemented
- 🔧 **TODO**: Repository validation is basic
- 🔧 **TODO**: No retry logic for API failures
- 🔧 **TODO**: No support for unpinning repositories
- 🔧 **TODO**: No rate limiting handling

These will be addressed in future iterations.

## Support

For issues or questions:
- Review the workflow logs in the Actions tab
- Check `docs/pin-repos-log.txt` in the logs artifact
- Create an issue in the repository
- Contact @deegpnini

---

**Last Updated**: 2026-02-11  
**Version**: 1.0.0 (Preparatory)
