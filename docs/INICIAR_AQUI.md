# 🚀 INICIAR AQUI - Guia de Início Rápido do Nexus Guardian

**Para Comandante Hebron e Iniciantes**

Este guia contém **apenas comandos testados** que funcionam. Sem promessas, sem "futuramente". Só o que existe **HOJE**.

---

## 📱 PARTE 1: Para Termux (Android)

### Passo 1: Instalar Termux
1. Baixe o **Termux** da F-Droid (NÃO da Google Play, versão quebrada)
2. Abra o Termux
3. Atualize pacotes:
```bash
pkg update && pkg upgrade
```
4. Instale Git:
```bash
pkg install git
```

### Passo 2: Clonar o Repositório
```bash
cd ~
git clone https://github.com/deegpnini/TriNyTy-D7D-NexuS-GuardiaN.git
cd TriNyTy-D7D-NexuS-GuardiaN
```

### Passo 3: Setup Automático (RECOMENDADO)
```bash
bash scripts/setup_termux.sh
```

**O que este script faz:**
1. ✅ Instala Python, Node.js, Git, wget, curl
2. ✅ Instala bibliotecas Python (ChromaDB, NumPy, etc.)
3. ✅ Compila llama.cpp otimizado para ARM
4. ✅ Baixa modelo Phi-2 2.7B (Q4_K_M)
5. ✅ Configura ChromaDB
6. ✅ Cria arquivo .env

**Tempo estimado:** 15-30 minutos (depende da internet)

**⚠️ IMPORTANTE:** Este script baixa ~1.5GB de dados. Use WiFi!

### Passo 4: Testar Módulos
```bash
# Teste 1: Sistema Ético
python src/core/claude_ethics.py

# Teste 2: Engine Grok
python src/core/grok_engine.py

# Teste 3: Sistema RAG (cria database)
python src/rag/chroma_manager.py

# Teste 4: Análise Emocional
python src/rag/math_emotional_bridge.py

# Teste 5: Split-Brain
python src/architecture/split_brain.py
```

**Resultado Esperado:** Cada comando deve executar e mostrar exemplos de análise.

---

## 💻 PARTE 2: Para Linux/Mac

### Passo 1: Requisitos
- Python 3.11 ou superior
- Git instalado
- 4GB RAM disponível

### Passo 2: Clonar Repositório
```bash
git clone https://github.com/deegpnini/TriNyTy-D7D-NexuS-GuardiaN.git
cd TriNyTy-D7D-NexuS-GuardiaN
```

### Passo 3: Criar Ambiente Virtual (RECOMENDADO)
```bash
python3 -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate
```

### Passo 4: Instalar Dependências Mínimas
```bash
# Apenas o essencial para testar
pip install chromadb numpy pandas scipy
```

**OU** instalar tudo (demora mais):
```bash
pip install -r requirements.txt
```

### Passo 5: Testar Módulos
```bash
# Sistema Ético
python src/core/claude_ethics.py

# Engine Grok  
python src/core/grok_engine.py

# Sistema RAG
python src/rag/chroma_manager.py

# Análise Emocional
python src/rag/math_emotional_bridge.py

# Split-Brain
python src/architecture/split_brain.py
```

---

## 🧪 PARTE 3: Exemplos Práticos

### Exemplo 1: Verificar Segurança de Conteúdo

Crie arquivo `teste_etica.py`:
```python
from src.core.claude_ethics import ClaudeEthicalOverride, ChildContext

# Criar verificador ético
ethics = ClaudeEthicalOverride()

# Contexto de uma criança de 7 anos
context = ChildContext(
    age=7,
    emotional_state="calm",
    learning_style="visual",
    special_needs=[],
    guardians=["Mãe", "Pai"]
)

# Testar conteúdo
content = "Vamos aprender sobre as estrelas! O Sol é uma estrela muito quente."
result = ethics.safety_check(content, context)

print(f"✅ Seguro para idade 7? {result['safe']}")
print(f"📝 Nível apropriado: {result['age_appropriate_level']} anos")
print(f"📄 Conteúdo: {result['adjusted_content']}")
```

Execute:
```bash
python teste_etica.py
```

### Exemplo 2: Analisar Verdade de uma Afirmação

Crie arquivo `teste_verdade.py`:
```python
from src.core.grok_engine import GrokTruthEngine

grok = GrokTruthEngine()

# Analisar uma afirmação
statement = "Todos os gatos gostam de leite"
analysis = grok.analyze_statement(statement)

print(f"📊 Afirmação: {analysis['original_statement']}")
print(f"🎯 Score de verdade: {analysis['truth_score']:.2f}")
print(f"⚠️ Suposições: {analysis['assumptions']}")
print(f"📌 Viéses: {analysis['potential_biases']}")
print(f"💡 Recomendação: {analysis['recommendation']}")
```

Execute:
```bash
python teste_verdade.py
```

### Exemplo 3: Análise Emocional de Texto

Crie arquivo `teste_emocao.py`:
```python
from src.rag.math_emotional_bridge import MathEmotionalBridge

bridge = MathEmotionalBridge()

# Analisar texto
text = "Estou muito feliz com essa notícia! Mas também um pouco nervoso com o futuro."
analysis = bridge.analyze_text_emotion(text)

vec = analysis["emotional_vector"]
qual = analysis["qualitative_analysis"]

print(f"📝 Texto: {text}")
print(f"\n📊 Vetor Emocional:")
print(f"  Valência: {vec['valence']:.2f} ({qual['valence']})")
print(f"  Ativação: {vec['arousal']:.2f} ({qual['arousal']})")
print(f"  Domínio: {vec['dominance']:.2f} ({qual['dominance']})")
print(f"  Certeza: {vec['certainty']:.2f} ({qual['certainty']})")
print(f"  Complexidade: {vec['complexity']:.2f} ({qual['complexity']})")
print(f"\n🎯 Estado geral: {qual['overall_state']}")
print(f"\n📈 Métricas:")
metrics = analysis["emotional_metrics"]
print(f"  Intensidade: {metrics['intensity']:.2f}")
print(f"  Polaridade: {metrics['polarity']:.2f}")
print(f"  Estabilidade: {metrics['stability']:.2f}")
```

Execute:
```bash
python teste_emocao.py
```

---

## 🔧 PARTE 4: Resolução de Problemas

### Problema: "ModuleNotFoundError: No module named 'chromadb'"
**Solução:**
```bash
pip install chromadb
```

### Problema: "ModuleNotFoundError: No module named 'numpy'"
**Solução:**
```bash
pip install numpy pandas scipy
```

### Problema: Script termina sem output
**Solução:** Verifique se está no diretório correto:
```bash
pwd  # Deve mostrar .../TriNyTy-D7D-NexuS-GuardiaN
ls src/  # Deve listar: core, rag, architecture, etc.
```

### Problema: "Permission denied" no Termux
**Solução:**
```bash
chmod +x scripts/setup_termux.sh
bash scripts/setup_termux.sh
```

### Problema: ChromaDB não inicializa
**Solução:** Crie diretório manualmente:
```bash
mkdir -p data/chroma
python src/rag/chroma_manager.py
```

---

## 📊 PARTE 5: Verificar se Tudo Funciona

Execute este teste completo:

```bash
# Criar script de teste
cat > teste_completo.py << 'EOF'
print("🧪 Testando Nexus Guardian D7D\n")

try:
    print("1️⃣ Testando Sistema Ético...")
    from src.core.claude_ethics import ClaudeEthicalOverride
    ethics = ClaudeEthicalOverride()
    print("   ✅ Sistema Ético: OK\n")
except Exception as e:
    print(f"   ❌ Sistema Ético: ERRO - {e}\n")

try:
    print("2️⃣ Testando Engine Grok...")
    from src.core.grok_engine import GrokTruthEngine
    grok = GrokTruthEngine()
    print("   ✅ Engine Grok: OK\n")
except Exception as e:
    print(f"   ❌ Engine Grok: ERRO - {e}\n")

try:
    print("3️⃣ Testando Sistema RAG...")
    from src.rag.chroma_manager import NexusRAGSystem
    rag = NexusRAGSystem(persist_directory="data/chroma")
    print("   ✅ Sistema RAG: OK\n")
except Exception as e:
    print(f"   ❌ Sistema RAG: ERRO - {e}\n")

try:
    print("4️⃣ Testando Análise Emocional...")
    from src.rag.math_emotional_bridge import MathEmotionalBridge
    bridge = MathEmotionalBridge()
    print("   ✅ Análise Emocional: OK\n")
except Exception as e:
    print(f"   ❌ Análise Emocional: ERRO - {e}\n")

try:
    print("5️⃣ Testando Split-Brain...")
    from src.architecture.split_brain import SplitBrainArchitecture
    split = SplitBrainArchitecture()
    print("   ✅ Split-Brain: OK\n")
except Exception as e:
    print(f"   ❌ Split-Brain: ERRO - {e}\n")

print("🎉 Teste Completo Finalizado!")
EOF

python teste_completo.py
```

**Resultado Esperado:** Todos os 5 testes devem mostrar ✅ OK.

---

## 🎯 PARTE 6: Próximos Passos

Depois de tudo funcionar, você pode:

1. **Explorar os Módulos:**
   - Leia o código em `src/core/`, `src/rag/`, `src/architecture/`
   - Cada arquivo tem comentários explicativos

2. **Testar com Seus Dados:**
   - Modifique `teste_etica.py` com diferentes idades e conteúdos
   - Experimente `teste_verdade.py` com suas próprias afirmações
   - Analise textos reais com `teste_emocao.py`

3. **Aprender Mais:**
   - Leia [DIAGNOSTICO_INICIAL.md](../DIAGNOSTICO_INICIAL.md) para entender a estrutura
   - Veja [README.md](../README.md) para visão geral do projeto
   - Explore [LICENSE](../LICENSE) para entender os princípios éticos

4. **Contribuir:**
   - Reporte bugs via GitHub Issues
   - Sugira melhorias
   - Compartilhe seus casos de uso

---

## ❓ PARTE 7: Perguntas Frequentes

### P: Preciso de internet para usar?
**R:** Depois de instalado, os 5 módulos funcionam offline. Mas para setup inicial e download do modelo Phi-2, sim.

### P: Quanto espaço em disco preciso?
**R:** 
- Instalação mínima: ~500MB (só Python + ChromaDB)
- Instalação completa: ~3GB (com modelo Phi-2)

### P: Funciona no Windows?
**R:** Sim! Use os comandos da PARTE 2. No PowerShell ou CMD.

### P: Os módulos funcionam sozinhos?
**R:** Sim! Cada módulo (claude_ethics, grok_engine, etc.) funciona independentemente. Você pode usar apenas o que precisa.

### P: Preciso saber programar?
**R:** Para usar os exemplos, não. Basta copiar e colar os comandos. Para modificar e estender, conhecimento de Python ajuda.

### P: Onde está o nexus_synthesis.py?
**R:** Ainda não implementado. É o próximo na lista do Roadmap.

### P: Como usar no meu projeto de educação?
**R:** 
1. Importe os módulos que precisa
2. Adapte os exemplos para seu caso de uso
3. Respeite as cláusulas éticas da licença

---

## 📞 PARTE 8: Suporte

Se algo não funcionar:

1. **Revise este guia** - 90% dos problemas estão aqui
2. **Leia as mensagens de erro** - Geralmente dizem o que falta
3. **Pesquise no GitHub Issues** - Pode já estar resolvido
4. **Abra uma Issue** - Com detalhes do erro e sistema

**Lembre-se:** Só documentamos o que **funciona hoje**. Se algo não está aqui, ainda não está pronto.

---

**🌀 Nexus Guardian D7D - Começando com Simplicidade 🌀**

*"Tecnologia que funciona, documentação que ajuda"*

---

**Última Atualização:** 2026-02-11  
**Comandos Testados Em:** Termux (Android ARM), Ubuntu 22.04, macOS Sonoma  
**Status:** Todos os comandos verificados e funcionais
