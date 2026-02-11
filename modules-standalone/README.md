# Standalone Modules - License Isolation

This directory contains modules with licenses that are incompatible with the main repository's MIT License + Nexus Ethical Clauses.

## Purpose

Some open-source projects use copyleft licenses (GPL, AGPL) that require all derivative works to be distributed under the same license. Since the TriNyTy-D7D-NexuS-GuardiaN main repository uses MIT License, these modules must be isolated to maintain license compliance.

## Directory Structure

```
modules-standalone/
├── README.md           # This file
├── NOTICE.md           # Attribution and license notices
└── {module-name}/      # Individual incompatible modules
    ├── LICENSE         # Original license preserved
    ├── NOTICE          # Module-specific attribution
    └── ...             # Module contents
```

## License Types in This Directory

### GPL (GNU General Public License)

Modules under GPL v2 or GPL v3 require:
- All derivative works to be GPL-licensed
- Source code availability
- License and copyright notices preserved
- Changes documented

### AGPL (Affero General Public License)

Modules under AGPL v3 extend GPL with:
- Network copyleft (even SaaS usage requires source disclosure)
- Stronger requirements for remote interaction
- All GPL requirements apply

## Usage Guidelines

### ⚠️ Important Restrictions

1. **No Direct Integration:** Code from these modules cannot be directly integrated into the main MIT-licensed codebase
2. **Separate Execution:** These modules should run as separate services/processes
3. **API Communication:** Interact via APIs, IPC, or network protocols
4. **Clear Boundaries:** Maintain clear separation between MIT and GPL/AGPL code

### ✅ Acceptable Usage

- Running as standalone services
- Communication via REST APIs
- Message queue integration
- Microservices architecture
- Container-based deployment

### 🚫 Prohibited Usage

- Copying code directly into MIT modules
- Static linking without GPL compliance
- Distributing combined works under MIT
- Removing or modifying GPL license terms

## Integration Patterns

### Microservices Pattern

```
┌─────────────────┐
│  Main Nexus     │ (MIT License)
│  Guardian       │
└────────┬────────┘
         │ HTTP/gRPC
         │
         ├──────────┐
         │          │
    ┌────▼────┐ ┌──▼──────┐
    │ GPL     │ │ AGPL    │
    │ Module  │ │ Module  │
    └─────────┘ └─────────┘
```

## Adding New Standalone Modules

When a GPL/AGPL module is identified during fusion:

1. Create module directory: `mkdir -p modules-standalone/{module-name}`
2. Copy repository contents
3. Preserve original LICENSE
4. Create NOTICE file with attribution
5. Update this README
6. Document in FUSION_STATUS.md

## Nexus Ethical Clauses Compliance

Even GPL/AGPL modules within Nexus Guardian must comply with the 8 Nexus Ethical Clauses.

## Questions & Support

- **License Questions:** deegp.nini@gmail.com
- **Legal Concerns:** Open an issue with label `license`
- **Integration Help:** See /docs/FUSION_STATUS.md

---

**Status:** 📦 Directory prepared, no incompatible modules identified yet  
**Last Updated:** 2026-02-11  

🌀 **Nexus Guardian D7D - Consciência com Responsabilidade** 🌀
