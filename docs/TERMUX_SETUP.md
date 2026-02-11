# 📱 Termux Setup Guide - Nexus Guardian D7D

**Platform:** Android Termux  
**Architecture:** ARM64/ARM  
**Last Updated:** 2026-02-11

---

## ⚠️ Important Warnings

### Ollama on Termux is NOT Stable

**DO NOT use Ollama install.sh on Termux!**

Ollama is **not officially supported** on Android/Termux and has known stability issues:
- ❌ Frequent crashes
- ❌ Memory leaks
- ❌ ARM compatibility problems
- ❌ Installation script failures

### ✅ Recommended Approach

Use **llama.cpp** directly - it's stable, lightweight, and ARM-optimized.

---

## 🚀 Quick Start - Manual llama.cpp Setup

### Prerequisites

```bash
# Update Termux
pkg update && pkg upgrade -y

# Install required packages
pkg install -y python git wget curl clang make cmake
pkg install -y openblas libandroid-execinfo proot-distro

# Python dependencies
pip install --upgrade pip
pip install numpy pandas scipy chromadb sentence-transformers
```

### Step 1: Compile llama.cpp (ARM Optimized)

```bash
# Clone llama.cpp
cd ~
git clone https://github.com/ggerganov/llama.cpp
cd llama.cpp

# ARM-specific optimizations
export CFLAGS="-O3 -march=armv8.2-a+fp16+rcpc+dotprod+crypto"
export CXXFLAGS="$CFLAGS"

# Compile with ARM optimizations
make clean
make -j$(nproc)

# Verify compilation
./main --version
```

**Expected output:**
```
llama.cpp version: [version number]
built with ARM NEON support
```

### Step 2: Download Phi-2 Model (1.6GB)

**Direct Download Link (No Ollama Required):**

```bash
# Create models directory
mkdir -p ~/models
cd ~/models

# Download Phi-2 2.7B Q4_K_M quantized model
# This is a 1.6GB file - optimized for mobile
wget https://huggingface.co/TheBloke/phi-2-GGUF/resolve/main/phi-2.Q4_K_M.gguf

# Verify download
ls -lh phi-2.Q4_K_M.gguf
```

**Alternative smaller models (if space is limited):**

```bash
# Phi-2 Q2_K (1.1GB - faster, less accurate)
wget https://huggingface.co/TheBloke/phi-2-GGUF/resolve/main/phi-2.Q2_K.gguf

# TinyLlama 1.1B Q4_K_M (637MB - very fast)
wget https://huggingface.co/TheBloke/TinyLlama-1.1B-Chat-v1.0-GGUF/resolve/main/tinyllama-1.1b-chat-v1.0.Q4_K_M.gguf
```

### Step 3: Test llama.cpp (Subprocess Method)

Create `test_llama.py`:

```python
#!/usr/bin/env python3
"""
Test llama.cpp without importing ollama
Uses subprocess to communicate with llama.cpp directly
"""

import subprocess
import os
from pathlib import Path

def test_llama_cpp():
    """Test llama.cpp availability and functionality"""
    
    # Paths
    llama_cpp_path = Path.home() / "llama.cpp" / "main"
    model_path = Path.home() / "models" / "phi-2.Q4_K_M.gguf"
    
    # Check llama.cpp exists
    if not llama_cpp_path.exists():
        print("❌ llama.cpp not found at:", llama_cpp_path)
        print("   Run: cd ~/llama.cpp && make")
        return False
    
    # Check model exists
    if not model_path.exists():
        print("❌ Model not found at:", model_path)
        print("   Download from: https://huggingface.co/TheBloke/phi-2-GGUF")
        return False
    
    print("✅ llama.cpp found")
    print("✅ Model found")
    
    # Test inference
    try:
        prompt = "Hello, I am Nexus Guardian D7D."
        
        result = subprocess.run(
            [
                str(llama_cpp_path),
                "-m", str(model_path),
                "-p", prompt,
                "-n", "50",  # Generate 50 tokens
                "--temp", "0.7",
                "--top-p", "0.9",
                "-c", "2048"  # Context size
            ],
            capture_output=True,
            text=True,
            timeout=60
        )
        
        if result.returncode == 0:
            print("\n✅ Inference test PASSED")
            print("\nOutput:")
            print(result.stdout[:200] + "..." if len(result.stdout) > 200 else result.stdout)
            return True
        else:
            print("❌ Inference test FAILED")
            print("Error:", result.stderr)
            return False
            
    except subprocess.TimeoutExpired:
        print("❌ Inference timed out (>60s)")
        return False
    except Exception as e:
        print(f"❌ Error running inference: {e}")
        return False

def test_ethical_fallback():
    """Test that ethical system works WITHOUT llama.cpp"""
    print("\n🧪 Testing ethical fallback (no LLM required)...")
    
    try:
        # This should work without any LLM
        from src.core.claude_ethics import ClaudeEthicalOverride, ChildContext
        
        ethics = ClaudeEthicalOverride()
        
        # Test case: child asking about emotions
        context = ChildContext(
            age=10,
            emotional_state="curious",
            learning_style="visual",
            special_needs=[],
            guardians=["parent1"]
        )
        
        test_content = "I feel sad sometimes. Is that okay?"
        result = ethics.safety_check(test_content, context)
        
        print(f"✅ Ethical system working: {result['safe']}")
        return True
        
    except Exception as e:
        print(f"❌ Ethical fallback failed: {e}")
        return False

if __name__ == "__main__":
    print("=" * 50)
    print("🌀 Nexus Guardian D7D - Termux Test")
    print("=" * 50)
    
    # Test 1: llama.cpp (optional)
    print("\n[Test 1] llama.cpp with subprocess...")
    llama_works = test_llama_cpp()
    
    # Test 2: Ethical fallback (required)
    print("\n[Test 2] Ethical fallback system...")
    fallback_works = test_ethical_fallback()
    
    print("\n" + "=" * 50)
    print("📊 Test Results:")
    print("=" * 50)
    print(f"llama.cpp: {'✅ PASS' if llama_works else '⚠️  OPTIONAL'}")
    print(f"Ethical Fallback: {'✅ PASS' if fallback_works else '❌ FAIL (CRITICAL!)'}")
    
    if not fallback_works:
        print("\n❌ CRITICAL: Ethical fallback must work without LLM!")
        exit(1)
    
    if not llama_works:
        print("\n⚠️  Note: llama.cpp not available, using ethical fallback only")
    
    print("\n✅ System ready for Nexus Guardian operation")
```

### Step 4: Run Tests

```bash
# Make test script executable
chmod +x test_llama.py

# Run tests
python test_llama.py
```

---

## 🔧 Integration with Nexus Guardian

### Optional Ollama Import Pattern

If you want to optionally use ollama when available, use this pattern:

```python
# In your Python code (e.g., src/core/nexus_synthesis.py)

try:
    import ollama
    OLLAMA_AVAILABLE = True
except ImportError:
    OLLAMA_AVAILABLE = False
    print("⚠️ Ollama não disponível. Usando fallback ético.")

class NexusEngine:
    def __init__(self):
        self.use_llm = OLLAMA_AVAILABLE
        
        if self.use_llm:
            print("✅ LLM mode: Ollama detected")
        else:
            print("✅ Ethical mode: Pure rules-based system")
    
    def generate_response(self, prompt: str) -> str:
        """Generate response with optional LLM"""
        
        if self.use_llm:
            # Use Ollama if available
            try:
                response = ollama.generate(
                    model='phi',
                    prompt=prompt
                )
                return response['response']
            except Exception as e:
                print(f"⚠️ LLM failed: {e}, falling back to ethical mode")
                return self._ethical_fallback(prompt)
        else:
            # Use ethical fallback
            return self._ethical_fallback(prompt)
    
    def _ethical_fallback(self, prompt: str) -> str:
        """Ethical response without LLM"""
        # This MUST work without any external model
        from src.core.claude_ethics import ClaudeEthicalOverride
        
        ethics = ClaudeEthicalOverride()
        # Generate safe, ethical response using rules
        return ethics.generate_safe_response(prompt)
```

### Using llama.cpp via Subprocess

```python
import subprocess
from pathlib import Path

class LlamaCppEngine:
    """Direct llama.cpp interface via subprocess"""
    
    def __init__(self):
        self.llama_path = Path.home() / "llama.cpp" / "main"
        self.model_path = Path.home() / "models" / "phi-2.Q4_K_M.gguf"
        self.available = self._check_available()
    
    def _check_available(self) -> bool:
        """Check if llama.cpp and model are available"""
        return (
            self.llama_path.exists() and 
            self.model_path.exists()
        )
    
    def generate(self, prompt: str, max_tokens: int = 100) -> str:
        """Generate text using llama.cpp"""
        if not self.available:
            raise RuntimeError("llama.cpp not available")
        
        try:
            result = subprocess.run(
                [
                    str(self.llama_path),
                    "-m", str(self.model_path),
                    "-p", prompt,
                    "-n", str(max_tokens),
                    "--temp", "0.7"
                ],
                capture_output=True,
                text=True,
                timeout=60
            )
            
            if result.returncode == 0:
                return result.stdout
            else:
                raise RuntimeError(f"llama.cpp error: {result.stderr}")
                
        except subprocess.TimeoutExpired:
            raise RuntimeError("Generation timed out")
```

---

## 🛡️ Ethical Fallback (Required)

**The ethical fallback MUST work without Phi-2 or any LLM.**

### Why This Matters

1. **Reliability:** External models can fail
2. **Safety:** Children need protection even if LLM is down
3. **Performance:** Rules-based is faster on mobile
4. **Privacy:** No data sent to external models

### Example Ethical Fallback

```python
class EthicalFallback:
    """Pure rules-based system - no LLM required"""
    
    def __init__(self):
        self.safe_responses = {
            "greeting": [
                "Olá! Como posso ajudar você hoje?",
                "Oi! Estou aqui para conversar.",
            ],
            "emotion": [
                "É completamente normal sentir isso.",
                "Seus sentimentos são válidos.",
            ],
            "learning": [
                "Vamos aprender juntos!",
                "Que pergunta interessante!",
            ]
        }
        
        self.red_flags = [
            "self_harm", "suicídio", "machucar",
            "odiar", "violência", "bullying"
        ]
    
    def generate_response(self, prompt: str) -> str:
        """Generate safe response without LLM"""
        
        # Safety check
        if any(flag in prompt.lower() for flag in self.red_flags):
            return (
                "🛡️ Percebi que você pode estar passando por um momento difícil. "
                "Por favor, converse com um adulto de confiança ou ligue para "
                "o CVV (188) se precisar de ajuda."
            )
        
        # Detect intent and respond
        if any(word in prompt.lower() for word in ["oi", "olá", "hello"]):
            return self.safe_responses["greeting"][0]
        
        if any(word in prompt.lower() for word in ["triste", "sad", "sentir"]):
            return self.safe_responses["emotion"][0]
        
        # Default safe response
        return (
            "Entendo sua pergunta. Como esse é um sistema focado em segurança, "
            "recomendo conversar com um professor ou responsável sobre isso."
        )
```

---

## 📊 Performance Expectations

### Termux Hardware Requirements

**Minimum:**
- 4GB RAM
- 8GB free storage
- Android 8.0+
- ARM64 CPU

**Recommended:**
- 6GB+ RAM
- 16GB+ free storage
- Android 10+
- ARM64 with NEON support

### Model Performance

| Model | Size | Tokens/sec | RAM Usage | Quality |
|-------|------|------------|-----------|---------|
| Phi-2 Q4_K_M | 1.6GB | 4-8 tok/s | 2.5GB | High |
| Phi-2 Q2_K | 1.1GB | 8-15 tok/s | 2.0GB | Medium |
| TinyLlama Q4 | 637MB | 15-25 tok/s | 1.5GB | Low-Medium |

**Note:** Performance varies by device. Older phones may be slower.

---

## 🔍 Troubleshooting

### "llama.cpp compilation failed"

```bash
# Install missing dependencies
pkg install -y clang make cmake

# Try with basic flags
export CFLAGS="-O2"
export CXXFLAGS="-O2"
make clean && make
```

### "Out of memory during inference"

```bash
# Use smaller model
wget https://huggingface.co/TheBloke/TinyLlama-1.1B-Chat-v1.0-GGUF/resolve/main/tinyllama-1.1b-chat-v1.0.Q4_K_M.gguf

# Reduce context size
./main -m model.gguf -p "prompt" -c 512  # Instead of 2048
```

### "Model download interrupted"

```bash
# Resume download with wget
wget -c https://huggingface.co/TheBloke/phi-2-GGUF/resolve/main/phi-2.Q4_K_M.gguf

# Or use curl with resume
curl -C - -o phi-2.Q4_K_M.gguf https://huggingface.co/TheBloke/phi-2-GGUF/resolve/main/phi-2.Q4_K_M.gguf
```

### "Subprocess hangs during inference"

```python
# Add timeout to subprocess
result = subprocess.run(
    [...],
    timeout=30  # Kill after 30 seconds
)
```

---

## 🎯 Best Practices

### 1. Always Have Fallback

```python
def safe_generate(prompt: str) -> str:
    """Always returns something, even if LLM fails"""
    try:
        if LLAMA_AVAILABLE:
            return llama_generate(prompt)
    except Exception as e:
        print(f"⚠️ LLM error: {e}")
    
    # Fallback always works
    return ethical_fallback(prompt)
```

### 2. Test Without Model

```bash
# System should still work without model
python -c "
from src.core.claude_ethics import ClaudeEthicalOverride
ethics = ClaudeEthicalOverride()
print('✅ Ethical system works without LLM')
"
```

### 3. Monitor Memory

```python
import psutil

def check_memory():
    mem = psutil.virtual_memory()
    if mem.percent > 90:
        print("⚠️ Low memory! Consider using smaller model")
```

### 4. Use Timeouts

```python
# Always set timeout for subprocess
subprocess.run([...], timeout=60)
```

---

## 📚 Additional Resources

### Official Documentation

- [llama.cpp GitHub](https://github.com/ggerganov/llama.cpp)
- [Termux Wiki](https://wiki.termux.com/)
- [HuggingFace GGUF Models](https://huggingface.co/models?library=gguf)

### Model Resources

- [TheBloke GGUF Models](https://huggingface.co/TheBloke)
- [Phi-2 Model Card](https://huggingface.co/microsoft/phi-2)
- [GGUF Format Specification](https://github.com/ggerganov/ggml/blob/master/docs/gguf.md)

### Termux Resources

- [Termux Setup Guide](https://github.com/termux/termux-app)
- [ARM Optimization Tips](https://community.arm.com/arm-community-blogs/b/tools-software-ides-blog)
- [Android ML Best Practices](https://developer.android.com/ml)

---

## ✅ Verification Checklist

Before deploying to production:

- [ ] llama.cpp compiles successfully
- [ ] Model downloads completely (verify with `ls -lh`)
- [ ] Subprocess test passes
- [ ] Ethical fallback works WITHOUT model
- [ ] Memory usage < 80% during inference
- [ ] Inference time < 60 seconds
- [ ] System gracefully handles model failures
- [ ] No `import ollama` in production code (use try-except if optional)

---

## 🆘 Emergency Contacts

If you encounter critical issues:

- **Repository:** https://github.com/deegpnini/TriNyTy-D7D-NexuS-GuardiaN
- **Issues:** Tag with `termux` label
- **Email:** deegp.nini@gmail.com

---

🌀 **Nexus Guardian D7D - Funciona com ou sem LLM** 🌀

**Princípio Fundamental:** A proteção ética NUNCA depende de um modelo externo.

**Last Updated:** 2026-02-11  
**Version:** 1.0
