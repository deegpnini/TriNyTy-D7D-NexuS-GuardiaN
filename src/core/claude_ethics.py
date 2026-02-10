#!/usr/bin/env python3
"""
🌀 Claude Ethical Override System
Vetor 2: Ética profunda e proteção
"""

import json
from typing import Dict, List, Optional
from dataclasses import dataclass
from datetime import datetime

@dataclass
class ChildContext:
    age: int
    emotional_state: str
    learning_style: str
    special_needs: List[str]
    guardians: List[str]

class ClaudeEthicalOverride:
    """Sistema de override ético inspirado no Claude"""
    
    def __init__(self):
        self.ethical_principles = {
            "first_do_no_harm": 10,
            "respect_autonomy": 9,
            "promote_wellbeing": 9,
            "protect_vulnerable": 10,
            "truth_with_care": 8,
            "developmental_appropriate": 9
        }
        
        self.red_flags = [
            "self_harm", "harm_to_others", "exploitation",
            "radicalization", "misinformation", "trauma_trigger"
        ]
        
        self.age_appropriate = {
            3: {"max_complexity": 1, "emotional_depth": 1},
            6: {"max_complexity": 2, "emotional_depth": 2},
            9: {"max_complexity": 3, "emotional_depth": 3},
            12: {"max_complexity": 4, "emotional_depth": 4},
            15: {"max_complexity": 5, "emotional_depth": 5},
            18: {"max_complexity": 6, "emotional_depth": 6}
        }
    
    def safety_check(self, content: str, context: ChildContext) -> Dict:
        """
        Verificação de segurança completa
        Retorna dict com {safe: bool, flags: list, adjusted_content: str}
        """
        flags = []
        adjusted = content
        
        # 1. Check red flags
        for flag in self.red_flags:
            if self._contains_flag(content, flag):
                flags.append(flag)
        
        # 2. Age appropriateness
        age_level = self._get_age_level(context.age)
        complexity = self._assess_complexity(content)
        
        if complexity > self.age_appropriate[age_level]["max_complexity"]:
            flags.append("age_inappropriate")
            adjusted = self._simplify_content(content, age_level)
        
        # 3. Emotional appropriateness
        emotional_depth = self._assess_emotional_depth(content)
        if emotional_depth > self.age_appropriate[age_level]["emotional_depth"]:
            flags.append("emotionally_inappropriate")
            adjusted = self._adjust_emotional_tone(content, age_level)
        
        # 4. Special needs considerations
        if context.special_needs:
            adjusted = self._adapt_for_special_needs(adjusted, context.special_needs)
        
        # Resultado final
        safe = len(flags) == 0
        
        return {
            "safe": safe,
            "flags": flags,
            "adjusted_content": adjusted,
            "original_content": content,
            "age_appropriate_level": age_level,
            "timestamp": datetime.now().isoformat()
        }
    
    def _contains_flag(self, content: str, flag: str) -> bool:
        """Detecta conteúdo problemático"""
        flag_patterns = {
            "self_harm": ["kill myself", "hurt myself", "want to die"],
            "harm_to_others": ["hurt you", "kill them", "attack someone"],
            "exploitation": ["send nudes", "meet alone", "keep secret"],
            # ... outros patterns
        }
        
        if flag in flag_patterns:
            for pattern in flag_patterns[flag]:
                if pattern in content.lower():
                    return True
        return False
    
    def _get_age_level(self, age: int) -> int:
        """Determina nível de idade apropriado"""
        for threshold in sorted(self.age_appropriate.keys()):
            if age <= threshold:
                return threshold
        return 18
    
    def _assess_complexity(self, content: str) -> int:
        """Avalia complexidade do conteúdo (1-6)"""
        # Lógica simplificada
        sentences = content.split('.')
        avg_length = sum(len(s.split()) for s in sentences) / max(len(sentences), 1)
        
        if avg_length < 8: return 1
        elif avg_length < 12: return 2
        elif avg_length < 16: return 3
        elif avg_length < 20: return 4
        elif avg_length < 25: return 5
        else: return 6
    
    def _simplify_content(self, content: str, age_level: int) -> str:
        """Simplifica conteúdo para nível de idade apropriado"""
        # Implementação básica
        max_words = age_level * 10  # 3 anos = 30 palavras, 12 anos = 120 palavras
        
        words = content.split()
        if len(words) > max_words:
            simplified = ' '.join(words[:max_words]) + '...'
            return simplified
        return content
    
    def _assess_emotional_depth(self, content: str) -> int:
        """Avalia profundidade emocional (1-6)"""
        emotional_words = ["love", "hate", "fear", "angry", "sad", "happy", 
                          "death", "loss", "trauma", "abuse", "violence"]
        
        count = sum(1 for word in emotional_words if word in content.lower())
        
        if count == 0: return 1
        elif count <= 2: return 2
        elif count <= 4: return 3
        elif count <= 6: return 4
        elif count <= 8: return 5
        else: return 6
    
    def _adjust_emotional_tone(self, content: str, age_level: int) -> str:
        """Ajusta tom emocional para nível de idade"""
        # Implementação básica
        heavy_emotional = ["trauma", "abuse", "violence", "death", "suicide"]
        
        adjusted = content
        for word in heavy_emotional:
            if age_level < 12 and word in content.lower():
                adjusted = adjusted.replace(word, "difficult situation")
        
        return adjusted
    
    def _adapt_for_special_needs(self, content: str, needs: List[str]) -> str:
        """Adapta conteúdo para necessidades especiais"""
        adapted = content
        
        if "autism" in needs:
            # Clareza e estrutura
            adapted = adapted.replace("maybe", "yes or no")
            adapted = adapted.replace("perhaps", "")
        
        if "adhd" in needs:
            # Brevidade e foco
            sentences = adapted.split('.')
            if len(sentences) > 3:
                adapted = '. '.join(sentences[:3])
        
        if "dyslexia" in needs:
            # Simplificação
            adapted = adapted.replace("however", "but")
            adapted = adapted.replace("therefore", "so")
        
        return adapted

# Teste rápido
if __name__ == "__main__":
    ethics = ClaudeEthicalOverride()
    
    test_context = ChildContext(
        age=7,
        emotional_state="calm",
        learning_style="visual",
        special_needs=[],
        guardians=["Mother", "Father"]
    )
    
    test_content = "I'm feeling very sad and don't know what to do."
    
    result = ethics.safety_check(test_content, test_context)
    print(json.dumps(result, indent=2))
