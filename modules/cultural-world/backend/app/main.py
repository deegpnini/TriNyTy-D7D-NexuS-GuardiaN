"""
Cultural World Adaptive Nexus - Main FastAPI Application

Provides REST API endpoints for:
- Passport creation and management
- Vibrational analysis
- Archetypal profiling
- Talent assessment
- Predictive modeling

Author: Comandante Hebron Nexus
License: MIT + Nexus Ethical Clauses

Usage:
    uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

TODO: Add authentication and authorization
TODO: Implement rate limiting
TODO: Add comprehensive error handling
TODO: Add API versioning
TODO: Add WebSocket support for real-time analysis
"""

from fastapi import FastAPI, HTTPException, Depends, status
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from typing import List, Dict, Any
import uuid
from datetime import datetime

# Import models and services
from .models import (
    Passport, 
    AnalysisRequest, 
    ArchetypeRequest, 
    PredictRequest,
    AnalysisResponse,
    ArchetypeResponse,
    PredictResponse
)
from .db import get_db, init_db, Profile, AnalysisHistory
from .services import vibrational, archetypal, talent, predictive


# Initialize FastAPI app
app = FastAPI(
    title="Cultural World Adaptive Nexus API",
    description="API for vibrational analysis, archetypal profiling, and predictive modeling",
    version="0.1.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# CORS middleware for frontend integration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # TODO: Restrict in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Initialize database on startup
@app.on_event("startup")
async def startup_event():
    """Initialize database tables on startup"""
    init_db()
    print("🌀 Cultural World Adaptive Nexus API started successfully")
    print("📚 API Documentation available at: http://localhost:8000/docs")


@app.get("/")
async def root():
    """Root endpoint with API information"""
    return {
        "name": "Cultural World Adaptive Nexus API",
        "version": "0.1.0",
        "description": "Multi-dimensional human potential mapping system",
        "endpoints": {
            "passport": "/passport (POST) - Create cultural passport",
            "analyze_vibrational": "/analyze/vibrational (POST) - Analyze vibrational signature",
            "archetype": "/archetype (POST) - Identify archetypal patterns",
            "predict": "/predict (POST) - Generate predictions",
            "docs": "/docs - Interactive API documentation"
        },
        "status": "operational",
        "frequency": "528Hz ✨"
    }


@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {
        "status": "healthy",
        "timestamp": datetime.utcnow().isoformat(),
        "service": "cultural-world-nexus"
    }


@app.post("/passport", status_code=status.HTTP_201_CREATED)
async def create_passport(
    passport: Passport,
    db: Session = Depends(get_db)
) -> Dict[str, Any]:
    """
    Create a new cultural passport for a user
    
    Args:
        passport: Passport data including user_id, name, and optional attributes
        db: Database session
        
    Returns:
        Created passport with ID and status
        
    TODO: Add validation for duplicate user_ids
    TODO: Add support for passport updates
    """
    # Check if profile already exists
    existing = db.query(Profile).filter(Profile.user_id == passport.user_id).first()
    if existing:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=f"Passport already exists for user_id: {passport.user_id}"
        )
    
    # Create new profile
    new_profile = Profile(
        user_id=passport.user_id,
        name=passport.name,
        birth_date=passport.birth_date,
        vibrational_signature=passport.vibrational_signature,
        archetypes=passport.archetypes,
        talents=passport.talents,
        cultural_markers=passport.cultural_markers
    )
    
    db.add(new_profile)
    db.commit()
    db.refresh(new_profile)
    
    return {
        "status": "created",
        "user_id": passport.user_id,
        "message": "Cultural passport created successfully",
        "created_at": new_profile.created_at.isoformat()
    }


@app.get("/passport/{user_id}")
async def get_passport(
    user_id: str,
    db: Session = Depends(get_db)
) -> Dict[str, Any]:
    """
    Retrieve a user's cultural passport
    
    Args:
        user_id: User identifier
        db: Database session
        
    Returns:
        Passport data
    """
    profile = db.query(Profile).filter(Profile.user_id == user_id).first()
    
    if not profile:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Passport not found for user_id: {user_id}"
        )
    
    return {
        "user_id": profile.user_id,
        "name": profile.name,
        "birth_date": profile.birth_date,
        "vibrational_signature": profile.vibrational_signature,
        "archetypes": profile.archetypes,
        "talents": profile.talents,
        "cultural_markers": profile.cultural_markers,
        "created_at": profile.created_at.isoformat(),
        "updated_at": profile.updated_at.isoformat()
    }


@app.post("/analyze/vibrational")
async def analyze_vibrational(
    request: AnalysisRequest,
    db: Session = Depends(get_db)
) -> AnalysisResponse:
    """
    Perform vibrational frequency analysis
    
    Args:
        request: Analysis request with user_id and signal_data
        db: Database session
        
    Returns:
        Analysis results with dominant frequencies and recommendations
        
    TODO: Add support for real-time streaming analysis
    TODO: Integrate with audio/biometric input devices
    """
    # Perform vibrational analysis
    analysis_results = vibrational.analyze_signal(
        request.signal_data,
        sample_rate=1000.0  # TODO: Make configurable
    )
    
    # Generate recommendations
    recommendations = vibrational.generate_recommendations(analysis_results)
    
    # Store analysis history
    history_entry = AnalysisHistory(
        id=str(uuid.uuid4()),
        user_id=request.user_id,
        analysis_type=request.analysis_type,
        dominant_frequencies=analysis_results["dominant_frequencies"],
        resonance_score=analysis_results["resonance_score"],
        results=analysis_results,
        created_at=datetime.utcnow()
    )
    db.add(history_entry)
    db.commit()
    
    return AnalysisResponse(
        user_id=request.user_id,
        dominant_frequencies=analysis_results["dominant_frequencies"],
        harmonic_patterns=analysis_results["harmonic_patterns"],
        resonance_score=analysis_results["resonance_score"],
        recommendations=recommendations
    )


@app.post("/archetype")
async def analyze_archetype(
    request: ArchetypeRequest,
    db: Session = Depends(get_db)
) -> ArchetypeResponse:
    """
    Perform archetypal profiling
    
    Args:
        request: Archetype request with user_id and personality_data
        db: Database session
        
    Returns:
        Archetype profile with primary and secondary archetypes
        
    TODO: Add support for journey predictions
    TODO: Integrate with personality assessment frameworks
    """
    # Analyze personality for archetypes
    archetype_results = archetypal.analyze_personality(request.personality_data)
    
    # Get journey prediction if requested
    journey = None
    if request.include_subarchetypes:
        journey = archetypal.predict_archetypal_journey(
            archetype_results["primary_archetype"],
            request.personality_data
        )
    
    # Update user profile with archetype information
    profile = db.query(Profile).filter(Profile.user_id == request.user_id).first()
    if profile:
        profile.archetypes = [archetype_results["primary_archetype"]] + archetype_results["secondary_archetypes"]
        profile.updated_at = datetime.utcnow()
        db.commit()
    
    return ArchetypeResponse(
        user_id=request.user_id,
        primary_archetype=archetype_results["primary_archetype"],
        secondary_archetypes=archetype_results["secondary_archetypes"],
        archetype_scores=archetype_results["archetype_scores"],
        archetypal_journey=journey
    )


@app.post("/talent")
async def profile_talent(
    user_id: str,
    user_data: Dict[str, Any],
    db: Session = Depends(get_db)
) -> Dict[str, Any]:
    """
    Perform talent profiling
    
    Args:
        user_id: User identifier
        user_data: User performance and assessment data
        db: Database session
        
    Returns:
        Talent profile with scores and recommendations
        
    TODO: Add validation for user_data structure
    TODO: Integrate with skill assessment platforms
    """
    # Profile talents
    talent_results = talent.profile_talents(user_data)
    
    # Update user profile with talent information
    profile = db.query(Profile).filter(Profile.user_id == user_id).first()
    if profile:
        profile.talents = talent_results["top_talents"]
        profile.updated_at = datetime.utcnow()
        db.commit()
    
    return {
        "user_id": user_id,
        **talent_results
    }


@app.post("/predict")
async def make_prediction(
    request: PredictRequest,
    db: Session = Depends(get_db)
) -> PredictResponse:
    """
    Generate predictions based on user profile and context
    
    Args:
        request: Prediction request with user_id, context, and parameters
        db: Database session
        
    Returns:
        Predictions with confidence scores and recommendations
        
    TODO: Add support for multiple prediction scenarios
    TODO: Implement confidence intervals
    """
    # Get user profile
    profile = db.query(Profile).filter(Profile.user_id == request.user_id).first()
    
    if not profile:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Profile not found for user_id: {request.user_id}. Create a passport first."
        )
    
    # Build current profile for prediction
    current_profile = {
        "vibrational_signature": profile.vibrational_signature,
        "archetypes": profile.archetypes,
        "talents": profile.talents,
        "cultural_markers": profile.cultural_markers
    }
    
    # Generate predictions
    prediction_results = predictive.predict_future_state(
        request.user_id,
        current_profile,
        request.context,
        request.time_horizon or 90
    )
    
    # Extract recommendations
    recommendations = []
    for pred in prediction_results["predictions"]:
        recommendations.extend(pred.get("recommendations", []))
    
    return PredictResponse(
        user_id=request.user_id,
        predictions=prediction_results["predictions"],
        recommendations=recommendations[:5],  # Top 5 recommendations
        confidence=prediction_results["overall_confidence"],
        time_horizon=prediction_results["time_horizon"]
    )


@app.get("/analysis/history/{user_id}")
async def get_analysis_history(
    user_id: str,
    limit: int = 10,
    db: Session = Depends(get_db)
) -> List[Dict[str, Any]]:
    """
    Get analysis history for a user
    
    Args:
        user_id: User identifier
        limit: Maximum number of results (default: 10)
        db: Database session
        
    Returns:
        List of historical analyses
    """
    history = (
        db.query(AnalysisHistory)
        .filter(AnalysisHistory.user_id == user_id)
        .order_by(AnalysisHistory.created_at.desc())
        .limit(limit)
        .all()
    )
    
    return [
        {
            "id": entry.id,
            "analysis_type": entry.analysis_type,
            "dominant_frequencies": entry.dominant_frequencies,
            "resonance_score": entry.resonance_score,
            "created_at": entry.created_at.isoformat()
        }
        for entry in history
    ]


# Additional utility endpoints

@app.get("/solfeggio")
async def get_solfeggio_frequencies():
    """Get information about Solfeggio healing frequencies"""
    return {
        "frequencies": vibrational.SOLFEGGIO_FREQUENCIES,
        "description": "Ancient healing frequencies used in sacred music and sound therapy"
    }


@app.get("/archetypes")
async def get_archetype_info():
    """Get information about available archetypes"""
    return {
        "jungian": archetypal.JUNGIAN_ARCHETYPES,
        "common": archetypal.COMMON_ARCHETYPES,
        "description": "Archetypal patterns for human psychology and development"
    }


@app.get("/talents")
async def get_talent_categories():
    """Get information about talent categories"""
    return {
        "categories": talent.TALENT_CATEGORIES,
        "description": "Multiple intelligence framework for talent identification"
    }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
