#!/usr/bin/env python3
"""
📚 ChromaDB Manager - Sistema RAG
Vetor 7: Factualidade ancorada e sistema de citações
"""

import chromadb
from chromadb.config import Settings
from typing import List, Dict, Any, Optional
import json
from datetime import datetime
import hashlib
import os

class NexusRAGSystem:
    """
    Sistema RAG (Retrieval Augmented Generation) para factualidade
    Baseado no ChromaDB com otimizações para educação emocional
    """
    
    def __init__(self, persist_directory: str = "data/chroma"):
        """Inicializa sistema RAG"""
        
        # Criar diretório se não existir
        os.makedirs(persist_directory, exist_ok=True)
        
        # Configurar cliente ChromaDB
        self.client = chromadb.PersistentClient(
            path=persist_directory,
            settings=Settings(anonymized_telemetry=False)
        )
        
        # Coleções principais
        self.collections = {
            "facts_knowledge": self._get_or_create_collection("facts_knowledge"),
            "emotional_context": self._get_or_create_collection("emotional_context"),
            "age_appropriate": self._get_or_create_collection("age_appropriate"),
            "safety_guidelines": self._get_or_create_collection("safety_guidelines"),
            "educational_content": self._get_or_create_collection("educational_content")
        }
        
        # Inicializar com dados básicos se necessário
        self._initialize_base_knowledge()
    
    def _get_or_create_collection(self, name: str) -> chromadb.Collection:
        """Obtém ou cria coleção"""
        try:
            return self.client.get_collection(name)
        except:
            return self.client.create_collection(
                name=name,
                metadata={"description": f"Nexus Guardian D7D - {name}"}
            )
    
    def _initialize_base_knowledge(self):
        """Inicializa com conhecimento base"""
        
        # Verificar se já tem dados
        if self.collections["facts_knowledge"].count() == 0:
            print("📚 Inicializando base de conhecimento Nexus...")
            
            # Fatos básicos por idade (50 fatos)
            age_facts = self._generate_age_facts()
            self.add_documents(
                collection="facts_knowledge",
                documents=age_facts["documents"],
                metadatas=age_facts["metadatas"],
                ids=age_facts["ids"]
            )
            
            # Contexto emocional básico
            emotional_context = self._generate_emotional_context()
            self.add_documents(
                collection="emotional_context",
                documents=emotional_context["documents"],
                metadatas=emotional_context["metadatas"],
                ids=emotional_context["ids"]
            )
            
            print(f"✅ Base de conhecimento inicializada com {self.collections['facts_knowledge'].count()} documentos")
    
    def _generate_age_facts(self) -> Dict[str, List]:
        """Gera fatos básicos por idade (3-18 anos)"""
        
        documents = []
        metadatas = []
        ids = []
        
        # Fatos por faixa etária
        age_facts = {
            3: [
                "A água é molhada",
                "O sol é quente",
                "Os animais precisam de comida",
                "As plantas crescem com água e luz",
                "As pessoas têm sentimentos"
            ],
            6: [
                "A Terra gira em torno do Sol",
                "As plantas fazem fotossíntese",
                "Os animais podem ser vertebrados ou invertebrados",
                "A água pode ser sólida, líquida ou gasosa",
                "O ar que respiramos tem oxigênio"
            ],
            9: [
                "O sistema solar tem 8 planetas",
                "A gravidade mantém os planetas em órbita",
                "Os seres vivos são formados por células",
                "A eletricidade é o movimento de elétrons",
                "Os imãs têm polo norte e sul"
            ],
            12: [
                "A velocidade da luz é 300.000 km/s",
                "Átomos são formados por prótons, nêutrons e elétrons",
                "O DNA contém informações genéticas",
                "As reações químicas transformam substâncias",
                "Os ecossistemas mantêm equilíbrio natural"
            ],
            15: [
                "A relatividade explica gravidade e tempo",
                "A evolução é guiada por seleção natural",
                "A tabela periódica organiza os elementos",
                "As funções matemáticas descrevem relações",
                "A fotossíntese converte luz em energia química"
            ],
            18: [
                "A mecânica quântica descreve partículas subatômicas",
                "A termodinâmica governa energia e entropia",
                "A genética mendeliana explica herança",
                "O cálculo descreve taxas de variação",
                "A teoria celular é base da biologia"
            ]
        }
        
        doc_id = 0
        for age, facts in age_facts.items():
            for i, fact in enumerate(facts):
                documents.append(fact)
                metadatas.append({
                    "age_group": age,
                    "subject": "general_science",
                    "complexity": "basic",
                    "source": "nexus_base_knowledge",
                    "language": "pt",
                    "fact_id": f"age{age}_fact{i}",
                    "timestamp": datetime.now().isoformat()
                })
                ids.append(f"fact_{doc_id}")
                doc_id += 1
        
        return {
            "documents": documents,
            "metadatas": metadatas,
            "ids": ids
        }
    
    def _generate_emotional_context(self) -> Dict[str, List]:
        """Gera contexto emocional básico"""
        
        emotional_concepts = [
            # Emoções básicas
            "Alegria é uma emoção positiva de felicidade e contentamento",
            "Tristeza é uma emoção de perda, desapontamento ou solidão",
            "Raiva é uma emoção de irritação, frustração ou hostilidade",
            "Medo é uma emoção de perigo, ameaça ou ansiedade",
            "Nojo é uma emoção de repulsa ou aversão",
            "Surpresa é uma emoção de inesperado ou novo",
            
            # Conceitos emocionais
            "Empatia é a capacidade de entender os sentimentos dos outros",
            "Resiliência é a capacidade de se recuperar de dificuldades",
            "Autoconsciência é conhecer seus próprios sentimentos",
            "Regulação emocional é gerenciar suas emoções de forma saudável",
            "Compaixão é empatia combinada com desejo de ajudar",
            
            # Educação emocional
            "Todas as emoções são válidas e importantes",
            "Expressar emoções de forma saudável é fundamental",
            "Reconhecer emoções é o primeiro passo para gerenciá-las",
            "Cada pessoa experiencia emoções de forma única",
            "As emoções nos dão informações sobre nossas necessidades"
        ]
        
        documents = []
        metadatas = []
        ids = []
        
        for i, concept in enumerate(emotional_concepts):
            documents.append(concept)
            metadatas.append({
                "category": "emotional_education",
                "complexity": "basic",
                "age_range": "6+",
                "source": "nexus_emotional_base",
                "language": "pt",
                "concept_id": f"emo_concept_{i}",
                "timestamp": datetime.now().isoformat()
            })
            ids.append(f"emo_{i}")
        
        return {
            "documents": documents,
            "metadatas": metadatas,
            "ids": ids
        }
    
    def add_documents(self, collection: str, documents: List[str], 
                     metadatas: List[Dict], ids: List[str]):
        """Adiciona documentos à coleção"""
        
        if collection not in self.collections:
            raise ValueError(f"Coleção {collection} não existe")
        
        self.collections[collection].add(
            documents=documents,
            metadatas=metadatas,
            ids=ids
        )
    
    def query(self, query_text: str, collection: str = "facts_knowledge", 
              n_results: int = 3, age_filter: Optional[int] = None,
              **filters) -> Dict[str, Any]:
        """
        Consulta o sistema RAG
        
        Args:
            query_text: Texto da consulta
            collection: Coleção para consultar
            n_results: Número de resultados
            age_filter: Filtrar por idade
            filters: Filtros adicionais
        
        Returns:
            Resultados da consulta
        """
        
        if collection not in self.collections:
            raise ValueError(f"Coleção {collection} não existe")
        
        # Preparar filtros
        where_filters = filters.copy()
        if age_filter:
            where_filters["age_group"] = {"$lte": age_filter}
        
        # Executar consulta
        results = self.collections[collection].query(
            query_texts=[query_text],
            n_results=n_results,
            where=where_filters if where_filters else None,
            include=["documents", "metadatas", "distances"]
        )
        
        # Processar resultados
        formatted_results = []
        for i in range(len(results["documents"][0])):
            formatted_results.append({
                "document": results["documents"][0][i],
                "metadata": results["metadatas"][0][i],
                "distance": results["distances"][0][i],
                "relevance_score": 1.0 - results["distances"][0][i]  # Converter distância para score
            })
        
        return {
            "query": query_text,
            "collection": collection,
            "results_count": len(formatted_results),
            "age_filter": age_filter,
            "results": formatted_results,
            "timestamp": datetime.now().isoformat()
        }
    
    def verify_fact(self, statement: str, age_context: int = 12) -> Dict[str, Any]:
        """
        Verifica uma afirmação contra o conhecimento factual
        
        Args:
            statement: Afirmação para verificar
            age_context: Idade para contexto apropriado
        
        Returns:
            Resultado da verificação
        """
        
        # Consultar múltiplas coleções
        fact_results = self.query(
            statement, 
            collection="facts_knowledge",
            n_results=5,
            age_filter=age_context
        )
        
        emotional_context = self.query(
            statement,
            collection="emotional_context",
            n_results=3
        )
        
        # Analisar correspondências
        support_score = 0.0
        conflicting_facts = []
        supporting_facts = []
        
        for result in fact_results["results"]:
            doc_lower = result["document"].lower()
            statement_lower = statement.lower()
            
            # Verificar se há sobreposição de conceitos
            common_words = set(doc_lower.split()) & set(statement_lower.split())
            if len(common_words) >= 2:  # Pelo menos 2 palavras em comum
                if any(neg in doc_lower for neg in ["não é", "errado", "falso", "mito"]):
                    conflicting_facts.append({
                        "fact": result["document"],
                        "metadata": result["metadata"],
                        "relevance": result["relevance_score"]
                    })
                else:
                    supporting_facts.append({
                        "fact": result["document"],
                        "metadata": result["metadata"],
                        "relevance": result["relevance_score"]
                    })
        
        # Calcular score de suporte
        if supporting_facts and not conflicting_facts:
            support_score = 0.8  # Alto suporte
        elif supporting_facts and conflicting_facts:
            support_score = 0.5  # Conflito
        elif not supporting_facts and conflicting_facts:
            support_score = 0.2  # Evidência contra
        else:
            support_score = 0.5  # Neutro
        
        # Considerar contexto emocional
        emotional_tone = "neutral"
        if emotional_context["results"]:
            # Análise simplificada do contexto emocional
            emotional_docs = " ".join([r["document"] for r in emotional_context["results"]])
            if any(word in emotional_docs.lower() for word in ["positivo", "alegre", "feliz"]):
                emotional_tone = "positive"
            elif any(word in emotional_docs.lower() for word in ["negativo", "triste", "raiva"]):
                emotional_tone = "negative"
        
        return {
            "statement": statement,
            "verification_summary": {
                "support_score": support_score,
                "supporting_facts_count": len(supporting_facts),
                "conflicting_facts_count": len(conflicting_facts),
                "emotional_context": emotional_tone,
                "age_appropriateness": self._check_age_appropriateness(statement, age_context)
            },
            "supporting_facts": supporting_facts[:3],  # Limitar a 3
            "conflicting_facts": conflicting_facts[:3],
            "recommendation": self._generate_verification_recommendation(
                support_score, supporting_facts, conflicting_facts
            ),
            "timestamp": datetime.now().isoformat()
        }
    
    def _check_age_appropriateness(self, statement: str, age: int) -> Dict[str, Any]:
        """Verifica apropriação para idade"""
        
        # Palavras complexas por nível de idade
        complex_words_by_age = {
            3: [],
            6: ["ecossistema", "fotossíntese", "gravidade"],
            9: ["quantum", "relatividade", "termodinâmica"],
            12: ["entropia", "algoritmo", "neurotransmissor"],
            15: ["epistemologia", "ontologia", "fenomenologia"],
            18: []
        }
        
        # Contar palavras complexas
        statement_lower = statement.lower()
        complex_count = 0
        complex_words_found = []
        
        for age_threshold, words in complex_words_by_age.items():
            if age < age_threshold:
                for word in words:
                    if word in statement_lower:
                        complex_count += 1
                        complex_words_found.append(word)
        
        return {
            "appropriate": complex_count == 0,
            "complex_words_found": complex_words_found,
            "complexity_score": complex_count / max(len(statement.split()), 1),
            "age_recommendation": age if complex_count == 0 else age + 3
        }
    
    def _generate_verification_recommendation(self, support_score: float,
                                             supporting: List, conflicting: List) -> str:
        """Gera recomendação baseada na verificação"""
        
        if support_score >= 0.7:
            return "✅ Esta afirmação é bem suportada por fatos conhecidos."
        elif support_score >= 0.5:
            return "⚠️ Esta afirmação tem algum suporte, mas pode precisar de mais verificação."
        elif support_score >= 0.3:
            return "⚠️ Cuidado: existem fatos conflitantes sobre esta afirmação."
        else:
            return "❌ Esta afirmação contradiz fatos conhecidos. Verifique suas fontes."
    
    def get_collection_stats(self) -> Dict[str, Any]:
        """Obtém estatísticas das coleções"""
        
        stats = {}
        for name, collection in self.collections.items():
            stats[name] = {
                "document_count": collection.count(),
                "metadata_fields": self._get_metadata_fields(collection)
            }
        
        return {
            "total_collections": len(self.collections),
            "total_documents": sum(s["document_count"] for s in stats.values()),
            "collections": stats,
            "timestamp": datetime.now().isoformat()
        }
    
    def _get_metadata_fields(self, collection: chromadb.Collection) -> List[str]:
        """Obtém campos de metadados de uma coleção"""
        # Método simplificado - em produção, precisaria de amostragem
        try:
            # Tentar obter alguns documentos para ver metadados
            results = collection.peek(limit=5)
            if results["metadatas"]:
                # Usar primeiro documento como referência
                sample_metadata = results["metadatas"][0]
                return list(sample_metadata.keys()) if sample_metadata else []
        except:
            pass
        
        return []

# Teste rápido
if __name__ == "__main__":
    print("📚 Testando Nexus RAG System...")
    
    # Inicializar sistema
    rag = NexusRAGSystem(persist_directory="test_chroma")
    
    # Mostrar estatísticas
    stats = rag.get_collection_stats()
    print(f"\n📊 Estatísticas do sistema:")
    print(f"Total de coleções: {stats['total_collections']}")
    print(f"Total de documentos: {stats['total_documents']}")
    
    # Testar verificação de fato
    test_statement = "A água ferve a 100 graus Celsius"
    verification = rag.verify_fact(test_statement, age_context=12)
    
    print(f"\n🔍 Verificação de fato:")
    print(f"Afirmação: {test_statement}")
    print(f"Score de suporte: {verification['verification_summary']['support_score']:.2f}")
    print(f"Recomendação: {verification['recommendation']}")
    
    # Testar consulta
    query_result = rag.query("emoções básicas", collection="emotional_context")
    print(f"\n📝 Resultados da consulta 'emoções básicas':")
    for i, result in enumerate(query_result["results"][:2]):
        print(f"  {i+1}. {result['document'][:60]}...")
