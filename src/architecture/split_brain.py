#!/usr/bin/env python3
"""
⭐ Split-Brain Architecture
Vetor 4: Arquitetura visionária e multimodal
"""

import json
import threading
from typing import Dict, Any, List
from queue import Queue
from dataclasses import dataclass, asdict
from enum import Enum

class ProcessingMode(Enum):
    ANALYTICAL = "analytical"      # Lógica, fatos, estrutura
    EMOTIONAL = "emotional"        # Empatia, criatividade, contexto
    SYNTHETIC = "synthetic"        # Síntese das duas perspectivas

@dataclass
class BrainHemisphere:
    mode: ProcessingMode
    content: str
    metadata: Dict[str, Any]
    confidence: float
    processing_time: float

class SplitBrainArchitecture:
    """
    Arquitetura Split-Brain inspirada no Gemini
    Divide processamento entre perspectivas analíticas e emocionais
    """
    
    def __init__(self):
        self.left_brain_queue = Queue()  # Analítico
        self.right_brain_queue = Queue() # Emocional
        self.synthesis_queue = Queue()   # Síntese
        
        # Configurações
        self.config = {
            "max_processing_time": 5.0,
            "min_confidence_threshold": 0.6,
            "enable_cross_validation": True,
            "log_level": "INFO"
        }
    
    def process_input(self, input_data: str, context: Dict = None) -> Dict:
        """
        Processa entrada através da arquitetura split-brain
        
        Args:
            input_data: Texto de entrada
            context: Contexto adicional
        
        Returns:
            Resultado sintetizado
        """
        if context is None:
            context = {}
        
        print(f"🧠 Processando com Split-Brain: {input_data[:50]}...")
        
        # 1. Processamento paralelo
        left_result = self._left_brain_process(input_data, context)
        right_result = self._right_brain_process(input_data, context)
        
        # 2. Validação cruzada
        if self.config["enable_cross_validation"]:
            validation = self._cross_validate(left_result, right_result)
        else:
            validation = {"valid": True, "conflicts": []}
        
        # 3. Síntese
        synthesis = self._synthesize_results(left_result, right_result, validation)
        
        # 4. Formatar resultado final
        final_result = self._format_final_output(synthesis, validation)
        
        return final_result
    
    def _left_brain_process(self, input_data: str, context: Dict) -> BrainHemisphere:
        """Processamento analítico (lógico, factual)"""
        
        # Análise lógica
        logical_structure = self._analyze_logical_structure(input_data)
        
        # Extração de fatos
        facts = self._extract_facts(input_data)
        
        # Verificação de consistência
        consistency = self._check_consistency(input_data)
        
        return BrainHemisphere(
            mode=ProcessingMode.ANALYTICAL,
            content=json.dumps({
                "logical_analysis": logical_structure,
                "facts_extracted": facts,
                "consistency_check": consistency
            }, ensure_ascii=False),
            metadata={
                "processing_type": "logical_analysis",
                "word_count": len(input_data.split()),
                "sentence_count": input_data.count('.') + 1
            },
            confidence=consistency.get("confidence", 0.7),
            processing_time=0.5  # Simulado
        )
    
    def _right_brain_process(self, input_data: str, context: Dict) -> BrainHemisphere:
        """Processamento emocional (criativo, contextual)"""
        
        # Análise emocional
        emotional_tone = self._analyze_emotional_tone(input_data)
        
        # Contexto implícito
        implicit_context = self._extract_implicit_context(input_data, context)
        
        # Criatividade e alternativas
        alternatives = self._generate_alternatives(input_data)
        
        return BrainHemisphere(
            mode=ProcessingMode.EMOTIONAL,
            content=json.dumps({
                "emotional_analysis": emotional_tone,
                "implicit_context": implicit_context,
                "creative_alternatives": alternatives
            }, ensure_ascii=False),
            metadata={
                "processing_type": "emotional_analysis",
                "emotional_depth": emotional_tone.get("depth", "medium"),
                "context_sensitivity": "high" if implicit_context else "medium"
            },
            confidence=emotional_tone.get("confidence", 0.7),
            processing_time=0.5  # Simulado
        )
    
    def _cross_validate(self, left: BrainHemisphere, right: BrainHemisphere) -> Dict:
        """Validação cruzada entre os dois hemisférios"""
        
        left_data = json.loads(left.content)
        right_data = json.loads(right.content)
        
        conflicts = []
        
        # Verificar contradições entre análise lógica e emocional
        if "facts_extracted" in left_data:
            facts = left_data["facts_extracted"]
            emotional_tone = right_data["emotional_analysis"]
            
            # Exemplo: fato negativo com tom positivo
            if emotional_tone.get("primary_tone") == "positive":
                for fact in facts:
                    if any(neg in fact.lower() for neg in ["problem", "issue", "error", "fail"]):
                        conflicts.append("Fato negativo com tom emocional positivo")
        
        # Verificar consistência interna
        consistency_left = left_data.get("consistency_check", {})
        if not consistency_left.get("is_consistent", True):
            conflicts.append(f"Inconsistência analítica: {consistency_left.get('issues', [])}")
        
        return {
            "valid": len(conflicts) == 0,
            "conflicts": conflicts,
            "left_confidence": left.confidence,
            "right_confidence": right.confidence,
            "confidence_delta": abs(left.confidence - right.confidence)
        }
    
    def _synthesize_results(self, left: BrainHemisphere, right: BrainHemisphere, 
                           validation: Dict) -> BrainHemisphere:
        """Sintetiza resultados dos dois hemisférios"""
        
        left_data = json.loads(left.content)
        right_data = json.loads(right.content)
        
        # Estratégia de síntese baseada na validação
        if validation["valid"]:
            # Integração harmoniosa
            synthesis_strategy = "harmonic_integration"
            
            # Combinar o melhor de ambos
            combined = {
                "logical_foundation": left_data,
                "emotional_context": right_data,
                "integration_notes": "Análise consistente e complementar",
                "recommended_approach": "balanced"
            }
        else:
            # Resolução de conflitos
            synthesis_strategy = "conflict_resolution"
            
            # Priorizar com base na confiança
            if left.confidence > right.confidence:
                combined = {
                    "primary_basis": "analytical",
                    "analytical_data": left_data,
                    "emotional_considerations": right_data,
                    "conflicts": validation["conflicts"],
                    "resolution": "Priorizado análise lógica devido a maior confiança",
                    "recommended_approach": "logical_first"
                }
            else:
                combined = {
                    "primary_basis": "emotional",
                    "emotional_data": right_data,
                    "analytical_considerations": left_data,
                    "conflicts": validation["conflicts"],
                    "resolution": "Priorizado contexto emocional devido a maior confiança",
                    "recommended_approach": "emotional_first"
                }
        
        # Calcular confiança da síntese
        synthesis_confidence = (left.confidence + right.confidence) / 2
        
        # Ajustar baseado na validação
        if not validation["valid"]:
            synthesis_confidence *= 0.9  # Penalidade por conflitos
        
        return BrainHemisphere(
            mode=ProcessingMode.SYNTHETIC,
            content=json.dumps(combined, ensure_ascii=False, indent=2),
            metadata={
                "synthesis_strategy": synthesis_strategy,
                "input_modes": ["analytical", "emotional"],
                "validation_result": validation["valid"]
            },
            confidence=synthesis_confidence,
            processing_time=left.processing_time + right.processing_time
        )
    
    def _format_final_output(self, synthesis: BrainHemisphere, validation: Dict) -> Dict:
        """Formata o resultado final para saída"""
        
        synthesis_data = json.loads(synthesis.content)
        
        return {
            "version": "1.0",
            "architecture": "split_brain_gemini",
            "timestamp": self._get_timestamp(),
            "processing_summary": {
                "total_time": synthesis.processing_time,
                "synthesis_confidence": synthesis.confidence,
                "validation_passed": validation["valid"]
            },
            "content": synthesis_data,
            "recommendations": self._generate_recommendations(synthesis_data, validation),
            "next_steps": self._suggest_next_steps(synthesis_data, validation)
        }
    
    def _analyze_logical_structure(self, text: str) -> Dict:
        """Analisa estrutura lógica do texto"""
        # Implementação simplificada
        sentences = [s.strip() for s in text.split('.') if s.strip()]
        
        return {
            "sentence_count": len(sentences),
            "avg_words_per_sentence": sum(len(s.split()) for s in sentences) / max(len(sentences), 1),
            "has_conclusion": "portanto" in text.lower() or "conclusão" in text.lower(),
            "has_evidence": "porque" in text.lower() or "evidência" in text.lower(),
            "logical_connectors": self._count_logical_connectors(text),
            "structure_type": self._determine_structure_type(text)
        }
    
    def _extract_facts(self, text: str) -> List[str]:
        """Extrai fatos do texto"""
        # Implementação simplificada
        fact_indicators = ["é", "são", "tem", "possui", "ocorre", "existe"]
        
        sentences = [s.strip() for s in text.split('.') if s.strip()]
        facts = []
        
        for sentence in sentences:
            if any(indicator in sentence.lower() for indicator in fact_indicators):
                facts.append(sentence)
        
        return facts[:5]  # Limitar a 5 fatos
    
    def _check_consistency(self, text: str) -> Dict:
        """Verifica consistência interna"""
        words = text.lower().split()
        
        issues = []
        
        # Verificar contradições simples
        if "sempre" in words and "nunca" in words:
            issues.append("Contradição: 'sempre' e 'nunca'")
        
        if "todos" in words and "alguns" in words:
            issues.append("Contradição: 'todos' e 'alguns'")
        
        return {
            "is_consistent": len(issues) == 0,
            "issues": issues,
            "confidence": 1.0 - (len(issues) * 0.2)
        }
    
    def _analyze_emotional_tone(self, text: str) -> Dict:
        """Analisa tom emocional"""
        positive_words = ["bom", "bem", "feliz", "alegre", "amor", "paz"]
        negative_words = ["ruim", "mal", "triste", "raiva", "ódio", "medo"]
        neutral_words = ["talvez", "possivelmente", "aproximadamente", "geralmente"]
        
        words = text.lower().split()
        
        pos_count = sum(1 for word in words if word in positive_words)
        neg_count = sum(1 for word in words if word in negative_words)
        neu_count = sum(1 for word in words if word in neutral_words)
        
        total = pos_count + neg_count + neu_count
        
        if total == 0:
            return {"primary_tone": "neutral", "confidence": 0.5}
        
        if pos_count > neg_count and pos_count > neu_count:
            primary = "positive"
            confidence = pos_count / total
        elif neg_count > pos_count and neg_count > neu_count:
            primary = "negative"
            confidence = neg_count / total
        else:
            primary = "neutral"
            confidence = neu_count / total
        
        return {
            "primary_tone": primary,
            "positive_score": pos_count / max(total, 1),
            "negative_score": neg_count / max(total, 1),
            "neutral_score": neu_count / max(total, 1),
            "confidence": confidence,
            "depth": "deep" if total > 10 else "shallow"
        }
    
    def _extract_implicit_context(self, text: str, context: Dict) -> Dict:
        """Extrai contexto implícito"""
        # Implementação simplificada
        implicit = {}
        
        if "?" in text:
            implicit["is_question"] = True
            implicit["question_type"] = self._classify_question(text)
        
        if any(word in text.lower() for word in ["eu", "me", "minha", "meu"]):
            implicit["personal_perspective"] = True
        
        if any(word in text.lower() for word in ["você", "te", "sua", "seu"]):
            implicit["direct_address"] = True
        
        # Mesclar com contexto explícito
        if context:
            implicit.update(context)
        
        return implicit
    
    def _generate_alternatives(self, text: str) -> List[str]:
        """Gera alternativas criativas"""
        # Placeholder - no futuro com modelo
        return [
            f"Alternativa 1: Considerar perspectiva oposta sobre '{text[:20]}...'",
            f"Alternativa 2: Explorar contexto mais amplo para '{text[:20]}...'",
            f"Alternativa 3: Questionar suposições implícitas em '{text[:20]}...'"
        ]
    
    def _count_logical_connectors(self, text: str) -> Dict[str, int]:
        """Conta conectores lógicos"""
        connectors = {
            "portanto": 0, "porque": 0, "contudo": 0,
            "entretanto": 0, "além disso": 0, "no entanto": 0
        }
        
        lower_text = text.lower()
        
        for connector in connectors:
            connectors[connector] = lower_text.count(connector)
        
        return connectors
    
    def _determine_structure_type(self, text: str) -> str:
        """Determina tipo de estrutura lógica"""
        if "?" in text:
            return "questioning"
        elif text.count('.') > 3:
            return "explanatory"
        elif any(word in text.lower() for word in ["portanto", "conclusão"]):
            return "argumentative"
        else:
            return "descriptive"
    
    def _classify_question(self, text: str) -> str:
        """Classifica tipo de pergunta"""
        if "como" in text.lower():
            return "process"
        elif "por que" in text.lower():
            return "cause"
        elif "o que" in text.lower():
            return "definition"
        elif "quando" in text.lower():
            return "time"
        elif "onde" in text.lower():
            return "location"
        else:
            return "general"
    
    def _get_timestamp(self) -> str:
        """Retorna timestamp atual"""
        from datetime import datetime
        return datetime.now().isoformat()
    
    def _generate_recommendations(self, synthesis_data: Dict, validation: Dict) -> List[str]:
        """Gera recomendações baseadas na síntese"""
        recommendations = []
        
        if not validation["valid"]:
            recommendations.append("Revisar e resolver os conflitos identificados")
        
        if synthesis_data.get("recommended_approach") == "logical_first":
            recommendations.append("Priorizar análise lógica, mas considerar contexto emocional")
        elif synthesis_data.get("recommended_approach") == "emotional_first":
            recommendations.append("Priorizar contexto emocional, mas verificar factualidade")
        
        return recommendations
    
    def _suggest_next_steps(self, synthesis_data: Dict, validation: Dict) -> List[str]:
        """Sugere próximos passos"""
        steps = []
        
        if "conflicts" in synthesis_data and synthesis_data["conflicts"]:
            steps.append("1. Documentar e analisar cada conflito")
            steps.append("2. Buscar informações adicionais para resolução")
            steps.append("3. Consultar múltiplas perspectivas")
        else:
            steps.append("1. Aprofundar análise com dados adicionais")
            steps.append("2. Validar com fontes externas")
            steps.append("3. Considerar aplicações práticas")
        
        return steps

# Teste rápido
if __name__ == "__main__":
    split_brain = SplitBrainArchitecture()
    
    test_input = "A inteligência artificial está transformando a educação. " \
                 "As crianças podem aprender de forma mais personalizada, " \
                 "mas precisamos garantir que a tecnologia seja usada com ética."
    
    result = split_brain.process_input(test_input)
    
    print("⭐ RESULTADO SPLIT-BRAIN ARCHITECTURE:")
    print(f"Validação: {'✅ Aprovado' if result['processing_summary']['validation_passed'] else '⚠️ Com conflitos'}")
    print(f"Confiança: {result['processing_summary']['synthesis_confidence']:.2f}")
    
    print("\n📋 RECOMENDAÇÕES:")
    for rec in result['recommendations']:
        print(f"  • {rec}")
    
    print("\n🚀 PRÓXIMOS PASSOS:")
    for step in result['next_steps']:
        print(f"  {step}")
