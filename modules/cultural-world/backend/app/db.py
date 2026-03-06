"""
Database Configuration for Cultural World Adaptive Nexus

Provides SQLAlchemy setup with SQLite database for storing:
- User profiles and cultural passports
- Analysis history
- Archetypal progressions

TODO: Migrate to PostgreSQL for production
TODO: Add database migrations with Alembic
TODO: Implement proper connection pooling
"""

from sqlalchemy import create_engine, Column, String, DateTime, JSON, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime
import os

# Database URL - defaults to SQLite for POC
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./cultural_world.db")

# Create engine
engine = create_engine(
    DATABASE_URL, 
    connect_args={"check_same_thread": False} if "sqlite" in DATABASE_URL else {}
)

# Session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for models
Base = declarative_base()


class Profile(Base):
    """
    User Profile Model
    
    Stores user cultural passport data and vibrational signatures.
    """
    __tablename__ = "profiles"
    
    user_id = Column(String, primary_key=True, index=True)
    name = Column(String, nullable=False)
    birth_date = Column(String, nullable=True)
    vibrational_signature = Column(JSON, nullable=True)  # List of frequencies
    archetypes = Column(JSON, nullable=True)  # List of archetype names
    talents = Column(JSON, nullable=True)  # List of talent identifiers
    cultural_markers = Column(JSON, nullable=True)  # Dict of cultural data
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)


class AnalysisHistory(Base):
    """
    Analysis History Model
    
    Stores historical vibrational analysis results for tracking evolution.
    """
    __tablename__ = "analysis_history"
    
    id = Column(String, primary_key=True)
    user_id = Column(String, index=True, nullable=False)
    analysis_type = Column(String, nullable=False)
    dominant_frequencies = Column(JSON, nullable=True)
    resonance_score = Column(Float, nullable=True)
    results = Column(JSON, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)


# Database initialization
def init_db():
    """Initialize database tables"""
    Base.metadata.create_all(bind=engine)


def get_db():
    """
    Dependency function for FastAPI to get database session
    
    Usage in FastAPI routes:
        @app.get("/endpoint")
        def endpoint(db: Session = Depends(get_db)):
            ...
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Initialize database on import (for POC)
# In production, use proper migration tools
if __name__ == "__main__":
    init_db()
    print("Database initialized successfully")
