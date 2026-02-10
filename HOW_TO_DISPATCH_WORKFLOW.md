# How to Dispatch the Nexus Fusion Workflow

This document provides instructions for running the Nexus Fusion workflow immediately.

## Prerequisites

The workflow is now available in the repository. To dispatch it, you need:
1. Write access to the repository
2. The workflow must be on a branch that has been pushed to GitHub

## Method 1: GitHub Web Interface (Recommended)

1. Go to https://github.com/deegpnini/TriNyTy-D7D-NexuS-GuardiaN
2. Click the **"Actions"** tab at the top
3. In the left sidebar, find and click **"Nexus Fusion - Merge 12 Source Repositories"**
4. Click the **"Run workflow"** button (on the right side)
5. A dialog will appear:
   - **Branch**: Select `copilot/add-nexus-fusion-workflow` (or `main` if merged)
   - **Confirm**: Type exactly `FUSE` (all caps)
6. Click the green **"Run workflow"** button

The workflow will start running immediately. You can monitor its progress in the Actions tab.

## Method 2: GitHub CLI

If you have the GitHub CLI (`gh`) installed:

```bash
# For the current PR branch
gh workflow run nexus-fusion.yml \
  --ref copilot/add-nexus-fusion-workflow \
  --field confirm=FUSE

# After merging to main
gh workflow run nexus-fusion.yml \
  --ref main \
  --field confirm=FUSE
```

## Method 3: REST API

Using curl:

```bash
# Set your GitHub token
export GITHUB_TOKEN="your_personal_access_token_here"

# Dispatch the workflow
curl -X POST \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer $GITHUB_TOKEN" \
  -H "X-GitHub-Api-Version: 2022-11-28" \
  https://api.github.com/repos/deegpnini/TriNyTy-D7D-NexuS-GuardiaN/actions/workflows/nexus-fusion.yml/dispatches \
  -d '{"ref":"copilot/add-nexus-fusion-workflow","inputs":{"confirm":"FUSE"}}'
```

## What Happens When You Run It

The workflow will:
1. ✅ Create a `modules/` directory
2. ✅ Add all 12 source repositories as git subtrees under `modules/`
3. ✅ Preserve 100% of git history from each repository
4. ✅ Create documentation in `modules/README.md`
5. ✅ Push all changes to the branch

This process may take 10-30 minutes depending on the size of the repositories.

## After the Workflow Completes

1. Review the changes in the branch
2. If on a PR branch, merge the PR to `main`
3. The `modules/` directory will contain all 12 repositories with full history

## Troubleshooting

**Workflow doesn't appear in Actions tab**
- Make sure the workflow file is committed and pushed to the branch
- Refresh the page

**"Run workflow" button is disabled**
- You may not have write access to the repository
- Check if you're viewing the correct branch

**Workflow fails to run**
- Verify you typed `FUSE` exactly (case-sensitive)
- Check the Actions tab for error messages

## Note About Repository Access

The workflow accesses 12 public repositories. If any repository becomes private or is deleted, that specific subtree addition will fail, but the workflow will continue with the remaining repositories.

## Alternative: Manual Execution

If you prefer to run the fusion manually instead of using the workflow:

```bash
# Clone the repository
git clone https://github.com/deegpnini/TriNyTy-D7D-NexuS-GuardiaN.git
cd TriNyTy-D7D-NexuS-GuardiaN

# Run the helper script
./scripts/nexus-fusion.sh

# Push the changes
git push origin <branch-name>
```

For more details, see `.github/workflows/NEXUS_FUSION_README.md`.
