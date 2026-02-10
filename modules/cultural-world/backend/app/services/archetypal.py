"""
Archetypal Analysis Service

Implements archetypal profiling using graph-based pattern recognition.
Maps personality data to archetypal frameworks including:
- Jungian archetypes
- Hero's Journey stages
- Cultural archetypes

Uses networkx for graph-based archetype relationships.

TODO: Implement ML-based archetype classification
TODO: Add support for cultural-specific archetypes
TODO: Integrate with personality assessment frameworks (Big 5, MBTI, etc.)
TODO: Add archetypal journey prediction and evolution tracking
"""

import networkx as nx
from typing import Dict, List, Any, Tuple
import random


# Core Jungian Archetypes with characteristics
JUNGIAN_ARCHETYPES = {
    "Self": {
        "description": "The unified unconscious and conscious, wholeness",
        "traits": ["integration", "balance", "wisdom", "completeness"],
        "frequency": 963  # Crown chakra / Divine consciousness
    },
    "Shadow": {
        "description": "Hidden or rejected aspects of self",
        "traits": ["unconscious", "repressed", "mysterious", "transformative"],
        "frequency": 396  # Liberation from fear
    },
    "Anima/Animus": {
        "description": "Contrasexual aspect of psyche",
        "traits": ["integration", "balance", "relationship", "soul"],
        "frequency": 639  # Connection & Relationships
    },
    "Persona": {
        "description": "Social mask or role",
        "traits": ["social", "adaptive", "outward", "protective"],
        "frequency": 528  # Transformation & Miracles
    }
}


# Additional Common Archetypes
COMMON_ARCHETYPES = {
    "Explorer": {
        "description": "Seeker of new experiences and knowledge",
        "traits": ["curiosity", "adventure", "independence", "discovery"],
        "related_to": ["Hero", "Sage"],
        "frequency": 852  # Awakening intuition
    },
    "Creator": {
        "description": "Brings new things into existence",
        "traits": ["imagination", "innovation", "expression", "vision"],
        "related_to": ["Magician", "Artist"],
        "frequency": 528  # Transformation & Miracles
    },
    "Hero": {
        "description": "Overcomes challenges and transforms",
        "traits": ["courage", "determination", "growth", "triumph"],
        "related_to": ["Warrior", "Explorer"],
        "frequency": 741  # Awakening intuition
    },
    "Caregiver": {
        "description": "Nurtures and protects others",
        "traits": ["compassion", "nurturing", "protection", "service"],
        "related_to": ["Mother", "Healer"],
        "frequency": 639  # Connection & Relationships
    },
    "Sage": {
        "description": "Seeks truth and wisdom",
        "traits": ["wisdom", "knowledge", "truth", "understanding"],
        "related_to": ["Teacher", "Philosopher"],
        "frequency": 852  # Awakening intuition
    },
    "Innocent": {
        "description": "Optimistic and trusting",
        "traits": ["optimism", "trust", "simplicity", "purity"],
        "related_to": ["Child", "Dreamer"],
        "frequency": 528  # Transformation & Miracles
    },
    "Magician": {
        "description": "Transforms reality through knowledge",
        "traits": ["transformation", "power", "knowledge", "catalyst"],
        "related_to": ["Creator", "Sage"],
        "frequency": 963  # Divine consciousness
    },
    "Rebel": {
        "description": "Challenges status quo",
        "traits": ["revolution", "independence", "disruption", "freedom"],
        "related_to": ["Hero", "Explorer"],
        "frequency": 417  # Facilitation of change
    },
    "Lover": {
        "description": "Seeks connection and passion",
        "traits": ["passion", "intimacy", "connection", "beauty"],
        "related_to": ["Caregiver", "Artist"],
        "frequency": 639  # Connection & Relationships
    },
    "Ruler": {
        "description": "Creates order and stability",
        "traits": ["leadership", "control", "responsibility", "order"],
        "related_to": ["Father", "King"],
        "frequency": 285  # Energy & Safety
    }
}


def build_archetype_graph() -> nx.Graph:
    """
    Build a graph of archetype relationships
    
    Returns:
        NetworkX graph with archetypes as nodes and relationships as edges
    """
    G = nx.Graph()
    
    # Add all archetypes as nodes
    all_archetypes = {**JUNGIAN_ARCHETYPES, **COMMON_ARCHETYPES}
    for name, data in all_archetypes.items():
        G.add_node(name, **data)
    
    # Add edges based on related_to relationships
    for name, data in COMMON_ARCHETYPES.items():
        if "related_to" in data:
            for related in data["related_to"]:
                if related in all_archetypes:
                    G.add_edge(name, related, weight=0.8)
    
    # Add complementary relationships (opposites attract)
    complementary_pairs = [
        ("Explorer", "Ruler"),
        ("Creator", "Caregiver"),
        ("Hero", "Sage"),
        ("Rebel", "Innocent"),
        ("Magician", "Lover")
    ]
    
    for arch1, arch2 in complementary_pairs:
        if arch1 in G and arch2 in G:
            G.add_edge(arch1, arch2, weight=0.5, type="complementary")
    
    return G


def analyze_personality(personality_data: Dict[str, Any]) -> Dict[str, Any]:
    """
    Analyze personality data to identify archetypal patterns
    
    Args:
        personality_data: Dictionary of personality traits and scores
        
    Returns:
        Dictionary with archetype analysis results
        
    TODO: Implement ML-based classification
    TODO: Add support for multiple assessment frameworks
    """
    # POC: Simple trait-based matching
    # In production, use ML models trained on personality datasets
    
    archetype_scores = {}
    all_archetypes = {**JUNGIAN_ARCHETYPES, **COMMON_ARCHETYPES}
    
    # Calculate scores based on trait overlap (simplified)
    for archetype_name, archetype_data in all_archetypes.items():
        score = 0.0
        trait_matches = 0
        
        # Check personality data keys against archetype traits
        for trait in archetype_data.get("traits", []):
            # Look for matching or related keys in personality_data
            for key, value in personality_data.items():
                if trait.lower() in key.lower() or key.lower() in trait.lower():
                    if isinstance(value, (int, float)):
                        score += float(value)
                        trait_matches += 1
        
        # Normalize score
        if trait_matches > 0:
            archetype_scores[archetype_name] = score / trait_matches
        else:
            # Assign random small score for POC
            archetype_scores[archetype_name] = random.uniform(0.1, 0.3)
    
    # Sort archetypes by score
    sorted_archetypes = sorted(
        archetype_scores.items(), 
        key=lambda x: x[1], 
        reverse=True
    )
    
    primary_archetype = sorted_archetypes[0][0]
    secondary_archetypes = [arch for arch, score in sorted_archetypes[1:4]]
    
    return {
        "primary_archetype": primary_archetype,
        "secondary_archetypes": secondary_archetypes,
        "archetype_scores": archetype_scores,
        "dominant_traits": all_archetypes[primary_archetype]["traits"],
        "associated_frequency": all_archetypes[primary_archetype].get("frequency", 528)
    }


def predict_archetypal_journey(
    current_archetype: str, 
    personality_data: Dict[str, Any]
) -> Dict[str, Any]:
    """
    Predict archetypal development journey
    
    Args:
        current_archetype: Current primary archetype
        personality_data: Current personality data
        
    Returns:
        Predicted journey stages and recommendations
        
    TODO: Implement journey prediction based on life stage and goals
    TODO: Add integration with Hero's Journey framework
    """
    G = build_archetype_graph()
    
    # Find connected archetypes (potential development paths)
    if current_archetype in G:
        connected = list(G.neighbors(current_archetype))
        
        # Calculate path scores
        journey_paths = []
        for target in connected[:3]:  # Top 3 paths
            try:
                path = nx.shortest_path(G, current_archetype, target)
                journey_paths.append({
                    "target_archetype": target,
                    "path": path,
                    "distance": len(path) - 1,
                    "description": COMMON_ARCHETYPES.get(
                        target, 
                        JUNGIAN_ARCHETYPES.get(target, {})
                    ).get("description", "")
                })
            except nx.NetworkXNoPath:
                continue
    else:
        journey_paths = []
    
    return {
        "current_stage": current_archetype,
        "potential_paths": journey_paths,
        "recommended_next_stage": journey_paths[0]["target_archetype"] if journey_paths else None,
        "development_focus": _get_development_focus(current_archetype)
    }


def _get_development_focus(archetype: str) -> List[str]:
    """Get development recommendations for an archetype"""
    focus_map = {
        "Explorer": ["Cultivate grounding", "Balance adventure with stability", "Document discoveries"],
        "Creator": ["Practice discipline", "Learn technical skills", "Share creations"],
        "Hero": ["Develop humility", "Seek mentorship", "Recognize limits"],
        "Caregiver": ["Practice self-care", "Set boundaries", "Receive support"],
        "Sage": ["Apply knowledge", "Teach others", "Embrace uncertainty"],
        "Innocent": ["Build resilience", "Face reality", "Maintain optimism"],
        "Magician": ["Use power wisely", "Stay grounded", "Serve others"],
        "Rebel": ["Choose battles wisely", "Build constructively", "Find community"],
        "Lover": ["Balance passion and reason", "Maintain identity", "Develop discernment"],
        "Ruler": ["Share power", "Serve community", "Stay flexible"]
    }
    
    return focus_map.get(archetype, ["Continue self-discovery", "Embrace growth", "Seek balance"])


def get_archetype_recommendations(analysis_results: Dict[str, Any]) -> List[str]:
    """
    Generate recommendations based on archetypal analysis
    
    Args:
        analysis_results: Results from analyze_personality()
        
    Returns:
        List of actionable recommendations
    """
    recommendations = []
    
    primary = analysis_results["primary_archetype"]
    frequency = analysis_results["associated_frequency"]
    
    recommendations.append(
        f"Your primary archetype is {primary}. "
        f"Resonate with {frequency}Hz frequency for alignment."
    )
    
    # Add trait-specific recommendations
    traits = analysis_results["dominant_traits"]
    recommendations.append(
        f"Focus on developing: {', '.join(traits[:3])}"
    )
    
    # Add balance recommendations
    secondaries = analysis_results["secondary_archetypes"]
    if len(secondaries) > 0:
        recommendations.append(
            f"Balance your primary archetype with qualities from: {secondaries[0]}"
        )
    
    return recommendations
