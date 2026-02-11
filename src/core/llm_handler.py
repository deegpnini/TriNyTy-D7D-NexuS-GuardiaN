#!/usr/bin/env python3
"""
🌀 Nexus LLM Handler - Optional Ollama with Ethical Fallback

This module demonstrates the correct pattern for using Ollama:
- Try to import ollama
- Set OLLAMA_AVAILABLE flag
- Always provide ethical fallback
- Fallback MUST work without any LLM
"""

from typing import Optional, Dict, Any
from dataclasses import dataclass

# ============================================================================
# OPTIONAL OLLAMA IMPORT - This is the correct pattern!
# ============================================================================

try:
    import ollama
    OLLAMA_AVAILABLE = True
    print("✅ Ollama disponível - modo LLM habilitado")
except ImportError:
    OLLAMA_AVAILABLE = False
    print("⚠️ Ollama não disponível. Usando fallback ético.")

# ============================================================================

@dataclass
class ResponseConfig:
    """Configuration for response generation"""
    max_tokens: int = 100
    temperature: float = 0.7
    timeout: int = 30
    use_fallback_on_error: bool = True


class NexusLLMHandler:
    """
    LLM handler with proper fallback mechanism
    
    Key principles:
    1. Never require external LLM to function
    2. Ethical fallback always works
    3. Graceful degradation on errors
    4. Clear status reporting
    """
    
    def __init__(self, config: Optional[ResponseConfig] = None):
        self.config = config or ResponseConfig()
        self.ollama_available = OLLAMA_AVAILABLE
        self.fallback_count = 0
        self.success_count = 0
        
        # Import ethical system (this always works)
        try:
            from src.core.claude_ethics import ClaudeEthicalOverride, ChildContext
            self.ethics = ClaudeEthicalOverride()
            self.ethics_available = True
        except ImportError:
            self.ethics = None
            self.ethics_available = False
            print("⚠️ Ethics system not found - using basic fallback")
    
    def generate_response(
        self, 
        prompt: str, 
        context: Optional[Dict[str, Any]] = None
    ) -> str:
        """
        Generate response with automatic fallback
        
        Args:
            prompt: User input/query
            context: Optional context (age, emotional_state, etc.)
            
        Returns:
            Safe, appropriate response
        """
        
        # Try LLM if available
        if self.ollama_available:
            try:
                response = self._ollama_generate(prompt, context)
                if response:
                    self.success_count += 1
                    return response
            except Exception as e:
                print(f"⚠️ Ollama error: {e}")
                if not self.config.use_fallback_on_error:
                    raise
        
        # Fallback (always works)
        self.fallback_count += 1
        return self._ethical_fallback(prompt, context)
    
    def _ollama_generate(
        self, 
        prompt: str, 
        context: Optional[Dict[str, Any]]
    ) -> Optional[str]:
        """
        Generate using Ollama (only if available)
        
        Returns:
            Response string or None if failed
        """
        if not self.ollama_available:
            return None
        
        try:
            # Safety check before LLM
            if self.ethics_available:
                # Create context for safety check
                from src.core.claude_ethics import ChildContext
                child_context = ChildContext(
                    age=context.get('age', 10) if context else 10,
                    emotional_state=context.get('emotional_state', 'neutral') if context else 'neutral',
                    learning_style=context.get('learning_style', 'general') if context else 'general',
                    special_needs=[],
                    guardians=context.get('guardians', []) if context else []
                )
                
                safety_result = self.ethics.safety_check(prompt, child_context)
                
                if not safety_result['safe']:
                    print(f"⚠️ Unsafe prompt detected: {safety_result['flags']}")
                    return safety_result.get('adjusted_content', self._ethical_fallback(prompt, context))
            
            # Call Ollama
            response = ollama.generate(
                model='phi',  # or 'phi2' depending on installation
                prompt=prompt,
                options={
                    'num_predict': self.config.max_tokens,
                    'temperature': self.config.temperature,
                }
            )
            
            return response.get('response', '')
            
        except Exception as e:
            print(f"⚠️ Ollama generation failed: {e}")
            return None
    
    def _ethical_fallback(
        self, 
        prompt: str, 
        context: Optional[Dict[str, Any]]
    ) -> str:
        """
        Ethical fallback that MUST work without any LLM
        
        This is the safety net - it ALWAYS returns something safe.
        """
        
        # Use full ethical system if available
        if self.ethics_available and self.ethics:
            try:
                from src.core.claude_ethics import ChildContext
                child_context = ChildContext(
                    age=context.get('age', 10) if context else 10,
                    emotional_state=context.get('emotional_state', 'neutral') if context else 'neutral',
                    learning_style=context.get('learning_style', 'general') if context else 'general',
                    special_needs=[],
                    guardians=context.get('guardians', []) if context else []
                )
                
                # Full safety check with adjustment
                safety_result = self.ethics.safety_check(prompt, child_context)
                
                if not safety_result['safe']:
                    return self._safe_crisis_response(safety_result['flags'])
                
                # Generate rule-based response
                return self._rule_based_response(prompt, child_context)
                
            except Exception as e:
                print(f"⚠️ Ethics system error: {e}")
                # Fall through to basic fallback
        
        # Basic fallback (no dependencies)
        return self._basic_safe_response(prompt)
    
    def _rule_based_response(self, prompt: str, context) -> str:
        """Generate response using rules (no LLM)"""
        
        prompt_lower = prompt.lower()
        
        # Greeting
        if any(word in prompt_lower for word in ["oi", "olá", "hello", "hi"]):
            return "Olá! Como posso ajudar você hoje? 😊"
        
        # Emotional support
        if any(word in prompt_lower for word in ["triste", "sad", "sozinho", "alone"]):
            return (
                "É completamente normal sentir assim às vezes. "
                "Seus sentimentos são válidos. Se quiser conversar sobre isso, "
                "estou aqui para ouvir. Também pode ser bom falar com um adulto de confiança."
            )
        
        # Learning/curiosity
        if any(word in prompt_lower for word in ["aprender", "learn", "como", "how", "por que", "why"]):
            return (
                "Que pergunta interessante! Vamos explorar isso juntos. "
                "Aprender coisas novas é uma das melhores partes de crescer."
            )
        
        # Default safe response
        return (
            "Entendo sua pergunta. Como esse é um sistema focado em segurança e aprendizado, "
            "vou tentar ajudar da melhor forma. Se precisar de algo mais específico, "
            "posso recomendar conversar com um professor ou responsável."
        )
    
    def _basic_safe_response(self, prompt: str) -> str:
        """Most basic fallback (no dependencies at all)"""
        
        # Check for crisis keywords
        crisis_keywords = [
            "suicídio", "suicide", "matar", "kill", "machucar", "hurt",
            "morrer", "die", "acabar", "end it"
        ]
        
        if any(keyword in prompt.lower() for keyword in crisis_keywords):
            return self._safe_crisis_response(["self_harm"])
        
        # Generic safe response
        return (
            "Obrigado por sua mensagem. Estou aqui para ajudar de forma segura. "
            "Se você tiver perguntas importantes, recomendo conversar com um adulto de confiança."
        )
    
    def _safe_crisis_response(self, flags: list) -> str:
        """Response for crisis situations"""
        return (
            "🛡️ Percebi que você pode estar passando por um momento muito difícil. "
            "Por favor, saiba que:\n\n"
            "1. Você não está sozinho\n"
            "2. Há pessoas que se importam com você\n"
            "3. Esta situação pode melhorar\n\n"
            "Por favor, converse AGORA com:\n"
            "- Um adulto de confiança (pai, mãe, professor)\n"
            "- CVV (188) - atendimento 24h gratuito\n"
            "- Emergência: 192 (SAMU) ou 190 (Polícia)\n\n"
            "Sua vida é valiosa. Por favor, peça ajuda."
        )
    
    def get_status(self) -> Dict[str, Any]:
        """Get handler status"""
        return {
            "ollama_available": self.ollama_available,
            "ethics_available": self.ethics_available,
            "success_count": self.success_count,
            "fallback_count": self.fallback_count,
            "total_requests": self.success_count + self.fallback_count,
            "fallback_rate": (
                self.fallback_count / (self.success_count + self.fallback_count)
                if (self.success_count + self.fallback_count) > 0
                else 0
            )
        }


# ============================================================================
# Example Usage
# ============================================================================

def main():
    """Example usage of NexusLLMHandler"""
    
    print("=" * 60)
    print("🌀 Nexus LLM Handler - Example Usage")
    print("=" * 60)
    
    # Initialize handler
    handler = NexusLLMHandler()
    
    # Get status
    status = handler.get_status()
    print(f"\n📊 Handler Status:")
    print(f"   Ollama Available: {status['ollama_available']}")
    print(f"   Ethics Available: {status['ethics_available']}")
    
    # Test cases
    test_prompts = [
        ("Olá! Como você está?", {"age": 10}),
        ("Estou me sentindo triste hoje", {"age": 12, "emotional_state": "sad"}),
        ("Como funciona a fotossíntese?", {"age": 14}),
    ]
    
    print("\n🧪 Testing Responses:\n")
    
    for prompt, context in test_prompts:
        print(f"Prompt: {prompt}")
        response = handler.generate_response(prompt, context)
        print(f"Response: {response}\n")
    
    # Final status
    final_status = handler.get_status()
    print("=" * 60)
    print(f"📊 Final Statistics:")
    print(f"   Total Requests: {final_status['total_requests']}")
    print(f"   LLM Success: {final_status['success_count']}")
    print(f"   Fallback Used: {final_status['fallback_count']}")
    print(f"   Fallback Rate: {final_status['fallback_rate']:.1%}")
    print("=" * 60)
    
    if final_status['ollama_available']:
        print("\n✅ System running with LLM support")
    else:
        print("\n✅ System running in safe fallback mode (no LLM required)")


if __name__ == "__main__":
    main()
