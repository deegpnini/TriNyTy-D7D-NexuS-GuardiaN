# 🚀 Guia de Início - Nexus Guardian D7D

Este guia contém **apenas comandos testados e funcionais**. Nada de "em breve" ou "planejado".

---

## 📋 Pré-requisitos

Antes de começar, verifique:

```bash
# Python 3.12 ou superior
python3 --version

# Git instalado
git --version

# pip disponível
pip3 --version
```

**Requisitos mínimos:**
- Python 3.12+
- Git 2.30+
- 4GB RAM (8GB recomendado)
- 2GB espaço em disco

---

## 📥 Instalação

### 1. Clone o Repositório

```bash
# Clone via HTTPS
git clone https://github.com/deegpnini/TriNyTy-D7D-NexuS-GuardiaN.git

# Entre no diretório
cd TriNyTy-D7D-NexuS-GuardiaN
```

### 2. Crie o Ambiente Virtual

```bash
# Crie o ambiente virtual
python3 -m venv venv

# Ative o ambiente (Linux/Mac)
source venv/bin/activate

# Ative o ambiente (Windows)
venv\Scripts\activate

# Verifique a ativação
which python  # deve apontar para venv/bin/python
```

### 3. Instale as Dependências

```bash
# Atualize pip
pip install --upgrade pip

# Instale os requirements
pip install -r requirements.txt

# Verifique a instalação
pip list | grep -E "fastapi|chromadb|torch"
```

**Nota:** A instalação pode levar 10-30 minutos dependendo da sua conexão.

---

## 🔍 Explorar o Projeto

### Estrutura de Diretórios

```bash
# Liste a estrutura principal
ls -la

# Veja os módulos principais
ls -la src/

# Veja a documentação
ls -la docs/

# Veja os scripts disponíveis
ls -la scripts/
```

### Verificar Código Python

```bash
# Conte linhas de código
find src/ -name "*.py" -exec wc -l {} + | tail -1

# Liste arquivos Python principais
find src/ -name "*.py" | head -20

# Veja o sistema ético
head -50 src/core/claude_ethics.py

# Veja o motor Grok
head -50 src/core/grok_engine.py
```

---

## 🧪 Testar Importações

### Teste Básico de Imports

```bash
# Teste o sistema ético
python3 -c "import sys; sys.path.insert(0, 'src'); from core.claude_ethics import ClaudeEthicalOverride; print('✓ Ethics System OK')"

# Teste o motor Grok
python3 -c "import sys; sys.path.insert(0, 'src'); from core.grok_engine import GrokTruthEngine; print('✓ Grok Engine OK')"
```

**Nota:** Estes testes requerem que as dependências estejam instaladas (`pip install -r requirements.txt`).

---

## 📊 Verificar Status do Projeto

### Status da Fusão

```bash
# Veja o status completo da fusão
cat docs/FUSION_STATUS.md | head -100

# Veja estatísticas
grep "Successfully Integrated" docs/FUSION_STATUS.md
grep "Pending Fusion" docs/FUSION_STATUS.md
```

### Licenças de Terceiros

```bash
# Veja o relatório de licenças
cat docs/THIRD_PARTY_NOTICES.md | head -50

# Conte repositórios escaneados
grep "repository" docs/THIRD_PARTY_NOTICES.md | wc -l
```

### Workflow de Fusão

```bash
# Veja o workflow do GitHub Actions
cat .github/workflows/nexus-fusion.yml | head -50

# Leia a documentação do workflow
cat .github/workflows/NEXUS_FUSION_README.md | head -50
```

---

## 🔧 Scripts Disponíveis

### Script de Fusão Manual

```bash
# Veja o script de fusão
cat scripts/nexus-fusion.sh

# Verifique a sintaxe (não executa)
bash -n scripts/nexus-fusion.sh
echo "✓ Script válido"
```

**⚠️ ATENÇÃO:** Não execute o script de fusão sem entender completamente o que ele faz. Ele faz git subtree de 12 repositórios.

### Setup Termux (Android)

```bash
# Veja o script de setup Termux
cat scripts/setup_termux.sh

# Verifique a sintaxe
bash -n scripts/setup_termux.sh
echo "✓ Script válido"
```

---

## 🔐 Verificar Segurança

### Licenças

```bash
# Veja a licença principal
cat LICENSE | head -50

# Verifique as cláusulas éticas
grep "CLAUSE" LICENSE
```

### Git Ignore

```bash
# Veja o que está ignorado
cat .gitignore

# Verifique que não há secrets commitados
git grep -i "password\|secret\|token\|key" -- ':!.gitignore' || echo "✓ Nenhum secret encontrado"
```

---

## 📝 Git Básico

### Informações do Repositório

```bash
# Veja o remote
git remote -v

# Veja o branch atual
git branch --show-current

# Veja os últimos commits
git log --oneline -10

# Veja o status
git status
```

### Criar um Branch

```bash
# Crie um novo branch para suas mudanças
git checkout -b feature/minha-feature

# Veja os branches
git branch -a
```

---

## 📚 Documentação Adicional

### Arquivos de Documentação Disponíveis

```bash
# Liste toda documentação
ls -la docs/

# README principal
cat README.md | head -100

# Arquitetura (se disponível)
cat ARCHITECTURE.md 2>/dev/null || echo "Arquivo ainda não criado"

# Como contribuir (se disponível)
cat CONTRIBUTING.md 2>/dev/null || echo "Arquivo ainda não criado"

# Framework ético (se disponível)
cat ETHICAL_FRAMEWORK.md 2>/dev/null || echo "Arquivo ainda não criado"
```

---

## 🛠️ Desenvolvimento

### Verificar Python

```bash
# Versão do Python
python3 --version

# Path do Python (dentro do venv)
which python3

# Pacotes instalados
pip list

# Informações do pip
pip --version
```

### Análise de Código

```bash
# Conte linhas por módulo
wc -l src/core/*.py
wc -l src/rag/*.py
wc -l src/multimodal/*.py
wc -l src/architecture/*.py
wc -l src/training/*.py

# Total de linhas Python
find src/ -name "*.py" -exec wc -l {} + | tail -1
```

---

## ❓ Troubleshooting

### Problemas Comuns

**1. "Python 3.12 não encontrado"**
```bash
# Verifique versões disponíveis
ls /usr/bin/python*

# Use python3.12 explicitamente se disponível
python3.12 --version
```

**2. "pip install falha"**
```bash
# Tente com pip3
pip3 install -r requirements.txt

# Ou force reinstalação
pip install --force-reinstall -r requirements.txt
```

**3. "ImportError ao executar testes"**
```bash
# Verifique se o venv está ativo
which python  # deve apontar para venv/

# Reative o venv
source venv/bin/activate  # Linux/Mac
```

**4. "Sem espaço em disco"**
```bash
# Verifique espaço disponível
df -h .

# Limpe cache do pip
pip cache purge
```

---

## 🎯 Próximos Passos

Depois de concluir este guia:

1. ✅ Leia `/docs/FUSION_STATUS.md` para entender o estado do projeto
2. ✅ Leia `/docs/THIRD_PARTY_NOTICES.md` para compliance de licenças
3. ✅ Explore o código em `src/` para entender a arquitetura
4. ✅ Veja `LICENSE` para entender as cláusulas éticas

---

## 📞 Suporte

Se encontrar problemas:

1. **Issues:** Abra um issue em [GitHub Issues](https://github.com/deegpnini/TriNyTy-D7D-NexuS-GuardiaN/issues)
2. **Email:** deegp.nini@gmail.com
3. **Documentação:** Veja outros arquivos em `/docs/`

---

## ⚠️ Avisos Importantes

1. **Este é um projeto em desenvolvimento ativo** - Coisas podem mudar
2. **Não use em produção** sem validação completa
3. **Respeite as cláusulas éticas** do LICENSE
4. **Não execute scripts** sem entender o que fazem
5. **Faça backup** antes de mudanças significativas

---

🌀 **Nexus Guardian D7D - Comandos Testados e Funcionais** 🌀

**Última atualização:** 2026-02-11  
**Versão:** 1.0
