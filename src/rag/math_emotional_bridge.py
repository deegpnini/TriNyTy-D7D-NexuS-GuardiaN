#!/usr/bin/env python3
"""
🧮 Math-Emotional Bridge System
Vetor 10: Lógica matemática aplicada à análise emocional
"""

import numpy as np
from typing import Dict, List, Tuple, Optional
import json
from dataclasses import dataclass
from enum import Enum
import re

class EmotionalDimension(Enum):
    """Dimensões emocionais mapeadas para espaços matemáticos"""
    VALENCE = "valence"          # Positivo/Negativo
    AROUSAL = "arousal"          # Calmo/Excitado
    DOMINANCE = "dominance"      # Submisso/No controle
    CERTAINTY = "certainty"      # Inseguro/Confiente
    COMPLEXITY = "complexity"    # Simples/Complexo

@dataclass
class EmotionalVector:
    """Vetor emocional em espaço n-dimensional"""
    valence: float          # -1 (negativo) a 1 (positivo)
    arousal: float         # -1 (calmo) a 1 (excitado)
    dominance: float       # -1 (submisso) a 1 (dominante)
    certainty: float       # 0 (incerto) a 1 (certo)
    complexity: float      # 0 (simples) a 1 (complexo)
    timestamp: str
    
    def to_array(self) -> np.ndarray:
        """Converte para array numpy"""
        return np.array([
            self.valence,
            self.arousal,
            self.dominance,
            self.certainty,
            self.complexity
        ])
    
    def to_dict(self) -> Dict:
        """Converte para dicionário"""
        return {
            "valence": self.valence,
            "arousal": self.arousal,
            "dominance": self.dominance,
            "certainty": self.certainty,
            "complexity": self.complexity,
            "timestamp": self.timestamp
        }

class MathEmotionalBridge:
    """
    Ponte entre matemática e análise emocional
    Aplica conceitos matemáticos para análise quantitativa de emoções
    """
    
    def __init__(self):
        # Dicionário emocional com pesos matemáticos
        self.emotional_lexicon = {
            # Emoções básicas com coordenadas no espaço emocional
            "alegria": EmotionalVector(
                valence=0.8, arousal=0.6, dominance=0.4, certainty=0.7, complexity=0.3,
                timestamp=""
            ),
            "tristeza": EmotionalVector(
                valence=-0.7, arousal=-0.3, dominance=-0.5, certainty=0.6, complexity=0.4,
                timestamp=""
            ),
            "raiva": EmotionalVector(
                valence=-0.6, arousal=0.8, dominance=0.7, certainty=0.8, complexity=0.5,
                timestamp=""
            ),
            "medo": EmotionalVector(
                valence=-0.5, arousal=0.7, dominance=-0.6, certainty=0.4, complexity=0.6,
                timestamp=""
            ),
            "nojo": EmotionalVector(
                valence=-0.8, arousal=0.3, dominance=0.2, certainty=0.9, complexity=0.3,
                timestamp=""
            ),
            "surpresa": EmotionalVector(
                valence=0.3, arousal=0.9, dominance=0.1, certainty=0.2, complexity=0.7,
                timestamp=""
            ),
            # Estados emocionais complexos
            "gratidão": EmotionalVector(
                valence=0.9, arousal=0.4, dominance=0.3, certainty=0.8, complexity=0.4,
                timestamp=""
            ),
            "esperança": EmotionalVector(
                valence=0.7, arousal=0.5, dominance=0.6, certainty=0.5, complexity=0.6,
                timestamp=""
            ),
            "culpa": EmotionalVector(
                valence=-0.6, arousal=0.4, dominance=-0.3, certainty=0.7, complexity=0.7,
                timestamp=""
            ),
            "vergonha": EmotionalVector(
                valence=-0.8, arousal=0.5, dominance=-0.8, certainty=0.9, complexity=0.6,
                timestamp=""
            )
        }
        
        # Matriz de transição emocional (Markov)
        self.emotional_transition_matrix = self._create_transition_matrix()
    
    def analyze_text_emotion(self, text: str) -> Dict[str, any]:
        """
        Analisa texto e retorna vetor emocional quantitativo
        
        Args:
            text: Texto para análise
        
        Returns:
            Vetor emocional e métricas
        """
        
        # Tokenização simples
        words = re.findall(r'\b\w+\b', text.lower())
        
        # Inicializar vetor acumulador
        total_vector = np.zeros(5)
        emotion_counts = {}
        found_emotions = []
        
        # Mapear palavras para emoções
        for word in words:
            for emotion, vector in self.emotional_lexicon.items():
                if emotion in word or self._is_synonym(word, emotion):
                    # Adicionar ao vetor acumulado
                    vector_array = vector.to_array()
                    total_vector += vector_array
                    
                    # Contar ocorrências
                    if emotion not in emotion_counts:
                        emotion_counts[emotion] = 0
                    emotion_counts[emotion] += 1
                    
                    found_emotions.append(emotion)
                    break
        
        # Calcular vetor médio se houver emoções encontradas
        if len(found_emotions) > 0:
            avg_vector = total_vector / len(found_emotions)
        else:
            # Vetor neutro se nenhuma emoção encontrada
            avg_vector = np.array([0.0, 0.0, 0.0, 0.5, 0.5])
        
        # Criar EmotionalVector com timestamp
        from datetime import datetime
        timestamp = datetime.now().isoformat()
        
        result_vector = EmotionalVector(
            valence=float(avg_vector[0]),
            arousal=float(avg_vector[1]),
            dominance=float(avg_vector[2]),
            certainty=float(avg_vector[3]),
            complexity=float(avg_vector[4]),
            timestamp=timestamp
        )
        
        # Calcular métricas adicionais
        metrics = self._calculate_emotional_metrics(
            result_vector, emotion_counts, found_emotions
        )
        
        # Detectar transições emocionais
        transitions = self._detect_emotional_transitions(found_emotions)
        
        # Mapear para descrição qualitativa
        qualitative = self._vector_to_qualitative(result_vector)
        
        return {
            "text": text,
            "emotional_vector": result_vector.to_dict(),
            "qualitative_analysis": qualitative,
            "detected_emotions": emotion_counts,
            "emotional_metrics": metrics,
            "transitions": transitions,
            "mathematical_analysis": self._mathematical_analysis(result_vector),
            "timestamp": timestamp
        }
    
    def _is_synonym(self, word: str, emotion: str) -> bool:
        """Verifica se palavra é sinônimo de emoção"""
        synonym_map = {
            "alegria": ["feliz", "content", "radiante", "jubiloso"],
            "tristeza": ["triste", "deprimido", "melancólico", "desolado"],
            "raiva": ["irritado", "furioso", "indignado", "bravo"],
            "medo": ["assustado", "atemorizado", "apreensivo", "receoso"],
            "nojo": ["repulsa", "aversão", "repugnância", "nojo"],
            "surpresa": ["surpreso", "espantado", "pasmo", "atônito"]
        }
        
        if emotion in synonym_map:
            return word in synonym_map[emotion]
        return False
    
    def _calculate_emotional_metrics(self, vector: EmotionalVector, 
                                   counts: Dict[str, int], 
                                   emotions: List[str]) -> Dict[str, float]:
        """Calcula métricas emocionais avançadas"""
        
        vector_array = vector.to_array()
        
        # 1. Intensidade emocional (norma do vetor)
        intensity = np.linalg.norm(vector_array)
        
        # 2. Polaridade (principalmente baseada em valence)
        polarity = vector.valence
        
        # 3. Estabilidade (variação entre dimensões)
        stability = 1.0 - np.std(vector_array)
        
        # 4. Diversidade emocional
        unique_emotions = len(set(emotions))
        total_emotions = len(emotions)
        diversity = unique_emotions / max(total_emotions, 1)
        
        # 5. Ambiguidade (baseada em certainty)
        ambiguity = 1.0 - vector.certainty
        
        return {
            "intensity": float(intensity),
            "polarity": float(polarity),
            "stability": float(stability),
            "diversity": float(diversity),
            "ambiguity": float(ambiguity),
            "complexity_score": float(vector.complexity)
        }
    
    def _detect_emotional_transitions(self, emotions: List[str]) -> List[Dict[str, any]]:
        """Detecta transições emocionais no texto"""
        
        transitions = []
        
        if len(emotions) < 2:
            return transitions
        
        for i in range(len(emotions) - 1):
            from_emotion = emotions[i]
            to_emotion = emotions[i + 1]
            
            # Calcular distância emocional
            if (from_emotion in self.emotional_lexicon and 
                to_emotion in self.emotional_lexicon):
                
                vec_from = self.emotional_lexicon[from_emotion].to_array()
                vec_to = self.emotional_lexicon[to_emotion].to_array()
                
                distance = np.linalg.norm(vec_to - vec_from)
                
                # Classificar transição
                if distance < 0.5:
                    transition_type = "smooth"
                elif distance < 1.0:
                    transition_type = "moderate"
                else:
                    transition_type = "abrupt"
                
                transitions.append({
                    "from": from_emotion,
                    "to": to_emotion,
                    "distance": float(distance),
                    "type": transition_type,
                    "position": i
                })
        
        return transitions
    
    def _vector_to_qualitative(self, vector: EmotionalVector) -> Dict[str, str]:
        """Converte vetor quantitativo em descrição qualitativa"""
        
        # Mapear dimensões para descrições
        valence_desc = self._describe_valence(vector.valence)
        arousal_desc = self._describe_arousal(vector.arousal)
        dominance_desc = self._describe_dominance(vector.dominance)
        certainty_desc = self._describe_certainty(vector.certainty)
        complexity_desc = self._describe_complexity(vector.complexity)
        
        # Dominant dimension
        dimensions = [
            (abs(vector.valence), "valência", valence_desc),
            (abs(vector.arousal), "ativação", arousal_desc),
            (abs(vector.dominance), "domínio", dominance_desc),
            (vector.certainty, "certeza", certainty_desc),
            (vector.complexity, "complexidade", complexity_desc)
        ]
        
        dominant_dim = max(dimensions, key=lambda x: x[0])
        
        # Overall emotional state
        overall = self._describe_overall_state(vector)
        
        return {
            "valence": valence_desc,
            "arousal": arousal_desc,
            "dominance": dominance_desc,
            "certainty": certainty_desc,
            "complexity": complexity_desc,
            "dominant_dimension": dominant_dim[1],
            "dominant_description": dominant_dim[2],
            "overall_state": overall
        }
    
    def _describe_valence(self, value: float) -> str:
        """Descreve dimensão valência"""
        if value > 0.6:
            return "muito positivo"
        elif value > 0.3:
            return "positivo"
        elif value > -0.3:
            return "neutro"
        elif value > -0.6:
            return "negativo"
        else:
            return "muito negativo"
    
    def _describe_arousal(self, value: float) -> str:
        """Descreve dimensão ativação"""
        if value > 0.6:
            return "muito excitado/ativo"
        elif value > 0.3:
            return "excitado/ativo"
        elif value > -0.3:
            return "neutro/calmo"
        elif value > -0.6:
            return "calmo/passivo"
        else:
            return "muito calmo/passivo"
    
    def _describe_dominance(self, value: float) -> str:
        """Descreve dimensão domínio"""
        if value > 0.6:
            return "muito dominante/no controle"
        elif value > 0.3:
            return "dominante/no controle"
        elif value > -0.3:
            return "neutro/equilibrado"
        elif value > -0.6:
            return "submisso/pouco controle"
        else:
            return "muito submisso/sem controle"
    
    def _describe_certainty(self, value: float) -> str:
        """Descreve dimensão certeza"""
        if value > 0.8:
            return "muito certo/definido"
        elif value > 0.6:
            return "certo/definido"
        elif value > 0.4:
            return "moderadamente certo"
        elif value > 0.2:
            return "incerto/ambíguo"
        else:
            return "muito incerto/confuso"
    
    def _describe_complexity(self, value: float) -> str:
        """Descreve dimensão complexidade"""
        if value > 0.8:
            return "muito complexo/nuanced"
        elif value > 0.6:
            return "complexo/detalhado"
        elif value > 0.4:
            return "moderadamente complexo"
        elif value > 0.2:
            return "simples/direto"
        else:
            return "muito simples/básico"
    
    def _describe_overall_state(self, vector: EmotionalVector) -> str:
        """Descreve estado emocional geral"""
        
        # Lógica baseada em combinações
        if vector.valence > 0.5 and vector.arousal > 0.5:
            return "Eufórico/Energético"
        elif vector.valence > 0.5 and vector.arousal < -0.5:
            return "Sereno/Contente"
        elif vector.valence < -0.5 and vector.arousal > 0.5:
            return "Angustiado/Ansioso"
        elif vector.valence < -0.5 and vector.arousal < -0.5:
            return "Deprimido/Letárgico"
        elif abs(vector.valence) < 0.3 and abs(vector.arousal) < 0.3:
            return "Neutro/Equilibrado"
        else:
            return "Misto/Complexo"
    
    def _mathematical_analysis(self, vector: EmotionalVector) -> Dict[str, any]:
        """Realiza análise matemática do vetor emocional"""
        
        vec_array = vector.to_array()
        
        # 1. Norma (intensidade total)
        norm = np.linalg.norm(vec_array)
        
        # 2. Produto escalar com vetores de referência
        reference_vectors = {
            "positive_calm": np.array([0.8, -0.8, 0.0, 0.7, 0.3]),
            "negative_excited": np.array([-0.8, 0.8, 0.0, 0.6, 0.4]),
            "neutral": np.array([0.0, 0.0, 0.0, 0.5, 0.5]),
            "complex_mixed": np.array([0.0, 0.0, 0.0, 0.5, 0.9])
        }
        
        similarities = {}
        for name, ref_vec in reference_vectors.items():
            similarity = np.dot(vec_array, ref_vec) / (
                np.linalg.norm(vec_array) * np.linalg.norm(ref_vec) + 1e-10
            )
            similarities[name] = float(similarity)
        
        # 3. Distância para cada emoção básica
        distances = {}
        for emotion, emo_vector in self.emotional_lexicon.items():
            distance = np.linalg.norm(vec_array - emo_vector.to_array())
            distances[emotion] = float(distance)
        
        # 4. Análise de cluster (simplificada)
        closest_emotions = sorted(distances.items(), key=lambda x: x[1])[:3]
        
        # 5. Espaço emocional reduzido (PCA simplificado)
        # Projeção em 2D (valência x ativação)
        projection_2d = [float(vec_array[0]), float(vec_array[1])]
        
        return {
            "vector_norm": float(norm),
            "reference_similarities": similarities,
            "closest_emotions": closest_emotions,
            "projection_2d": projection_2d,
            "dimensionality": 5,
            "coordinates": vec_array.tolist()
        }
    
    def _create_transition_matrix(self) -> np.ndarray:
        """Cria matriz de transição emocional (Markov)"""
        
        emotions = list(self.emotional_lexicon.keys())
        n = len(emotions)
        
        # Matriz de transição baseada em distâncias emocionais
        transition_matrix = np.zeros((n, n))
        
        for i, emo_i in enumerate(emotions):
            for j, emo_j in enumerate(emotions):
                if i == j:
                    # Auto-transição (tendência a permanecer)
                    transition_matrix[i, j] = 0.3
                else:
                    # Transição baseada em similaridade
                    vec_i = self.emotional_lexicon[emo_i].to_array()
                    vec_j = self.emotional_lexicon[emo_j].to_array()
                    
                    distance = np.linalg.norm(vec_j - vec_i)
                    similarity = 1.0 / (1.0 + distance)
                    
                    transition_matrix[i, j] = similarity
        
        # Normalizar linhas para soma = 1
        row_sums = transition_matrix.sum(axis=1, keepdims=True)
        transition_matrix = transition_matrix / row_sums
        
        return transition_matrix
    
    def predict_emotional_flow(self, current_emotion: str, steps: int = 3) -> List[Dict]:
        """
        Prediz fluxo emocional usando cadeias de Markov
        
        Args:
            current_emotion: Emoção atual
            steps: Número de passos para prever
        
        Returns:
            Sequência predita de emoções
        """
        
        if current_emotion not in self.emotional_lexicon:
            raise ValueError(f"Emoção {current_emotion} não reconhecida")
        
        emotions = list(self.emotional_lexicon.keys())
        current_idx = emotions.index(current_emotion)
        
        predictions = []
        
        for step in range(steps):
            # Distribuição de probabilidade atual
            if step == 0:
                probs = self.emotional_transition_matrix[current_idx]
            else:
                # Multiplicar por matriz de transição
                prev_probs = predictions[-1]["probability_vector"]
                probs = prev_probs @ self.emotional_transition_matrix
            
            # Encontrar emoção mais provável
            next_idx = np.argmax(probs)
            next_emotion = emotions[next_idx]
            probability = float(probs[next_idx])
            
            predictions.append({
                "step": step + 1,
                "predicted_emotion": next_emotion,
                "probability": probability,
                "probability_vector": probs.tolist(),
                "emotional_vector": self.emotional_lexicon[next_emotion].to_dict()
            })
        
        return predictions

# Teste rápido
if __name__ == "__main__":
    print("🧮 Testando Math-Emotional Bridge...")
    
    bridge = MathEmotionalBridge()
    
    test_text = "Estou muito feliz com essa notícia incrível! Mas também um pouco preocupado com o futuro."
    
    analysis = bridge.analyze_text_emotion(test_text)
    
    print(f"\n📝 Texto analisado: {test_text}")
    print(f"\n📊 Vetor Emocional:")
    vec = analysis["emotional_vector"]
    print(f"  Valência: {vec['valence']:.2f} ({analysis['qualitative_analysis']['valence']})")
    print(f"  Ativação: {vec['arousal']:.2f} ({analysis['qualitative_analysis']['arousal']})")
    print(f"  Domínio: {vec['dominance']:.2f} ({analysis['qualitative_analysis']['dominance']})")
    print(f"  Certeza: {vec['certainty']:.2f} ({analysis['qualitative_analysis']['certainty']})")
    print(f"  Complexidade: {vec['complexity']:.2f} ({analysis['qualitative_analysis']['complexity']})")
    
    print(f"\n🎯 Estado geral: {analysis['qualitative_analysis']['overall_state']}")
    
    print(f"\n📈 Métricas emocionais:")
    metrics = analysis["emotional_metrics"]
    print(f"  Intensidade: {metrics['intensity']:.2f}")
    print(f"  Polaridade: {metrics['polarity']:.2f}")
    print(f"  Estabilidade: {metrics['stability']:.2f}")
    print(f"  Diversidade: {metrics['diversity']:.2f}")
    
    print(f"\n🔄 Transições detectadas:")
    for trans in analysis["transitions"][:2]:  # Mostrar só 2
        print(f"  {trans['from']} → {trans['to']} ({trans['type']})")
    
    print(f"\n🔢 Análise matemática:")
    math = analysis["mathematical_analysis"]
    print(f"  Norma do vetor: {math['vector_norm']:.2f}")
    print(f"  Emoções mais próximas: {', '.join([e[0] for e in math['closest_emotions'][:2]])}")
