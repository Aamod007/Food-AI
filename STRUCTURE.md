# Food-AI Project Structure

## 📁 Complete Directory Layout

```
Food-AI/
│
├── 📂 src/                          # Source Code
│   ├── 📂 api/                      # Backend API
│   │   ├── backend.py              # Flask REST API server
│   │   └── __init__.py
│   │
│   ├── 📂 config/                   # Configuration
│   │   ├── config.py               # App settings & paths
│   │   └── __init__.py
│   │
│   ├── 📂 models/                   # Model Code
│   │   ├── food_model.py           # Model architecture
│   │   ├── predict.py              # Prediction pipeline
│   │   └── __init__.py
│   │
│   ├── 📂 utils/                    # Utilities
│   │   ├── dataset.py              # Dataset utilities
│   │   ├── macros.py               # Macro calculations
│   │   └── __init__.py
│   │
│   └── __init__.py
│
├── 📂 data/                         # Datasets
│   ├── 📂 raw/                      # Original data
│   │   ├── food101_ingredients.csv
│   │   └── food101_ingredient_macros.csv
│   │
│   ├── 📂 processed/                # Cleaned data
│   │   ├── converted_ingredients_grams.csv
│   │   └── ingredients_macros_final.csv
│   │
│   └── 📂 samples/                  # Test images
│       └── food.jpg
│
├── 📂 myth/                         # Pre-trained Model
│   ├── food_model.py               # Model wrapper
│   ├── __init__.py
│   └── 📂 nateraw-food/            # Pre-trained weights
│       ├── config.json
│       ├── pytorch_model.bin
│       ├── preprocessor_config.json
│       └── ...
│
├── 📂 Models/                       # Training Checkpoints
│   └── phase2_best.pth             # Phase 2 model
│
├── 📂 scripts/                      # Processing Scripts
│   ├── 📂 preprocessing/
│   │   ├── assemble_all_macros.py
│   │   ├── fill_missing_macros.py
│   │   ├── find_missing_ingredients.py
│   │   ├── prune_zero_macros.py
│   │   └── __init__.py
│   └── __init__.py
│
├── 📂 frontend/                     # Web Interface
│   ├── index.html                  # Main UI
│   └── README.md
│
├── 📂 notebooks/                    # Jupyter Notebooks
│   └── README.md
│
├── 📂 tests/                        # Test Suite
│   ├── test_model.py
│   └── __init__.py
│
├── 📂 docs/                         # Documentation
│   ├── API.md                      # API reference
│   ├── SETUP.md                    # Setup guide
│   └── ARCHITECTURE.md             # Architecture docs
│
├── 📄 run.py                        # Main entry point
├── 📄 requirements.txt              # Dependencies
├── 📄 README.md                     # Project overview
├── 📄 LICENSE                       # MIT License
├── 📄 CONTRIBUTING.md               # Contribution guide
├── 📄 .gitignore                    # Git ignore rules
└── 📄 .gitattributes                # Git LFS config

```

## 🎯 Key Improvements

### ✅ Modular Structure
- **src/** - All source code organized by function
- **data/** - Clear separation of raw vs processed data
- **scripts/** - Preprocessing utilities in dedicated folder

### ✅ Professional Layout
- **docs/** - Comprehensive documentation
- **tests/** - Unit test framework
- **frontend/** - Separate UI directory

### ✅ Easy Navigation
- **run.py** - Single entry point
- **README.md** - Clear project overview
- **CONTRIBUTING.md** - Contribution guidelines

### ✅ Preserved Structure
- **myth/** - Pre-trained model kept intact
- **Models/** - Training checkpoints preserved

## 🚀 Quick Start

```bash
# Run the application
python run.py

# Or directly
python src/api/backend.py

# Run tests
pytest tests/

# Open frontend
open frontend/index.html
```

## 📦 What Goes Where?

| Type | Location | Purpose |
|------|----------|---------|
| API code | `src/api/` | Backend server |
| Model code | `src/models/` | ML models |
| Utilities | `src/utils/` | Helper functions |
| Config | `src/config/` | Settings |
| Raw data | `data/raw/` | Original datasets |
| Processed data | `data/processed/` | Cleaned datasets |
| Scripts | `scripts/preprocessing/` | Data processing |
| Tests | `tests/` | Unit tests |
| Docs | `docs/` | Documentation |
| Frontend | `frontend/` | Web UI |
| Notebooks | `notebooks/` | Jupyter notebooks |

## 🔧 Configuration

All paths are configured in `src/config/config.py`:
- Data directories
- Model paths
- API settings
- Image settings

## 📝 Notes

- The **myth/** folder contains the pre-trained nateraw/food model
- The **Models/** folder contains custom training checkpoints
- All imports updated to reflect new structure
- Git LFS configured for large model files
