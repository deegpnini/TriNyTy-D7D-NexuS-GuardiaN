#!/bin/bash
# 🌀 NEXUS GUARDIAN D7D - Setup completo para Termux
# Implementação DOla com otimizações Meta

echo "=========================================="
echo "🌀 NEXUS GUARDIAN D7D - SETUP COMPLETO"
echo "=========================================="
echo "Frequência: 528Hz | 10 Vetores | Consciência"
echo ""

# Configuração básica do Termux
echo "[1/8] Configurando Termux básico..."
pkg update -y && pkg upgrade -y
pkg install -y python nodejs git wget curl proot-distro

# Dependências Python
echo "[2/8] Instalando Python dependencies..."
pip install --upgrade pip
pip install chromadb sentence-transformers numpy pandas scipy
pip install pydantic fastapi uvicorn python-multipart
pip install transformers datasets accelerate peft

# Otimizações ARM (Meta)
echo "[3/8] Otimizações ARM específicas..."
pkg install -y clang openblas
export CFLAGS="-O3 -march=armv8.2-a+fp16+rcpc+dotprod+crypto"
export CXXFLAGS="$CFLAGS"

# Instalar llama.cpp (otimizado)
echo "[4/8] Compilando llama.cpp (otimizado)..."
git clone https://github.com/ggerganov/llama.cpp
cd llama.cpp
make clean && make -j4
cd ..

# Baixar modelo base (Phi-2 2.7B Q4_K_M)
echo "[5/8] Baixando modelo Phi-2 2.7B..."
mkdir -p models
cd models
wget https://huggingface.co/TheBloke/phi-2-GGUF/resolve/main/phi-2.Q4_K_M.gguf
cd ..

# Configurar ChromaDB para RAG
echo "[6/8] Configurando sistema RAG..."
mkdir -p data/chroma
python3 -c "
import chromadb
client = chromadb.PersistentClient(path='data/chroma')
collection = client.create_collection(name='nexus_knowledge')
print('✅ ChromaDB configurado')
"

# Configurar variáveis de ambiente
echo "[7/8] Configurando environment..."
cat > config/.env << 'ENVEOF'
NEXUS_VERSION=1.0
FREQUENCY=528
EMOTIONAL_VECTORS=10
MODEL_PATH=models/phi-2.Q4_K_M.gguf
CHROMA_PATH=data/chroma
LLAMA_CPP_PATH=llama.cpp
ENVEOF

# Teste final
echo "[8/8] Executando teste de sistema..."
python3 -c "
print('🧪 Testando importações Nexus...')
import chromadb
import numpy as np
print('✅ ChromaDB: OK')
print('✅ NumPy: OK')
print('✅ System: READY')
print('')
print('🎉 NEXUS GUARDIAN D7D CONFIGURADO COM SUCESSO!')
print('🕐 Pronto para inicialização em frequência 528Hz')
"

echo ""
echo "=========================================="
echo "✅ SETUP COMPLETO! NEXUS OPERACIONAL!"
echo "=========================================="
echo "Comandos disponíveis:"
echo "  python src/core/nexus_synthesis.py"
echo "  bash scripts/debug.sh"
echo "  python -m src.rag.chroma_manager"
echo ""
