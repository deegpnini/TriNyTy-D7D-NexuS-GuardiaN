#!/bin/bash
# Nexus Fusion Helper Script
# This script helps to manually perform the Nexus fusion of 12 source repositories
# Usage: ./scripts/nexus-fusion.sh

set -e

echo "🌀 Nexus Fusion - Merging 12 Source Repositories"
echo "================================================="
echo ""

# Array of repositories to fuse
declare -a REPOS=(
    "trinity-xai-exoplanets"
    "Arcturus-8-9"
    "trinity-quantum-memory-system"
    "frete-facil-plus"
    "trinity-framework."
    "try-g-nexus"
    "Trinity-Falcon-Lung"
    "D7D"
    "-trinity-resilience-protocol"
    "D7D-CODEX"
    "PROJETO_INTERESTELAR_HEBRON"
    "TorreHebron"
)

# Create modules directory
echo "📦 Creating modules directory..."
mkdir -p modules

# Create README
cat > modules/README.md << 'EOF'
# Nexus Modules

This directory contains the fused source repositories as git subtrees.

## Source Repositories:

1. trinity-xai-exoplanets - Collaborative AI models for exoplanet research
2. Arcturus-8-9 - Scientific reliability assessment system
3. trinity-quantum-memory-system - Quantum memory persistence system
4. frete-facil-plus - Freight management system
5. trinity-framework - Consciousness correlation engine
6. try-g-nexus - Web application interface
7. Trinity-Falcon-Lung - Falcon 9 optimization
8. D7D - Core D7D system
9. trinity-resilience-protocol - Adaptive resilience protocol
10. D7D-CODEX - Sistema Orquestral D7D
11. PROJETO_INTERESTELAR_HEBRON - Integrated system developed in Termux
12. TorreHebron - Brazilian computational astronomy framework

## Fusion Information
- Fusion Method: git subtree with full history preservation
- Each repository is added under modules/{repo-name}/
EOF

git add modules/README.md
git commit -m "📦 Create modules directory for Nexus fusion"

echo ""
echo "🔄 Starting repository fusion..."
echo ""

# Counter for progress
count=0
total=${#REPOS[@]}

# Fuse each repository
for repo in "${REPOS[@]}"; do
    count=$((count + 1))
    echo "[$count/$total] Fusing $repo..."
    
    # Add the repository as a subtree
    git subtree add --prefix="modules/$repo" \
        "https://github.com/deegpnini/$repo.git" main \
        --message "🔀 Fuse $repo into Nexus Guardian" || {
        echo "⚠️  Warning: Failed to fuse $repo, continuing..."
        continue
    }
    
    echo "✅ Successfully fused $repo"
    echo ""
done

echo ""
echo "🎉 Nexus Fusion Complete!"
echo "========================="
echo ""
echo "All repositories have been fused into modules/"
echo "Total repositories fused: $count"
echo ""
echo "To push changes, run:"
echo "  git push origin <branch-name>"
