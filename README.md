# 🌀 Nexus Guardian D7D

**TriNyTy-D7D-NexuS-GuardiaN** é um sistema de inteligência artificial educacional focado em análise emocional e aprendizado multimodal. Combina arquitetura split-brain, RAG (Retrieval Augmented Generation), e processamento matemático de emoções para criar experiências de aprendizado adaptativas.

## 📊 Status do Projeto

**CI/CD:** Não configurado  
**Testes:** Não implementados  
**Deploy:** Desenvolvimento local  
**Licença:** MIT + Nexus Ethical Clauses

## 🎯 Funcionalidades Implementadas

### Arquitetura Split-Brain
Sistema de processamento dual que combina:
- **Left Brain (Analítico):** Análise lógica, extração de fatos, verificação de consistência
- **Right Brain (Emocional):** Processamento empático, análise de contexto emocional
- **Síntese:** Integração e validação cruzada entre perspectivas

**Localização:** `src/architecture/split_brain.py`

### Sistema RAG (ChromaDB)
Gerenciamento de conhecimento baseado em vetores com 5 coleções especializadas:
- `facts_knowledge`: Base de fatos verificados
- `emotional_context`: Contexto emocional
- `age_appropriate`: Conteúdo adequado por idade
- `safety_guidelines`: Diretrizes de segurança
- `educational_content`: Material educacional

**Localização:** `src/rag/chroma_manager.py`

### Math-Emotional Bridge
Mapeamento matemático de emoções em espaço vetorial n-dimensional:
- **Dimensões:** Valence, Arousal, Dominance, Certainty, Complexity
- **Operações:** Distância euclidiana, similaridade coseno, análise temporal

**Localização:** `src/rag/math_emotional_bridge.py`

## 🔧 Tecnologias

- **Python 3.x**
- **FastAPI** (0.104.1) - Framework web
- **ChromaDB** (0.4.18) - Vector database
- **PyTorch** (2.1.0) - Machine learning
- **Transformers** (4.36.0) - NLP models
- **Whisper** - Processamento de áudio
- **YOLOv8** - Computer vision

## 🚀 Instalação

```bash
# Clone o repositório
git clone https://github.com/deegpnini/TriNyTy-D7D-NexuS-GuardiaN.git
cd TriNyTy-D7D-NexuS-GuardiaN

# Instale as dependências
pip install -r requirements.txt

# (Opcional) Para otimização Termux/ARM
bash scripts/setup_termux.sh
```

## 📝 Estrutura do Projeto

```
src/
├── architecture/    # Arquitetura split-brain
├── core/           # Componentes principais (nexus, ethics, grok)
├── rag/            # Sistema RAG e math-emotional bridge
├── multimodal/     # Integrações multimodais (whisper, vision)
└── training/       # Módulos de treinamento
```

## 📚 Documentação

- [ARCHITECTURE.md](ARCHITECTURE.md) - Arquitetura técnica detalhada
- [ETHICAL_FRAMEWORK.md](ETHICAL_FRAMEWORK.md) - Framework ético do projeto
- [CONTRIBUTING.md](CONTRIBUTING.md) - Guia de contribuição
- [MANIFESTO.md](MANIFESTO.md) - Manifesto e visão do projeto

## 🛡️ Em desenvolvimento

- Integração completa dos módulos multimodais (whisper, vision)
- Sistema de treinamento e instruction folding
- Testes automatizados e CI/CD pipeline

## 👤 Autor

**Comandante Hebron Nexus** (Helyton Renato Gonçalves Ronchi)

## 📄 Licença

MIT License + Nexus Ethical Clauses - veja [LICENSE](LICENSE) para detalhes.

---

*Para reportar problemas ou contribuir, abra uma issue ou pull request.*
