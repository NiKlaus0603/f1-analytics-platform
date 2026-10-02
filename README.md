# F1 Analytics Platform

An AI-powered Formula 1 analytics platform for processing race data, telemetry, weather, tyre strategy, and historical performance to support live race analysis and predictive modeling.

## Project Goals

The platform is being built to:

- Ingest Formula 1 session, lap, telemetry, weather, tyre, and race data
- Process historical and live race-weekend information
- Engineer features for race-performance analysis
- Predict:
  - Pole position
  - Race winner
  - Podium finishes
  - Race strategy outcomes
- Analyze driver pace, tyre degradation, stint performance, and race evolution
- Provide an AI assistant capable of explaining race events and prediction changes
- Serve analytics and predictions through a FastAPI backend
- Power an interactive frontend dashboard

---

## Current Development Status

### Phase 1 — Backend Foundation ✅

The backend foundation is complete.

Implemented:

- FastAPI application
- Application configuration
- Logging configuration
- FastF1 integration
- FastF1 caching
- F1 session loading
- Historical race-data testing
- Driver and session data access
- Telemetry extraction testing

FastF1 successfully loads session information, race laps, driver data, track status, and telemetry.

---

### Phase 2 — Data Engine 🚧

The Data Engine is currently under development.

Implemented so far:

- Session data loader
- Session metadata extraction
- Driver extraction
- Race results extraction
- Weather-data access
- Raw lap-data extraction
- Lap-data cleaning
- Timing conversion to numeric seconds
- Driver-specific lap filtering
- Accurate-lap filtering
- Quick-lap filtering

Current test dataset:

**2026 Italian Grand Prix — Monza**

Example processed data:

```text
Raw laps:       1054
Accurate laps:   914
Quick laps:      872
```

The Data Engine currently processes information including:

- Driver
- Driver number
- Lap number
- Lap time
- Sector 1 time
- Sector 2 time
- Sector 3 time
- Tyre compound
- Tyre life
- Stint
- Track position
- Pit-in time
- Pit-out time
- Intermediate speeds
- Finish-line speed
- Speed trap
- Personal-best status
- FastF1 lap-accuracy status

---

## Planned Data Engine Architecture

```text
Formula 1 Data Sources
          │
          ▼
    Session Loader
          │
    ┌─────┼─────────┐
    ▼     ▼         ▼
   Laps Telemetry Weather
    │     │         │
    └─────┼─────────┘
          ▼
     Data Processors
          │
          ▼
   Feature Engineering
          │
          ▼
     Unified Data Engine
          │
    ┌─────┼────────────┐
    ▼     ▼            ▼
   API   ML Models   AI Assistant
```

---

## Planned Data Engine Modules

```text
backend/app/data_engine/
├── __init__.py
├── session_loader.py
├── lap_processor.py
├── telemetry_processor.py
├── weather_processor.py
├── tyre_processor.py
├── feature_engine.py
└── snapshot_builder.py
```

### Session Loader

Responsible for loading Formula 1 sessions and exposing:

- Session metadata
- Drivers
- Laps
- Weather
- Classification results

### Lap Processor

Responsible for cleaning and transforming raw lap data.

Current capabilities include:

- Timedelta-to-seconds conversion
- Numeric field normalization
- Accurate-lap filtering
- Quick-lap filtering
- Driver-specific lap extraction

Planned analytics include:

- Average race pace
- Median race pace
- Fastest lap
- Sector performance
- Pace delta
- Compound performance
- Stint performance
- Tyre-age performance

### Telemetry Processor

Planned telemetry processing includes:

- Speed
- Throttle
- Brake
- RPM
- Gear
- DRS
- Distance
- Time
- Acceleration characteristics

### Weather Processor

Planned weather features include:

- Air temperature
- Track temperature
- Humidity
- Pressure
- Wind speed
- Wind direction
- Rainfall

### Tyre Processor

Planned tyre analytics include:

- Compound usage
- Tyre age
- Stint duration
- Degradation
- Pit-stop behavior
- Compound performance comparison

### Feature Engine

The feature-engineering layer will generate derived analytics for machine-learning models, including:

- Driver pace
- Relative pace delta
- Sector performance
- Tyre degradation
- Stint performance
- Position evolution
- Pit strategy
- Weather impact
- DRS usage
- Race-state features

---

## ERS / Battery Modeling

Actual Formula 1 battery state-of-charge and detailed ERS deployment data are generally not directly available through standard public telemetry sources.

The platform will therefore keep:

```text
Observed telemetry
```

separate from:

```text
Estimated / derived telemetry
```

Future energy-related analytics may estimate:

- ERS deployment
- Energy recovery
- Approximate battery state
- High-deployment zones
- Overtake-mode-like behavior

Estimated values will always be explicitly identified as estimates.

---

## Technology Stack

### Backend

- Python
- FastAPI
- Uvicorn
- FastF1
- Pandas
- NumPy

### Machine Learning — Planned

- XGBoost
- LightGBM
- Random Forest
- Scikit-learn

### Data Layer — Planned

- PostgreSQL

### Frontend — Planned

- React

### Infrastructure — Planned

- Docker

### AI Layer — Planned

- Large Language Model integration
- Race-context retrieval
- Natural-language analytics assistant

---

## Project Structure

```text
f1-analytics-platform/
├── backend/
│   ├── __init__.py
│   └── app/
│       ├── __init__.py
│       ├── api/
│       ├── core/
│       │   ├── config.py
│       │   └── logging.py
│       ├── data_engine/
│       │   ├── __init__.py
│       │   ├── session_loader.py
│       │   ├── lap_processor.py
│       │   ├── telemetry_processor.py
│       │   ├── weather_processor.py
│       │   ├── tyre_processor.py
│       │   ├── feature_engine.py
│       │   └── snapshot_builder.py
│       ├── models/
│       ├── schemas/
│       ├── services/
│       │   └── f1_data_service.py
│       └── main.py
│
├── scripts/
│   ├── test_fastf1.py
│   ├── test_telemetry.py
│   ├── test_session_loader.py
│   └── test_lap_processor.py
│
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md
```

---

## Running the Project

Create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Start the FastAPI backend:

```bash
uvicorn backend.app.main:app --reload
```

The backend can then be accessed locally through the configured Uvicorn host and port.

---

## Data Engine Tests

Test the FastF1 integration:

```bash
python -m scripts.test_fastf1
```

Test telemetry:

```bash
python -m scripts.test_telemetry
```

Test the session loader:

```bash
python -m scripts.test_session_loader
```

Test the lap processor:

```bash
python -m scripts.test_lap_processor
```

---

## Development Roadmap

### Phase 1 — Foundation
- [x] FastAPI backend
- [x] Configuration
- [x] Logging
- [x] FastF1 integration
- [x] Caching
- [x] Session testing
- [x] Telemetry testing

### Phase 2 — Data Engine
- [x] Session loader
- [x] Lap processor
- [ ] Driver pace analytics
- [ ] Telemetry processor
- [ ] Weather processor
- [ ] Tyre / stint processor
- [ ] Feature engineering
- [ ] Race snapshots
- [ ] Live race-state processing

### Phase 3 — Historical Data Pipeline
- [ ] Multi-season ingestion
- [ ] Database persistence
- [ ] Data normalization
- [ ] Training datasets

### Phase 4 — Machine Learning
- [ ] Pole-position model
- [ ] Race-winner model
- [ ] Podium model
- [ ] Strategy model
- [ ] Hyperparameter optimization
- [ ] Model evaluation

### Phase 5 — Live Prediction Engine
- [ ] Live session ingestion
- [ ] Continuous feature updates
- [ ] Dynamic inference
- [ ] Prediction-change tracking

### Phase 6 — AI Race Assistant
- [ ] Natural-language race queries
- [ ] Prediction explanations
- [ ] Driver comparisons
- [ ] Race summaries
- [ ] Strategy explanations

### Phase 7 — Frontend
- [ ] React application
- [ ] Live timing dashboard
- [ ] Telemetry visualization
- [ ] Driver comparison
- [ ] Prediction dashboard
- [ ] AI assistant interface

---

## Vision

The finished platform will combine Formula 1 telemetry, historical race data, live race state, machine-learning predictions, strategy analytics, and generative AI into a single full-stack race intelligence platform.

The aim is to move beyond displaying race data and instead build a system capable of understanding how a race is evolving, quantifying driver and team performance, predicting likely outcomes, and explaining those predictions in natural language.
