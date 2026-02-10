# Nexus Fusion Workflow

This document explains how to use the Nexus Fusion workflow to merge 12 source repositories into the TriNyTy D7D NexuS GuardiaN repository.

## Overview

The Nexus Fusion workflow (`nexus-fusion.yml`) performs a complete integration of 12 source repositories into this repository, preserving 100% of their git history using git subtree merge strategy.

## Source Repositories

The following 12 repositories will be fused:

1. **trinity-xai-exoplanets** - Collaborative AI models for exoplanet research
2. **Arcturus-8-9** - Scientific reliability assessment system (8.9/10 skeptic rating)
3. **trinity-quantum-memory-system** - Quantum memory persistence system based on neuroscience
4. **frete-facil-plus** - Freight management system
5. **trinity-framework.** - Consciousness correlation engine for comet tracking
6. **try-g-nexus** - Web application interface
7. **Trinity-Falcon-Lung** - Open-source Falcon 9 optimization
8. **D7D** - Core D7D system
9. **trinity-resilience-protocol** - Adaptive resilience protocol for deep-space communications
10. **D7D-CODEX** - Sistema Orquestral D7D - Amor Ágape 100%
11. **PROJETO_INTERESTELAR_HEBRON** - Integrated system developed in Termux Android
12. **TorreHebron** - Brazilian computational astronomy framework

## How to Run the Workflow

### Via GitHub Actions UI

1. Go to the repository on GitHub
2. Click on the **Actions** tab
3. Select **"Nexus Fusion - Merge 12 Source Repositories"** from the workflows list
4. Click **"Run workflow"**
5. In the branch dropdown, select the branch you want to run on (e.g., `main`)
6. In the input field for "confirm", type exactly: **FUSE**
7. Click the green **"Run workflow"** button

### Via GitHub CLI

```bash
gh workflow run nexus-fusion.yml \
  --ref main \
  --field confirm=FUSE
```

Replace `main` with your target branch if needed.

### Via API

```bash
curl -X POST \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer YOUR_GITHUB_TOKEN" \
  -H "X-GitHub-Api-Version: 2022-11-28" \
  https://api.github.com/repos/deegpnini/TriNyTy-D7D-NexuS-GuardiaN/actions/workflows/nexus-fusion.yml/dispatches \
  -d '{"ref":"main","inputs":{"confirm":"FUSE"}}'
```

Replace `YOUR_GITHUB_TOKEN` with your personal access token and `main` with your target branch if needed.

## Manual Execution (Alternative)

If you prefer to run the fusion manually using the helper script:

```bash
cd /path/to/TriNyTy-D7D-NexuS-GuardiaN
./scripts/nexus-fusion.sh
```

## What Happens During Fusion

1. **Checkout** - The workflow checks out this repository
2. **Git Configuration** - Sets up git user for commits
3. **Create Modules Directory** - Creates `modules/` directory with a README
4. **Repository Fusion** - For each of the 12 repositories:
   - Adds the repository as a git subtree under `modules/{repo-name}/`
   - Preserves complete git history (no squashing)
   - Creates a merge commit
5. **Update Documentation** - Updates the modules README with fusion details
6. **Push Changes** - Pushes all changes to the branch

## Result Structure

After fusion, the repository structure will be:

```
TriNyTy-D7D-NexuS-GuardiaN/
├── .github/
│   └── workflows/
│       └── nexus-fusion.yml
├── modules/
│   ├── README.md
│   ├── trinity-xai-exoplanets/
│   ├── Arcturus-8-9/
│   ├── trinity-quantum-memory-system/
│   ├── frete-facil-plus/
│   ├── trinity-framework./
│   ├── try-g-nexus/
│   ├── Trinity-Falcon-Lung/
│   ├── D7D/
│   ├── trinity-resilience-protocol/
│   ├── D7D-CODEX/
│   ├── PROJETO_INTERESTELAR_HEBRON/
│   └── TorreHebron/
├── scripts/
├── src/
└── ...
```

## Git History Preservation

The workflow uses `git subtree add` **without** the `--squash` flag, which means:

- ✅ **100% of commit history** from each repository is preserved
- ✅ All commit messages, authors, and timestamps remain intact
- ✅ The git log will show the complete development history of all projects
- ✅ You can use `git log --follow` to trace file history across repositories

## Safety Measures

- **Confirmation Required**: The workflow requires typing "FUSE" to run, preventing accidental execution
- **Continue on Error**: If a repository fails to fuse, the workflow continues with remaining repositories
- **No Destructive Operations**: The workflow only adds content, never removes existing files

## Troubleshooting

### Workflow doesn't appear in Actions tab
- Make sure the workflow file is committed to the branch you're viewing
- Check that the YAML syntax is valid

### Subtree add fails
- Verify the repository exists and is accessible
- Check that the branch name is correct (default is `main`)
- Ensure there are no conflicts with existing directories

### Permission denied
- Ensure you have write access to the repository
- Check that the GITHUB_TOKEN has sufficient permissions

## Next Steps After Fusion

1. Review the fused repositories in `modules/`
2. Update documentation to reference the new structure
3. Consider adding integration scripts or workflows
4. Set up CI/CD pipelines for the unified codebase

## References

- [Git Subtree Documentation](https://git-scm.com/book/en/v2/Git-Tools-Subtree-Merging)
- [GitHub Actions workflow_dispatch](https://docs.github.com/en/actions/using-workflows/events-that-trigger-workflows#workflow_dispatch)
