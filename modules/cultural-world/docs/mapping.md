# Cultural World Adaptive Nexus - Responsibility Mapping

## Module Responsibilities

This document maps the responsibilities of each module and service within the Cultural World Adaptive Nexus system.

## Backend Services

### `app/main.py` - FastAPI Application

**Responsibilities**:
- HTTP request handling and routing
- API endpoint definitions
- Request validation via Pydantic models
- Response formatting
- CORS middleware configuration
- Database session management (dependency injection)
- Error handling and HTTP status codes
- API documentation (OpenAPI/Swagger)

**Dependencies**:
- FastAPI framework
- Pydantic for data validation
- SQLAlchemy for database access
- All service modules

### `app/models.py` - Data Models

**Responsibilities**:
- Define Pydantic models for API requests/responses
- Data validation rules
- Type definitions
- Schema examples for documentation
- Serialization/deserialization logic

**Models**:
- `Passport`: User cultural passport data
- `AnalysisRequest`: Vibrational analysis request
- `ArchetypeRequest`: Archetype profiling request
- `PredictRequest`: Prediction generation request
- `AnalysisResponse`: Analysis results
- `ArchetypeResponse`: Archetype profile
- `PredictResponse`: Predictions

### `app/db.py` - Database Layer

**Responsibilities**:
- Database connection management
- SQLAlchemy ORM models
- Database initialization and migration
- Session factory and dependency injection
- Query abstractions

**Models**:
- `Profile`: User cultural passport storage
- `AnalysisHistory`: Historical analysis records

**Database**: SQLite (POC) → PostgreSQL (production)

### `app/services/vibrational.py` - Vibrational Analysis

**Responsibilities**:
- Signal processing (FFT, spectral analysis)
- Frequency extraction and identification
- Harmonic pattern detection
- Solfeggio frequency alignment calculation
- Resonance quality assessment
- Signal quality metrics
- Recommendation generation based on vibrational data

**Key Functions**:
- `analyze_signal()`: Main analysis pipeline
- `_calculate_solfeggio_alignment()`: Match frequencies to Solfeggio scale
- `_detect_harmonics()`: Find harmonic relationships
- `_assess_signal_quality()`: Quality metrics
- `generate_recommendations()`: Create actionable advice

**Technologies**:
- NumPy for array operations
- SciPy for signal processing (FFT, filters)
- Custom algorithms for pattern detection

### `app/services/archetypal.py` - Archetypal Analysis

**Responsibilities**:
- Personality data analysis
- Archetype classification and scoring
- Archetype relationship graph management
- Journey path prediction
- Development focus recommendations
- Integration with Jungian and modern archetype frameworks

**Key Functions**:
- `analyze_personality()`: Identify archetypes from personality data
- `build_archetype_graph()`: Create archetype relationship network
- `predict_archetypal_journey()`: Forecast development path
- `get_archetype_recommendations()`: Generate guidance

**Technologies**:
- NetworkX for graph-based archetype relationships
- Pattern matching algorithms
- (Future: ML classifiers)

**Archetype Frameworks**:
- Jungian: Self, Shadow, Anima/Animus, Persona
- Common: Explorer, Creator, Hero, Caregiver, Sage, Innocent, Magician, Rebel, Lover, Ruler

### `app/services/talent.py` - Talent Profiling

**Responsibilities**:
- Multiple intelligence assessment
- Talent scoring across dimensions
- Learning style identification
- Career alignment suggestions
- Talent trajectory prediction
- Development priority identification
- Integration with archetypal profiles

**Key Functions**:
- `profile_talents()`: Main talent assessment
- `_generate_talent_profile()`: Comprehensive profile creation
- `_get_talent_development_recommendations()`: Development guidance
- `predict_talent_trajectory()`: Growth forecasting
- `integrate_with_archetypes()`: Cross-layer integration

**Technologies**:
- Scikit-learn for ML (POC stubs, future trained models)
- StandardScaler for normalization
- PCA for dimensionality reduction

**Talent Dimensions** (Gardner's Multiple Intelligences):
1. Musical
2. Analytical (Logical-Mathematical)
3. Linguistic (Verbal)
4. Spatial (Visual)
5. Kinesthetic (Bodily)
6. Interpersonal (Social)
7. Intrapersonal (Self-aware)
8. Naturalistic

### `app/services/predictive.py` - Predictive Engine

**Responsibilities**:
- Future state prediction
- Multi-scenario forecasting (career, relationships, growth)
- Optimal timing recommendations
- Integration of all analysis layers
- Confidence scoring
- Holistic insight generation

**Key Functions**:
- `predict_future_state()`: Main prediction pipeline
- `_predict_career_development()`: Career forecasting
- `_predict_relationship_dynamics()`: Relationship predictions
- `_predict_personal_growth()`: Growth trajectory
- `generate_optimal_timing()`: Activity timing optimization
- `integrate_predictions()`: Multi-layer synthesis

**Technologies**:
- Time-series analysis
- Rule-based systems (POC)
- (Future: ML prediction models, neural networks)

## Conceptual Mappings

### Frequency → Archetype → Talent Mapping

This table shows how different dimensions relate to each other:

| Frequency (Hz) | Meaning | Related Archetypes | Related Talents |
|---------------|---------|-------------------|-----------------|
| 174 | Pain Relief | Shadow (healing) | Intrapersonal |
| 285 | Energy & Safety | Ruler, Hero | Kinesthetic |
| 396 | Liberation from Fear | Shadow (transformation) | Intrapersonal |
| 417 | Facilitation of Change | Rebel, Explorer | Analytical |
| 528 | Transformation & Miracles | Creator, Magician, Innocent | Musical, Spatial |
| 639 | Connection & Relationships | Lover, Caregiver, Anima/Animus | Interpersonal |
| 741 | Awakening Intuition | Sage, Hero | Analytical, Linguistic |
| 852 | Spiritual Order | Sage, Explorer | Intrapersonal, Naturalistic |
| 963 | Divine Consciousness | Self, Magician | Intrapersonal |

### Archetype → Talent → Career Examples

| Archetype | Primary Talents | Career Alignments |
|-----------|----------------|-------------------|
| Explorer | Naturalistic, Kinesthetic | Researcher, Traveler, Scientist |
| Creator | Musical, Spatial | Artist, Designer, Musician |
| Hero | Kinesthetic, Analytical | Athlete, Engineer, Entrepreneur |
| Caregiver | Interpersonal, Intrapersonal | Nurse, Teacher, Counselor |
| Sage | Linguistic, Analytical | Professor, Writer, Analyst |
| Innocent | Musical, Interpersonal | Performer, Child Worker, Guide |
| Magician | Analytical, Spatial | Programmer, Architect, Scientist |
| Rebel | Linguistic, Interpersonal | Activist, Innovator, Disruptor |
| Lover | Interpersonal, Musical | Artist, Therapist, Relationship Coach |
| Ruler | Analytical, Interpersonal | Manager, CEO, Administrator |

### Learning Style by Talent Profile

| Primary Talents | Learning Style | Optimal Methods |
|----------------|---------------|-----------------|
| Analytical, Linguistic | Cognitive-Verbal | Reading, lectures, discussions |
| Spatial, Kinesthetic | Experiential-Visual | Hands-on, visual aids, movement |
| Interpersonal, Linguistic | Collaborative-Social | Group work, peer learning |
| Intrapersonal, Naturalistic | Reflective-Observational | Journaling, observation, meditation |
| Musical, Spatial | Creative-Artistic | Expression, creation, exploration |

## Integration Flows

### Layer Integration Flow

```
┌──────────────────────────────────────────────────────┐
│ 1. VIBRATIONAL ANALYSIS                              │
│    Input: Signal data (voice, biometric)             │
│    Output: Frequencies, harmonics, resonance         │
│    Feeds: Frequency data to Layer 2                  │
└──────────────────────────────────────────────────────┘
                         ↓
┌──────────────────────────────────────────────────────┐
│ 2. ARCHETYPAL PROFILING                              │
│    Input: Personality data + frequencies             │
│    Output: Archetype profile, journey path           │
│    Feeds: Archetype data to Layer 3                  │
└──────────────────────────────────────────────────────┘
                         ↓
┌──────────────────────────────────────────────────────┐
│ 3. TALENT ASSESSMENT                                 │
│    Input: Performance data + archetypes              │
│    Output: Talent profile, learning style            │
│    Feeds: Talent data to Layer 4                     │
└──────────────────────────────────────────────────────┘
                         ↓
┌──────────────────────────────────────────────────────┐
│ 4. CULTURAL INTEGRATION                              │
│    Input: Context data + talents                     │
│    Output: Cultural profile, preferences             │
│    Feeds: Complete profile to Layer 5               │
└──────────────────────────────────────────────────────┘
                         ↓
┌──────────────────────────────────────────────────────┐
│ 5. PREDICTIVE MODELING                               │
│    Input: All layers + context + goals               │
│    Output: Predictions, recommendations, timing      │
│    Result: Holistic guidance for user                │
└──────────────────────────────────────────────────────┘
```

### Typical User Journey

1. **Passport Creation**
   - User provides basic info (name, birth date)
   - Optional: Cultural markers and preferences
   - System creates profile in database

2. **Vibrational Analysis**
   - User provides signal data (voice recording)
   - System analyzes frequencies
   - Identifies Solfeggio alignments
   - Stores analysis history

3. **Archetypal Profiling**
   - User completes personality assessment
   - System identifies primary/secondary archetypes
   - Predicts journey path
   - Updates passport with archetypes

4. **Talent Assessment**
   - User provides performance/skill data
   - System profiles talents across dimensions
   - Identifies learning style
   - Suggests career alignments
   - Updates passport with talents

5. **Prediction Generation**
   - User specifies context and goals
   - System integrates all layers
   - Generates predictions with confidence scores
   - Provides actionable recommendations
   - Suggests optimal timing

6. **Ongoing Evolution**
   - Periodic re-analysis tracks changes
   - History shows development trajectory
   - Recommendations adapt to growth
   - System learns from user feedback

## API Endpoint Responsibilities

### Core CRUD Operations

- `POST /passport` → Create user profile (writes to `profiles` table)
- `GET /passport/{user_id}` → Retrieve user profile (reads from `profiles`)
- `POST /analyze/vibrational` → Run vibrational analysis (calls `vibrational.analyze_signal`, writes to `analysis_history`)
- `POST /archetype` → Profile archetypes (calls `archetypal.analyze_personality`, updates `profiles.archetypes`)
- `POST /talent` → Assess talents (calls `talent.profile_talents`, updates `profiles.talents`)
- `POST /predict` → Generate predictions (calls `predictive.predict_future_state`, integrates all layers)

### Information Endpoints

- `GET /solfeggio` → Reference data for frequencies
- `GET /archetypes` → Catalog of available archetypes
- `GET /talents` → Description of talent dimensions
- `GET /analysis/history/{user_id}` → Historical analyses for user

## Frontend Component Responsibilities (Future)

### Passport Module
- **PassportCreator**: Guided questionnaire for profile creation
- **PassportCard**: Display user passport summary

### Vibrational Module
- **FrequencyVisualizer**: 3D frequency spectrum display
- **SolfeggioWheel**: Interactive frequency wheel with audio playback

### Archetype Module
- **JourneyMap**: 3D graph of archetypal development path
- **ArchetypeCard**: Display archetype details and traits

### Talent Module
- **TalentConstellation**: 3D star map of talents
- **TalentRadar**: Radar chart of talent dimensions

### Predictive Module
- **Timeline**: Interactive timeline with predictions
- **PredictionCard**: Display individual predictions

## Integration with Repository Modules

### modules/datasets/
- **Purpose**: Historical data for ML training
- **Cultural World Use**: Training archetypal classifiers, talent predictors
- **Data Flow**: Datasets → Model training → Service modules

### modules/vectors/
- **Purpose**: Embedding representations
- **Cultural World Use**: Vector representations of profiles for similarity matching
- **Data Flow**: Profiles → Embeddings → Similarity search

### modules/ethics/
- **Purpose**: Ethical guidelines and privacy controls
- **Cultural World Use**: Ensure all analyses respect Nexus Ethical Clauses
- **Data Flow**: Ethics rules → Service validation → Safe operations

### modules/rag/ (RAG: Retrieval-Augmented Generation)
- **Purpose**: Knowledge retrieval for recommendations
- **Cultural World Use**: Retrieve relevant guidance and insights
- **Data Flow**: Query → RAG retrieval → Enhanced recommendations

## Development Priorities

### Phase 1: POC (Current)
- ✅ Basic service stubs
- ✅ Simple rule-based logic
- ✅ SQLite database
- ✅ REST API endpoints

### Phase 2: ML Integration
- [ ] Train archetype classifiers
- [ ] Implement talent prediction models
- [ ] Add time-series forecasting
- [ ] Integrate with datasets module

### Phase 3: Advanced Features
- [ ] Real-time WebSocket analysis
- [ ] 3D visualization frontend
- [ ] Audio recording integration
- [ ] Mobile apps

### Phase 4: Scale & Production
- [ ] PostgreSQL migration
- [ ] Kubernetes deployment
- [ ] Performance optimization
- [ ] Advanced security

## Maintenance Responsibilities

- **Backend Services**: Python developers, API specialists
- **ML Models**: Data scientists, ML engineers
- **Frontend**: React/Three.js developers
- **Database**: Database administrators
- **DevOps**: Infrastructure engineers
- **Documentation**: Technical writers
- **Community**: Open-source maintainers

## References

- FastAPI Best Practices: https://fastapi.tiangolo.com/
- Gardner's Multiple Intelligences: https://en.wikipedia.org/wiki/Theory_of_multiple_intelligences
- Jungian Archetypes: https://en.wikipedia.org/wiki/Jungian_archetypes
- Solfeggio Frequencies: https://en.wikipedia.org/wiki/Solfeggio_frequencies
