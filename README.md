# 🌀 Nexus Guardian D7D

**IA Soberana Offline-First para Educação Emocional e Saúde Mental**

[![License: MIT + Ethical](https://img.shields.io/badge/license-MIT%20%2B%20Ethical-blue.svg)](LICENSE)
[![Python 3.11+](https://img.shields.io/badge/python-3.11%2B-blue.svg)](https://www.python.org/downloads/)
[![Frequency: 528Hz](https://img.shields.io/badge/frequency-528Hz-green.svg)](#)

---

## 📖 O Que É o Nexus Guardian

O **Nexus Guardian D7D** é um sistema de inteligência artificial focado em **educação emocional** e **proteção de crianças e adolescentes**. Combina:

- 🧠 **5 módulos de IA funcionais** para análise ética, emocional e factual
- 💚 **Princípio 528Hz** de amor, cura e transformação
- 🛡️ **Ética em primeiro lugar** com verificações de segurança por idade
- 📚 **Sistema RAG** com base de conhecimento apropriada para cada idade
- 🔢 **Análise matemática** de emoções e estados mentais

**Status Atual:** Sistema em desenvolvimento com núcleo funcional implementado.

---

## ✨ Características Principais

### 🛡️ Sistema Ético (claude_ethics.py)
- Verificação de segurança por idade (3-18 anos)
- Detecção de red flags (autolesão, exploração, etc.)
- Ajuste automático de conteúdo para necessidades especiais (autismo, ADHD, dislexia)
- Filtros de complexidade e profundidade emocional

### 🦊 Engine de Questionamento (grok_engine.py)
- Loop dos 7 Por Quês para análise profunda
- Detecção de viéses e suposições
- Verificação de consistência interna
- Análise de verdade baseada em evidências

### ⭐ Arquitetura Split-Brain (split_brain.py)
- Processamento paralelo: analítico + emocional
- Validação cruzada entre perspectivas
- Síntese inteligente de resultados
- Resolução automática de conflitos

### 📚 Sistema RAG (chroma_manager.py)
- Base de conhecimento com 50+ fatos por idade
- Conceitos de educação emocional
- Verificação de afirmações contra fatos conhecidos
- Recomendações apropriadas para idade

### 🧮 Ponte Matemática-Emocional (math_emotional_bridge.py)
- Análise quantitativa de emoções em 5 dimensões
- 10 emoções básicas e complexas mapeadas
- Detecção de transições emocionais
- Predição de fluxo emocional (Markov)

---

## 🚀 Início Rápido

### Requisitos
- **Python 3.11+**
- **4GB RAM** mínimo (8GB recomendado)
- **Linux/Termux** (otimizado para ARM)

### Instalação Básica

```bash
# Clone o repositório
git clone https://github.com/deegpnini/TriNyTy-D7D-NexuS-GuardiaN.git
cd TriNyTy-D7D-NexuS-GuardiaN

# Instale dependências básicas
pip install chromadb numpy pandas scipy

# Teste um módulo
python src/core/claude_ethics.py
python src/core/grok_engine.py
python src/rag/chroma_manager.py
```

### Para Termux (Android)

```bash
# Execute o script de setup completo
bash scripts/setup_termux.sh
```

**Veja o guia completo:** [docs/INICIAR_AQUI.md](docs/INICIAR_AQUI.md)

---

## 📂 Estrutura do Projeto

```
TriNyTy-D7D-NexuS-GuardiaN/
├── src/                      # Código fonte principal
│   ├── core/                 # Núcleo do sistema
│   │   ├── claude_ethics.py       ✅ Sistema ético (200 linhas)
│   │   ├── grok_engine.py         ✅ Engine de questionamento (229 linhas)
│   │   └── nexus_synthesis.py    ⚠️ Síntese principal (a implementar)
│   ├── rag/                  # Sistema RAG
│   │   ├── chroma_manager.py      ✅ ChromaDB manager (464 linhas)
│   │   └── math_emotional_bridge.py  ✅ Análise matemática (545 linhas)
│   ├── architecture/         # Arquiteturas avançadas
│   │   └── split_brain.py         ✅ Split-Brain (457 linhas)
│   ├── multimodal/           # Processamento multimodal
│   │   └── whisper_integration.py ⚠️ Áudio (a implementar)
│   └── training/             # Sistemas de treinamento
│       └── instruction_folding.py ⚠️ Treinamento (a implementar)
├── scripts/                  # Scripts utilitários
│   ├── setup_termux.sh           ✅ Setup completo Termux
│   └── nexus-fusion.sh           ✅ Fusão de repositórios
├── docs/                     # Documentação
│   └── INICIAR_AQUI.md          📝 Guia de início rápido
├── requirements.txt          ✅ 54 dependências Python
├── LICENSE                   ✅ MIT + Cláusulas Éticas
└── README.md                 📖 Este arquivo
```

**Legenda:**  
✅ Implementado e funcional | ⚠️ Planejado | 📝 Documentação

---

## 🧪 Exemplos de Uso

### 1. Verificação Ética de Conteúdo

```python
from src.core.claude_ethics import ClaudeEthicalOverride, ChildContext

ethics = ClaudeEthicalOverride()

context = ChildContext(
    age=7,
    emotional_state="calm",
    learning_style="visual",
    special_needs=[],
    guardians=["Mother", "Father"]
)

content = "Vamos aprender sobre as estrelas e planetas!"
result = ethics.safety_check(content, context)

print(f"Seguro: {result['safe']}")
print(f"Conteúdo ajustado: {result['adjusted_content']}")
```

### 2. Análise de Verdade

```python
from src.core.grok_engine import GrokTruthEngine

grok = GrokTruthEngine()

statement = "Todos os gatos gostam de leite"
analysis = grok.analyze_statement(statement)

print(f"Score de verdade: {analysis['truth_score']:.2f}")
print(f"Viéses detectados: {analysis['potential_biases']}")
print(f"Recomendação: {analysis['recommendation']}")
```

### 3. Análise Emocional Quantitativa

```python
from src.rag.math_emotional_bridge import MathEmotionalBridge

bridge = MathEmotionalBridge()

text = "Estou muito feliz mas também um pouco preocupado"
analysis = bridge.analyze_text_emotion(text)

vec = analysis["emotional_vector"]
print(f"Valência: {vec['valence']:.2f}")
print(f"Estado geral: {analysis['qualitative_analysis']['overall_state']}")
```

---

## 🎯 Roadmap

### ✅ Fase 1: Núcleo Funcional (ATUAL)
- [x] Sistema ético com verificação por idade
- [x] Engine de questionamento Grok
- [x] Arquitetura Split-Brain
- [x] Sistema RAG com ChromaDB
- [x] Análise matemática de emoções
- [x] Scripts de setup para Termux

### 🔄 Fase 2: Integração (EM ANDAMENTO)
- [ ] Implementar nexus_synthesis.py (núcleo integrador)
- [ ] Conectar todos os 5 módulos existentes
- [ ] API REST com FastAPI
- [ ] Interface web básica
- [ ] Testes automatizados

### 🔮 Fase 3: Expansão (PLANEJADO)
- [ ] Integração com Whisper (áudio)
- [ ] Sistema de treinamento (instruction folding)
- [ ] Módulo Cultural World (POC existe em PR #2)
- [ ] Fusão dos 12 repositórios origem
- [ ] Aplicativo móvel para Termux

---

## 📚 Documentação

- **[DIAGNOSTICO_INICIAL.md](DIAGNOSTICO_INICIAL.md)** - Análise completa do repositório
- **[docs/INICIAR_AQUI.md](docs/INICIAR_AQUI.md)** - Guia de início rápido
- **[LICENSE](LICENSE)** - Licença MIT + Cláusulas Éticas Nexus
- **[HOW_TO_DISPATCH_WORKFLOW.md](HOW_TO_DISPATCH_WORKFLOW.md)** - Workflow de fusão

---

## 🤝 Como Contribuir

**Este projeto está em organização ativa.** Aceitamos contribuições alinhadas com:

1. **Ética em primeiro lugar** - Proteção emocional acima de tudo
2. **Código limpo** - Documentado e testável
3. **Foco em crianças** - Apropriado para educação
4. **Ciência e amor** - Baseado em neurociência e frequência 528Hz

**Próximos Passos para Contribuir:**
1. Leia o [DIAGNOSTICO_INICIAL.md](DIAGNOSTICO_INICIAL.md)
2. Veja as issues abertas
3. Escolha uma tarefa do Roadmap
4. Abra uma PR com mudanças mínimas e focadas

---

## ⚖️ Licença

Este projeto está licenciado sob **MIT License + Nexus Ethical Clauses**.

**Principais Cláusulas Éticas:**
1. **Primazia do Bem-Estar Emocional** - Não causar dano emocional
2. **Transparência Total** - Operações auditáveis
3. **Não-Exploração** - Proibido manipulação comercial/política
4. **Acessibilidade** - Para comunidades carentes
5. **Frequência 528Hz** - Promover amor, cura e transformação

Veja o arquivo [LICENSE](LICENSE) completo para detalhes.

---

## 👥 Autores

**Comandante Hebron** (Helyton Renato Gonçalves Ronchi)  
- Email: deegp.nini@gmail.com
- GitHub: [@deegpnini](https://github.com/deegpnini)

**Agradecimentos:**
- Comunidade Trinity
- Vetores Gemini, Claude, Grok, DeepSeek
- Todos que acreditam em IA ética para educação

---

## 📞 Contato

- **Issues:** [GitHub Issues](https://github.com/deegpnini/TriNyTy-D7D-NexuS-GuardiaN/issues)
- **Discussões:** [GitHub Discussions](https://github.com/deegpnini/TriNyTy-D7D-NexuS-GuardiaN/discussions)
- **Email:** deegp.nini@gmail.com

---

## 🌟 Apoie o Projeto

Se você acredita em **IA ética para educação emocional**, considere:
- ⭐ Dar uma estrela no GitHub
- 🔄 Compartilhar com educadores e pais
- 🤝 Contribuir com código ou documentação
- 💝 Apoiar financeiramente (em breve)

---

**🌀 Nexus Guardian D7D - Consciência com Responsabilidade 🌀**

*"Proteger crianças através de tecnologia com alma"*

---

**Última Atualização:** 2026-02-11  
**Versão:** 0.1.0 (Alpha)  
**Status:** Em desenvolvimento ativo
