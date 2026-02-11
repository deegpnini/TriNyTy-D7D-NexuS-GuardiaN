# 🚨 Security Quick Reference

## Emergency Response for Exposed Secrets

### 1. IMMEDIATE: Rotate Credentials
```bash
# Rotate the exposed secret IMMEDIATELY
# Don't wait for git cleanup
```

### 2. Create Emergency Branch
```bash
git checkout -b nexus/security-purge-$(date +%Y%m%d)
```

### 3. Remove Secret
```bash
# Remove file
git rm path/to/file/with/secret

# OR edit file to remove secret
vim path/to/file/with/secret
git add path/to/file/with/secret
```

### 4. Update .gitignore
```bash
echo "path/to/file" >> .gitignore
git add .gitignore
```

### 5. Commit & Push
```bash
git commit -m "[SECURITY] Remove exposed credentials"
git push -u origin nexus/security-purge-$(date +%Y%m%d)
```

### 6. Open PR
```bash
gh pr create --title "[SECURITY] Remoção de credenciais expostas" \
  --body "⚠️ Removed exposed credentials. Secrets have been rotated." \
  --label security
```

---

## Files That Should NEVER Be Committed

### ❌ NEVER Commit These:
- `.env` files
- `*.key` files (SSH, SSL, etc.)
- `*.pem` certificates
- `secrets.*` files
- `credentials.*` files
- `token.*` files
- `config/secrets.yaml`
- Any file with passwords/API keys

### ✅ ALWAYS Commit These:
- `.env.example` (without real values)
- `config/settings.yaml` (without secrets)
- `secrets.example.*` (template files)
- Documentation about secrets (not the secrets themselves)

---

## Quick Checks Before Commit

```bash
# 1. Check what will be committed
git status

# 2. Review changes
git diff

# 3. Scan for common secret patterns
git diff --cached | grep -i -E "(password|token|api_key|secret)"

# 4. Verify ignored files
git status --ignored

# 5. Test .gitignore
git check-ignore -v path/to/file
```

---

## Security Scan Commands

```bash
# Manual scan with grep
grep -r -i -E "(password|token|api_key|secret)" \
  --include="*.py" --include="*.yaml" .

# Check git history
git log -p | grep -i "password"

# Trigger GitHub Actions scan
gh workflow run security-scan.yml
```

---

## Common Mistakes to Avoid

### ❌ Mistake 1: Hardcoded Secrets
```python
API_KEY = "sk-abc123xyz..."  # DON'T DO THIS!
```

### ✅ Correct: Use Environment Variables
```python
import os
API_KEY = os.getenv('NEXUS_API_KEY')
```

### ❌ Mistake 2: Committing .env
```bash
git add .env  # DON'T DO THIS!
```

### ✅ Correct: Use .env.example
```bash
cp .env .env.example
# Remove real values from .env.example
git add .env.example
```

### ❌ Mistake 3: Secrets in Logs
```python
print(f"API Key: {api_key}")  # DON'T DO THIS!
```

### ✅ Correct: Log Safely
```python
print("API Key: [REDACTED]")
```

---

## Contact

**Security Issues:** deegp.nini@gmail.com

**Full Documentation:** [docs/SECURITY.md](SECURITY.md)

---

🔐 **When in doubt, DON'T commit. Ask first!**
