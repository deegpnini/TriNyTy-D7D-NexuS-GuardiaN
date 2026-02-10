"""
Pydantic Models for Cultural World Adaptive Nexus API

Defines data models for:
- Passport: User identity and vibrational signature
- AnalysisRequest: Request for vibrational analysis
- ArchetypeRequest: Request for archetypal profiling
- PredictRequest: Request for predictive modeling

TODO: Expand models with validation and complex nested structures
TODO: Add examples and documentation for each field
"""

from typing import List, Optional, Dict, Any
from pydantic import BaseModel, Field
from datetime import datetime


class Passport(BaseModel):
    """
    Cultural Passport - User's vibrational identity and profile
    
    Represents a user's unique cultural and vibrational signature,
    combining personal data with frequency patterns and archetypal associations.
    """
    user_id: str = Field(..., description="Unique user identifier")
    name: str = Field(..., description="User's display name")
    birth_date: Optional[str] = Field(None, description="Birth date (ISO format)")
    vibrational_signature: Optional[List[float]] = Field(
        None, 
        description="Core vibrational frequencies (Hz) - e.g., [528, 432, 963]"
    )
    archetypes: Optional[List[str]] = Field(
        None, 
        description="Identified archetypal patterns - e.g., ['Creator', 'Explorer']"
    )
    talents: Optional[List[str]] = Field(
        None, 
        description="Identified talents - e.g., ['musical', 'analytical']"
    )
    cultural_markers: Optional[Dict[str, Any]] = Field(
        None, 
        description="Cultural context and preferences"
    )
    created_at: datetime = Field(default_factory=datetime.utcnow)
    
    class Config:
        json_schema_extra = {
            "example": {
                "user_id": "usr_abc123",
                "name": "João Silva",
                "birth_date": "1990-05-15",
                "vibrational_signature": [528.0, 432.0, 396.0],
                "archetypes": ["Explorer", "Creator"],
                "talents": ["musical", "linguistic"],
                "cultural_markers": {
                    "language": "pt-BR",
                    "region": "São Paulo",
                    "interests": ["music", "technology"]
                }
            }
        }


class AnalysisRequest(BaseModel):
    """Request for vibrational frequency analysis"""
    user_id: str = Field(..., description="User identifier")
    signal_data: List[float] = Field(
        ..., 
        description="Time-series signal data for analysis (e.g., voice, biometric)"
    )
    analysis_type: str = Field(
        default="standard", 
        description="Type of analysis: 'standard', 'deep', 'harmonic'"
    )
    
    class Config:
        json_schema_extra = {
            "example": {
                "user_id": "usr_abc123",
                "signal_data": [0.1, 0.2, 0.15, 0.3, 0.25],
                "analysis_type": "standard"
            }
        }


class ArchetypeRequest(BaseModel):
    """Request for archetypal profiling"""
    user_id: str = Field(..., description="User identifier")
    personality_data: Dict[str, Any] = Field(
        ..., 
        description="Personality assessment data (responses, preferences)"
    )
    include_subarchetypes: bool = Field(
        default=False, 
        description="Include detailed sub-archetypal analysis"
    )
    
    class Config:
        json_schema_extra = {
            "example": {
                "user_id": "usr_abc123",
                "personality_data": {
                    "creativity_score": 0.85,
                    "exploration_tendency": 0.72,
                    "social_orientation": 0.60
                },
                "include_subarchetypes": True
            }
        }


class PredictRequest(BaseModel):
    """Request for predictive modeling and recommendations"""
    user_id: str = Field(..., description="User identifier")
    context: Dict[str, Any] = Field(
        ..., 
        description="Current context and parameters for prediction"
    )
    prediction_type: str = Field(
        default="general", 
        description="Type of prediction: 'general', 'career', 'relationships', 'growth'"
    )
    time_horizon: Optional[int] = Field(
        None, 
        description="Time horizon for prediction (days)"
    )
    
    class Config:
        json_schema_extra = {
            "example": {
                "user_id": "usr_abc123",
                "context": {
                    "current_phase": "exploration",
                    "recent_activities": ["learning", "creating"],
                    "goals": ["career_growth", "personal_development"]
                },
                "prediction_type": "career",
                "time_horizon": 90
            }
        }


class AnalysisResponse(BaseModel):
    """Response from vibrational analysis"""
    user_id: str
    dominant_frequencies: List[float] = Field(
        description="Identified dominant frequencies in Hz"
    )
    harmonic_patterns: Dict[str, Any] = Field(
        description="Detected harmonic patterns and relationships"
    )
    resonance_score: float = Field(
        description="Overall resonance quality (0-1)"
    )
    recommendations: List[str] = Field(
        description="Recommendations based on analysis"
    )


class ArchetypeResponse(BaseModel):
    """Response from archetypal profiling"""
    user_id: str
    primary_archetype: str = Field(description="Primary identified archetype")
    secondary_archetypes: List[str] = Field(
        description="Secondary archetypes in order of strength"
    )
    archetype_scores: Dict[str, float] = Field(
        description="Confidence scores for each archetype (0-1)"
    )
    archetypal_journey: Optional[Dict[str, Any]] = Field(
        None, 
        description="Predicted archetypal development path"
    )


class PredictResponse(BaseModel):
    """Response from predictive engine"""
    user_id: str
    predictions: List[Dict[str, Any]] = Field(
        description="List of predictions with confidence scores"
    )
    recommendations: List[str] = Field(
        description="Actionable recommendations"
    )
    confidence: float = Field(description="Overall prediction confidence (0-1)")
    time_horizon: int = Field(description="Prediction time horizon in days")
