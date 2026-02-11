# Cultural World Adaptive Nexus - Backend

POC implementation of the Cultural World Adaptive Nexus backend services.

## Features

- **Vibrational Analysis**: Frequency analysis of signals (voice, biometric)
- **Archetypal Profiling**: Jungian and modern archetype identification
- **Talent Assessment**: Multiple intelligence framework for talent mapping
- **Predictive Engine**: Future state predictions and recommendations

## Quick Start

### Prerequisites

- Python 3.11+
- pip

### Installation

```bash
cd modules/cultural-world/backend
pip install -r requirements.txt
```

### Running the Server

```bash
# From the backend directory
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

The API will be available at: `http://localhost:8000`

Interactive API documentation: `http://localhost:8000/docs`

### Using Docker

```bash
# Build the image
docker build -t cultural-world-backend .

# Run the container
docker run -p 8000:8000 cultural-world-backend
```

## API Endpoints

### Core Endpoints

- `POST /passport` - Create a cultural passport
- `GET /passport/{user_id}` - Retrieve passport data
- `POST /analyze/vibrational` - Analyze vibrational signature
- `POST /archetype` - Identify archetypal patterns
- `POST /talent` - Profile talents
- `POST /predict` - Generate predictions

### Information Endpoints

- `GET /solfeggio` - Get Solfeggio frequency information
- `GET /archetypes` - Get archetype catalog
- `GET /talents` - Get talent categories
- `GET /analysis/history/{user_id}` - Get analysis history

## Example Usage

### Create a Passport

```bash
curl -X POST http://localhost:8000/passport \
  -H "Content-Type: application/json" \
  -d '{
    "user_id": "usr_001",
    "name": "Test User",
    "birth_date": "1990-01-01"
  }'
```

### Analyze Vibrational Signature

```bash
curl -X POST http://localhost:8000/analyze/vibrational \
  -H "Content-Type: application/json" \
  -d '{
    "user_id": "usr_001",
    "signal_data": [0.1, 0.2, 0.15, 0.3, 0.25],
    "analysis_type": "standard"
  }'
```

## Architecture

### 5-Layer System

1. **Vibrational Layer**: Signal processing and frequency analysis
2. **Archetypal Layer**: Pattern recognition and personality profiling
3. **Talent Layer**: Multiple intelligence assessment
4. **Cultural Layer**: Context and preference integration
5. **Predictive Layer**: Future state modeling

### Technologies

- **FastAPI**: Modern async web framework
- **SQLAlchemy**: Database ORM
- **NumPy/SciPy**: Signal processing
- **NetworkX**: Graph-based archetype modeling
- **Scikit-learn**: ML foundations (POC stubs)

## Development

### Database

POC uses SQLite. Schema includes:
- `profiles`: User cultural passports
- `analysis_history`: Historical analysis records

Initialize database:
```python
from app.db import init_db
init_db()
```

### Adding New Services

1. Create service module in `app/services/`
2. Implement core functions
3. Add endpoint in `app/main.py`
4. Update documentation

## TODO

- [ ] Add authentication and authorization
- [ ] Implement ML models for predictions
- [ ] Add WebSocket support for real-time analysis
- [ ] Migrate to PostgreSQL for production
- [ ] Add comprehensive error handling
- [ ] Implement rate limiting
- [ ] Add API versioning
- [ ] Integrate with external data sources
- [ ] Add caching layer
- [ ] Implement batch processing

## License

MIT + Nexus Ethical Clauses (see repository LICENSE)

## Author

Comandante Hebron Nexus (Helyton Renato Gonçalves Ronchi)

## Contact

- Email: deegp.nini@gmail.com
- Repository: https://github.com/deegpnini/TriNyTy-D7D-Nexus-GuardiaN
