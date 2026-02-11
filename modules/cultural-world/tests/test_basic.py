"""
Basic Tests for Cultural World Adaptive Nexus

Tests for:
- Pydantic models validation
- Example script execution
- Basic service functionality

TODO: Add comprehensive test coverage
TODO: Add integration tests
TODO: Add performance tests
"""

import pytest
import sys
import os
from datetime import datetime

# Add parent directory to path for imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'backend'))

from app.models import Passport, AnalysisRequest, ArchetypeRequest, PredictRequest


class TestPydanticModels:
    """Test Pydantic model validation"""
    
    def test_passport_valid(self):
        """Test valid passport creation"""
        passport = Passport(
            user_id="usr_test_001",
            name="Test User",
            birth_date="1990-01-01",
            vibrational_signature=[528.0, 432.0, 396.0],
            archetypes=["Explorer", "Creator"],
            talents=["musical", "analytical"],
            cultural_markers={"language": "pt-BR"}
        )
        
        assert passport.user_id == "usr_test_001"
        assert passport.name == "Test User"
        assert len(passport.vibrational_signature) == 3
        assert isinstance(passport.created_at, datetime)
    
    def test_passport_minimal(self):
        """Test minimal passport (required fields only)"""
        passport = Passport(
            user_id="usr_minimal",
            name="Minimal User"
        )
        
        assert passport.user_id == "usr_minimal"
        assert passport.name == "Minimal User"
        assert passport.vibrational_signature is None
        assert passport.archetypes is None
    
    def test_analysis_request_valid(self):
        """Test valid analysis request"""
        request = AnalysisRequest(
            user_id="usr_test_001",
            signal_data=[0.1, 0.2, 0.15, 0.3, 0.25],
            analysis_type="standard"
        )
        
        assert request.user_id == "usr_test_001"
        assert len(request.signal_data) == 5
        assert request.analysis_type == "standard"
    
    def test_archetype_request_valid(self):
        """Test valid archetype request"""
        request = ArchetypeRequest(
            user_id="usr_test_001",
            personality_data={
                "creativity_score": 0.85,
                "exploration_tendency": 0.72
            },
            include_subarchetypes=True
        )
        
        assert request.user_id == "usr_test_001"
        assert request.personality_data["creativity_score"] == 0.85
        assert request.include_subarchetypes is True
    
    def test_predict_request_valid(self):
        """Test valid prediction request"""
        request = PredictRequest(
            user_id="usr_test_001",
            context={"current_phase": "exploration"},
            prediction_type="career",
            time_horizon=90
        )
        
        assert request.user_id == "usr_test_001"
        assert request.prediction_type == "career"
        assert request.time_horizon == 90


class TestVibrationalService:
    """Test vibrational analysis service"""
    
    def test_analyze_signal_basic(self):
        """Test basic signal analysis"""
        from app.services import vibrational
        
        # Simple test signal
        signal_data = [0.1, 0.2, 0.15, 0.3, 0.25, 0.2, 0.15, 0.1]
        
        results = vibrational.analyze_signal(signal_data)
        
        assert "dominant_frequencies" in results
        assert "harmonic_patterns" in results
        assert "resonance_score" in results
        assert "solfeggio_alignment" in results
        
        assert isinstance(results["dominant_frequencies"], list)
        assert isinstance(results["resonance_score"], float)
        assert 0 <= results["resonance_score"] <= 1
    
    def test_solfeggio_frequencies_defined(self):
        """Test that Solfeggio frequencies are defined"""
        from app.services import vibrational
        
        assert 528 in vibrational.SOLFEGGIO_FREQUENCIES
        assert vibrational.SOLFEGGIO_FREQUENCIES[528] == "Transformation & Miracles (DNA Repair)"
    
    def test_generate_recommendations(self):
        """Test recommendation generation"""
        from app.services import vibrational
        
        analysis_results = {
            "resonance_score": 0.5,
            "solfeggio_alignment": {
                "alignment_count": 1,
                "primary_resonance": "Transformation & Miracles (DNA Repair)"
            },
            "harmonic_patterns": {"harmonic_count": 2},
            "signal_quality": {"quality_score": 0.6}
        }
        
        recommendations = vibrational.generate_recommendations(analysis_results)
        
        assert isinstance(recommendations, list)
        assert len(recommendations) > 0


class TestArchetypalService:
    """Test archetypal analysis service"""
    
    def test_analyze_personality_basic(self):
        """Test basic personality analysis"""
        from app.services import archetypal
        
        personality_data = {
            "creativity_score": 0.85,
            "exploration_tendency": 0.72,
            "social_orientation": 0.60
        }
        
        results = archetypal.analyze_personality(personality_data)
        
        assert "primary_archetype" in results
        assert "secondary_archetypes" in results
        assert "archetype_scores" in results
        
        assert isinstance(results["primary_archetype"], str)
        assert isinstance(results["secondary_archetypes"], list)
    
    def test_archetypes_defined(self):
        """Test that archetypes are defined"""
        from app.services import archetypal
        
        assert "Explorer" in archetypal.COMMON_ARCHETYPES
        assert "Creator" in archetypal.COMMON_ARCHETYPES
        assert "Self" in archetypal.JUNGIAN_ARCHETYPES
    
    def test_build_archetype_graph(self):
        """Test archetype graph construction"""
        from app.services import archetypal
        
        graph = archetypal.build_archetype_graph()
        
        assert graph.number_of_nodes() > 0
        assert graph.has_node("Explorer")
        assert graph.has_node("Creator")


class TestTalentService:
    """Test talent profiling service"""
    
    def test_profile_talents_basic(self):
        """Test basic talent profiling"""
        from app.services import talent
        
        user_data = {
            "rhythm_sense": 0.8,
            "pitch_recognition": 0.7,
            "pattern_recognition": 0.9,
            "logical_reasoning": 0.85
        }
        
        results = talent.profile_talents(user_data)
        
        assert "primary_talent" in results
        assert "top_talents" in results
        assert "talent_scores" in results
        
        assert isinstance(results["primary_talent"], str)
        assert isinstance(results["top_talents"], list)
    
    def test_talent_categories_defined(self):
        """Test that talent categories are defined"""
        from app.services import talent
        
        assert "musical" in talent.TALENT_CATEGORIES
        assert "analytical" in talent.TALENT_CATEGORIES
        assert "interpersonal" in talent.TALENT_CATEGORIES


class TestPredictiveService:
    """Test predictive engine service"""
    
    def test_predict_future_state_basic(self):
        """Test basic future state prediction"""
        from app.services import predictive
        
        current_profile = {
            "vibrational_signature": [528.0, 432.0],
            "archetypes": ["Explorer", "Creator"],
            "talents": ["musical", "analytical"]
        }
        
        context = {
            "current_phase": "exploration",
            "prediction_type": "general"
        }
        
        results = predictive.predict_future_state(
            "usr_test_001",
            current_profile,
            context,
            time_horizon=90
        )
        
        assert "user_id" in results
        assert "predictions" in results
        assert "overall_confidence" in results
        assert "time_horizon" in results
        
        assert isinstance(results["predictions"], list)
        assert 0 <= results["overall_confidence"] <= 1


class TestExampleScript:
    """Test example passport script"""
    
    def test_generate_passport(self):
        """Test passport generation"""
        sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'scripts'))
        
        from example_passport import generate_passport
        
        passport = generate_passport(user_id="test_usr", name="Test Name")
        
        assert passport["user_id"] == "test_usr"
        assert passport["name"] == "Test Name"
        assert "vibrational_signature" in passport
        assert "archetypes" in passport
        assert "talents" in passport
        assert "cultural_markers" in passport
        
        # Check vibrational signature
        assert isinstance(passport["vibrational_signature"], list)
        assert len(passport["vibrational_signature"]) == 3
        
        # Check archetypes
        assert isinstance(passport["archetypes"], list)
        assert len(passport["archetypes"]) == 2
        
        # Check talents
        assert isinstance(passport["talents"], list)
        assert len(passport["talents"]) == 2


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
