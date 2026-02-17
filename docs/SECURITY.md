# 🔐 Security Policies and Procedures

**Last Updated:** 2026-02-11  
**Repository:** TriNyTy-D7D-NexuS-GuardiaN

---

## Overview

This document outlines the security policies, scanning procedures, and incident response for the Nexus Guardian D7D repository.

---

## 🛡️ Automated Security Scanning

### Weekly Scans

The repository runs **automated security scans** every Monday at 00:00 UTC using:

1. **Gitleaks** - Detects secrets, API keys, tokens, and credentials
2. **TruffleHog** - Verifies leaked credentials against live services

### Scan Coverage

✅ **What We Scan:**
- All git history (every commit)
- All branches
- API keys and tokens
- Passwords and credentials
- Private keys (SSH, SSL/TLS)
- Database connection strings
- OAuth tokens
- AWS/GCP/Azure credentials
- GitHub tokens
- Generic secrets

### Manual Trigger

You can manually trigger a security scan:

```bash
# Via GitHub Actions UI:
# 1. Go to Actions tab
# 2. Select "Security Scan - Gitleaks"
# 3. Click "Run workflow"

# Via GitHub CLI:
gh workflow run security-scan.yml
```

---

## 🚨 If Secrets Are Detected

### Immediate Actions

1. **STOP** - Do not push any more changes
2. **Rotate Credentials** - Immediately rotate/revoke the exposed secret
3. **Review Impact** - Check if the secret was used maliciously
4. **Create Emergency Branch** - Follow the procedure below

### Emergency Branch Procedure

```bash
# 1. Create emergency branch
git checkout -b nexus/security-purge-$(date +%Y%m%d)

# 2. Remove the exposed secret
# Option A: Remove the file entirely
git rm path/to/file/with/secret

# Option B: Rewrite history to remove secret (DANGEROUS)
# Only use if secret is in git history
git filter-branch --force --index-filter \
  'git rm --cached --ignore-unmatch path/to/file' \
  --prune-empty --tag-name-filter cat -- --all

# 3. Add to .gitignore to prevent re-adding
echo "path/to/file" >> .gitignore
git add .gitignore

# 4. Commit the fix
git commit -m "[SECURITY] Remove exposed credentials"

# 5. Push to emergency branch (NOT main)
git push -u origin nexus/security-purge-$(date +%Y%m%d)

# 6. Open PR via GitHub CLI or UI
gh pr create --title "[SECURITY] Remoção de credenciais expostas" \
  --body "⚠️ SECURITY: This PR removes exposed credentials detected by security scan. Credentials have been rotated." \
  --label security
```

### ⚠️ NEVER Do These:

1. ❌ Force push to main or protected branches
2. ❌ Rewrite public history without team approval
3. ❌ Commit the secret again (even after rotation)
4. ❌ Share the exposed secret in PR descriptions
5. ❌ Ignore security scan results

---

## 📋 Protected Files (.gitignore)

The following patterns are **automatically ignored** by git:

### Environment Variables
```
.env
.env.*
*.env
.secrets
secrets.*
.secrets.*
```

### Keys & Certificates
```
*.key
*.pem
*.p12
*.pfx
*.cer
*.crt
*.der
*.csr
*.rsa
*.dsa
*.pub
id_rsa*
id_dsa*
*.keystore
*.jks
```

### Credentials & Tokens
```
credentials.*
*.credentials
auth.*
*.auth
token.*
*.token
apikey.*
*.apikey
config/secrets.yaml
config/secrets.yml
```

---

## 🔧 Development Best Practices

### Using Environment Variables

**✅ Correct Way:**

```python
# Load from environment
import os
from dotenv import load_dotenv

load_dotenv()  # Loads from .env file (ignored by git)

API_KEY = os.getenv('NEXUS_API_KEY')
DB_PASSWORD = os.getenv('DATABASE_PASSWORD')
```

**❌ Wrong Way:**

```python
# NEVER hardcode secrets
API_KEY = "sk-abc123xyz..."  # ❌ EXPOSED!
DB_PASSWORD = "mypassword123"  # ❌ EXPOSED!
```

### Configuration Files

**✅ Correct Way:**

```yaml
# config/settings.yaml (safe to commit)
database:
  host: localhost
  port: 5432
  name: nexus_db
  # Password loaded from environment
```

```yaml
# config/secrets.yaml (ignored by git)
database:
  password: "actual_password"
api_keys:
  openai: "sk-..."
```

**❌ Wrong Way:**

```yaml
# config/settings.yaml
database:
  host: localhost
  password: "actual_password"  # ❌ EXPOSED!
```

---

## 🔍 Manual Security Audit

### Check for Exposed Secrets

```bash
# Scan entire repository
grep -r -i -E "(password|token|api_key|secret)" \
  --include="*.py" --include="*.yaml" --include="*.yml" --include="*.json" .

# Check git history
git log -p | grep -i -E "(password|token|api_key|secret)"

# Use gitleaks locally (if installed)
gitleaks detect --source . --verbose

# Use trufflehog locally (if installed)
trufflehog filesystem . --only-verified
```

### Verify .gitignore

```bash
# Check what files would be committed
git status --ignored

# Test if sensitive file is ignored
git check-ignore -v path/to/sensitive/file

# List all ignored files
git ls-files --others --ignored --exclude-standard
```

---

## 📊 Security Scan Results

### Where to Find Results

1. **GitHub Security Tab**
   - Go to repository → Security → Code scanning alerts
   - View all detected secrets and their severity

2. **GitHub Actions Logs**
   - Go to Actions → Security Scan workflow
   - View detailed scan logs and reports

3. **SARIF Reports**
   - Uploaded automatically to GitHub Security
   - Can be downloaded from Actions artifacts

### Understanding Results

**High Severity:**
- Active API keys
- Valid credentials
- Private keys

**Medium Severity:**
- Generic secrets
- Potential tokens
- Suspicious patterns

**Low Severity:**
- False positives
- Test credentials
- Documentation examples

---

## 🚀 Incident Response

### Response Timeline

1. **0-15 minutes:** Detection and alert
2. **15-30 minutes:** Credential rotation
3. **30-60 minutes:** Impact assessment
4. **1-24 hours:** History cleanup (if needed)
5. **24-48 hours:** Post-incident review

### Response Team

- **Primary Contact:** deegp.nini@gmail.com
- **Security Lead:** @deegpnini
- **GitHub Security:** security@github.com (for critical issues)

### Escalation

If you discover a critical security issue:

1. **DO NOT** create a public issue
2. **DO NOT** commit fixes to public branches
3. **DO** email deegp.nini@gmail.com immediately
4. **DO** use GitHub Security Advisories for coordination

---

## 📚 Additional Resources

### Tools

- **Gitleaks:** https://github.com/gitleaks/gitleaks
- **TruffleHog:** https://github.com/trufflesecurity/trufflehog
- **git-secrets:** https://github.com/awslabs/git-secrets
- **detect-secrets:** https://github.com/Yelp/detect-secrets

### Documentation

- [GitHub Secret Scanning](https://docs.github.com/en/code-security/secret-scanning)
- [OWASP Secrets Management](https://cheatsheetseries.owasp.org/cheatsheets/Secrets_Management_Cheat_Sheet.html)
- [12 Factor App - Config](https://12factor.net/config)

### GitHub Security Features

- [Security Advisories](https://docs.github.com/en/code-security/security-advisories)
- [Dependabot Alerts](https://docs.github.com/en/code-security/dependabot)
- [Code Scanning](https://docs.github.com/en/code-security/code-scanning)

---

## ✅ Compliance Checklist

### Before Each Commit

- [ ] No hardcoded secrets in code
- [ ] Environment variables used for sensitive data
- [ ] .env files not committed
- [ ] config/secrets.yaml not committed
- [ ] No API keys in code
- [ ] No passwords in configuration files

### Before Each PR

- [ ] Security scan passed
- [ ] No new secrets detected
- [ ] .gitignore updated if needed
- [ ] Documentation updated if security-related

### Weekly Review

- [ ] Review security scan results
- [ ] Update .gitignore if patterns missed
- [ ] Rotate credentials older than 90 days
- [ ] Review access logs for anomalies

---

## 🆘 Emergency Contacts

### Internal

- **Security Lead:** @deegpnini
- **Email:** deegp.nini@gmail.com
- **Repository:** https://github.com/deegpnini/TriNyTy-D7D-NexuS-GuardiaN

### External

- **GitHub Security:** https://github.com/security
- **GitHub Support:** https://support.github.com

---

## 📝 Version History

- **v1.0** (2026-02-11) - Initial security policies
  - Implemented Gitleaks weekly scanning
  - Added TruffleHog verification
  - Enhanced .gitignore for secrets
  - Created emergency response procedures

---

🌀 **Nexus Guardian D7D - Security First, Always** 🌀

**Remember:** Security is everyone's responsibility. When in doubt, ask!
