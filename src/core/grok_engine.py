#!/usr/bin/env python3
"""
🦊 Grok Engine - Loop dos 7 Por Quês
Vetor 1: Verdade radical e questionamento
"""

import re
from typing import List, Dict, Tuple

class GrokTruthEngine:
    """Engine de questionamento radical estilo Grok"""
    
    def __init__(self):
        self.question_patterns = [
            (r"por que", "question_cause"),
            (r"como funciona", "question_mechanism"),
            (r"o que é", "question_definition"),
            (r"e se", "question_hypothetical"),
            (r"realmente", "question_truth"),
            (r"prove que", "question_evidence"),
            (r"sempre é assim", "question_generalization"),
            (r"qual a fonte", "question_source"),
            (r"existe alternativa", "question_alternatives")
        ]
    
    def seven_whys_loop(self, statement: str, depth: int = 7) -> List[Dict]:
        """
        Aplica loop dos 7 porquês a uma afirmação
        
        Args:
            statement: Afirmação inicial
            depth: Profundidade do questionamento
        
        Returns:
            Lista de questões e respostas em cada nível
        """
        loop_results = []
        current_statement = statement
        
        for level in range(1, depth + 1):
            # Gerar questão para este nível
            question = self._generate_question(current_statement, level)
            
            # Tentar responder (no futuro, com modelo)
            potential_answer = self._generate_potential_answer(question, level)
            
            # Registrar
            loop_results.append({
                "level": level,
                "question": question,
                "current_belief": current_statement,
                "potential_answer": potential_answer,
                "question_type": self._classify_question(question)
            })
            
            # Atualizar statement para próximo nível
            current_statement = potential_answer
        
        return loop_results
    
    def _generate_question(self, statement: str, level: int) -> str:
        """Gera questão apropriada para o nível"""
        
        question_templates = [
            "Por que você acredita que '{}' é verdade?",
            "O que aconteceria se '{}' fosse falso?",
            "Como você sabe que '{}' é correto?",
            "Quais evidências suportam '{}'?",
            "Existe alguma exceção para '{}'?",
            "Qual a origem da ideia de que '{}'?",
            "Como '{}' se conecta com outras coisas que você sabe?"
        ]
        
        template_index = (level - 1) % len(question_templates)
        return question_templates[template_index].format(statement)
    
    def _generate_potential_answer(self, question: str, level: int) -> str:
        """Gera resposta potencial (placeholder para modelo)"""
        
        # Respostas padrão baseadas no tipo de questão
        if "por que" in question.lower():
            return "Esta é uma crença baseada em observações e experiências anteriores."
        elif "evidências" in question.lower():
            return "As evidências incluem observações diretas, dados coletados e consenso especializado."
        elif "exceção" in question.lower():
            return "Sim, existem exceções que devemos considerar para uma compreensão mais precisa."
        elif "origem" in question.lower():
            return "Esta ideia vem de uma combinação de aprendizado, experiência e reflexão."
        else:
            return "Precisamos investigar isso mais a fundo para uma resposta completa."
    
    def _classify_question(self, question: str) -> str:
        """Classifica o tipo de questão"""
        for pattern, q_type in self.question_patterns:
            if re.search(pattern, question, re.IGNORECASE):
                return q_type
        return "question_general"
    
    def analyze_statement(self, statement: str) -> Dict:
        """Análise completa de uma afirmação"""
        
        # 1. Loop dos 7 porquês
        why_loop = self.seven_whys_loop(statement)
        
        # 2. Identificar suposições
        assumptions = self._extract_assumptions(statement)
        
        # 3. Verificar consistência interna
        consistency = self._check_internal_consistency(statement)
        
        # 4. Identificar viéses potenciais
        biases = self._identify_potential_biases(statement)
        
        return {
            "original_statement": statement,
            "seven_whys_analysis": why_loop,
            "assumptions": assumptions,
            "internal_consistency": consistency,
            "potential_biases": biases,
            "truth_score": self._calculate_truth_score(why_loop, consistency),
            "recommendation": self._generate_recommendation(why_loop, biases)
        }
    
    def _extract_assumptions(self, statement: str) -> List[str]:
        """Extrai suposições implícitas"""
        assumptions = []
        
        # Padrões comuns de suposição
        assumption_patterns = [
            (r"todo(s|as)?\s+\w+", "generalização universal"),
            (r"sempre|nunca", "generalização temporal"),
            (r"obviamente|claramente", "pressuposto de clareza"),
            (r"todo mundo sabe", "pressuposto de conhecimento comum"),
            (r"naturalmente", "pressuposto de naturalidade")
        ]
        
        for pattern, desc in assumption_patterns:
            if re.search(pattern, statement, re.IGNORECASE):
                assumptions.append(desc)
        
        return assumptions
    
    def _check_internal_consistency(self, statement: str) -> Dict:
        """Verifica consistência interna"""
        # Análise simplificada
        words = statement.lower().split()
        unique_words = set(words)
        
        # Procurar contradições simples
        contradictions = []
        if "sempre" in words and "nunca" in words:
            contradictions.append("Uso de 'sempre' e 'nunca' na mesma afirmação")
        
        if "todos" in words and "alguns" in words:
            contradictions.append("Uso de 'todos' e 'alguns' na mesma afirmação")
        
        return {
            "word_count": len(words),
            "unique_words": len(unique_words),
            "contradictions_found": contradictions,
            "is_consistent": len(contradictions) == 0
        }
    
    def _identify_potential_biases(self, statement: str) -> List[str]:
        """Identifica viéses potenciais"""
        biases = []
        
        bias_patterns = [
            (r"melhor\s+\w+", "viés de superioridade"),
            (r"pior\s+\w+", "viés de inferioridade"),
            (r"só\s+\w+", "viés de exclusividade"),
            (r"nunca\s+\w+", "viés de absolutismo"),
            (r"todo\s+\w+", "viés de generalização")
        ]
        
        for pattern, bias_type in bias_patterns:
            if re.search(pattern, statement, re.IGNORECASE):
                biases.append(bias_type)
        
        return biases
    
    def _calculate_truth_score(self, why_loop: List, consistency: Dict) -> float:
        """Calcula score de verdade (0-1)"""
        # Lógica simplificada
        base_score = 0.5
        
        # Bônus por consistência
        if consistency["is_consistent"]:
            base_score += 0.2
        
        # Penalidade por muitas questões não respondidas
        unanswered = sum(1 for level in why_loop if "investigar" in level["potential_answer"].lower())
        if unanswered > 3:
            base_score -= 0.1 * (unanswered - 3)
        
        # Limitar entre 0 e 1
        return max(0.0, min(1.0, base_score))
    
    def _generate_recommendation(self, why_loop: List, biases: List[str]) -> str:
        """Gera recomendação baseada na análise"""
        if len(biases) > 0:
            return f"Recomendo questionar os seguintes viéses: {', '.join(biases)}"
        
        last_answer = why_loop[-1]["potential_answer"].lower()
        if "investigar" in last_answer or "precisamos" in last_answer:
            return "Recomendo pesquisa adicional para validar esta afirmação."
        
        return "A afirmação parece razoável, mas mantenha mente aberta para novas evidências."

# Teste rápido
if __name__ == "__main__":
    grok = GrokTruthEngine()
    
    test_statement = "Todos os gatos gostam de leite."
    
    analysis = grok.analyze_statement(test_statement)
    
    print("🦊 ANÁLISE GROK:")
    print(f"Afirmação: {analysis['original_statement']}")
    print(f"Suposições: {analysis['assumptions']}")
    print(f"Viéses: {analysis['potential_biases']}")
    print(f"Consistente: {analysis['internal_consistency']['is_consistent']}")
    print(f"Score verdade: {analysis['truth_score']:.2f}")
    print(f"Recomendação: {analysis['recommendation']}")
    
    print("\n📊 LOOP DOS 7 POR QUÊS:")
    for level in analysis['seven_whys_analysis'][:3]:  # Mostrar só 3 primeiros
        print(f"Nível {level['level']}: {level['question']}")
