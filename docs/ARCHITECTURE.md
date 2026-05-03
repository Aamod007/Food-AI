# Food-AI Architecture

## Project Structure

```
Food-AI/
│
├── .github/                      # GitHub configuration
│   └── workflows/
│       └── ci.yml               # CI/CD pipeline
│
├── data/                        # Data directory
│   ├── raw/                     # Raw datasets
│   │   ├── food101_ingredients.csv
│   │   └── food101_ingredient_macros.csv
│   ├── processed/               # Processed datasets
│   │   ├── ingredients_macros_final.csv
│   │   └── converted_ingredients_grams.csv
│   └── samples/                 # Sample images
│       └── food.jpg
│
├── docs/                        # Documentation
│   ├── API.md                   # API documentation
│   ├── SETUP.md                 # Setup guide
│   └── ARCHITECTURE.md          # This file
│
├── frontend/                    # Web interface
│   ├── index.html              # Main HTML file
│   └── README.md               # Frontend documentation
│
├── myth/                        # Pre-trained model
│   ├── food_model.py           # Model wrapper class
│   ├── __init__.py
│   └── nateraw-food/           # Pre-trained weights
│       ├── config.json
│       ├── pytorch_model.bin
│       └── ...
│
├── Models/                      # Training checkpoints
│   └── phase2_best.pth         # Phase 2 trained model
│
├── notebooks/                   # Jupyter notebooks
│   └── README.md
│
├── scripts/                     # Utility scripts
│   ├── preprocessing/          # Data preprocessing
│   │   ├── assemble_all_macros.py
│   │   ├── fill_missing_macros.py
│   │   ├── find_missing_ingredients.py
│   │   ├── prune_zero_macros.py
│   │   └── __init__.py
│   └── __init__.py
│
├── src/                         # Source code
│   ├── api/                    # Backend API
│   │   ├── backend.py          # Flask application
│   │   └── __init__.py
│   ├── config/                 # Configuration
│   │   ├── config.py           # App configuration
│   │   └── __init__.py
│   ├── models/                 # Model code
│   │   ├── food_model.py       # Model architecture
│   │   ├── predict.py          # Prediction logic
│   │   └── __init__.py
│   ├── utils/                  # Utilities
│   │   ├── dataset.py          # Dataset utilities
│   │   ├── macros.py           # Macro calculations
│   │   └── __init__.py
│   └── __init__.py
│
├── tests/                       # Test suite
│   ├── test_model.py
│   └── __init__.py
│
├── .gitattributes              # Git LFS configuration
├── .gitignore                  # Git ignore rules
├── CONTRIBUTING.md             # Contribution guidelines
├── LICENSE                     # MIT License
├── README.md                   # Project overview
├── run.py                      # Main entry point
└── requirements.txt            # Python dependencies
```

## Component Overview

### 1. Data Layer (`data/`)
- **raw/**: Original datasets from Food-101
- **processed/**: Cleaned and transformed data
- **samples/**: Test images for validation

### 2. Model Layer (`src/models/`)
- **food_model.py**: CNN architecture for food classification
- **predict.py**: Inference pipeline

### 3. API Layer (`src/api/`)
- **backend.py**: Flask REST API
  - `/predict` - Food recognition endpoint
  - `/health` - Health check endpoint

### 4. Configuration (`src/config/`)
- Centralized configuration management
- Path definitions
- Model hyperparameters

### 5. Utilities (`src/utils/`)
- Dataset loading and preprocessing
- Nutritional macro calculations
- Helper functions

### 6. Scripts (`scripts/`)
- Data preprocessing pipelines
- Ingredient validation
- Macro assembly

### 7. Frontend (`frontend/`)
- HTML/CSS/JavaScript interface
- Image upload and preview
- Results visualization

### 8. Tests (`tests/`)
- Unit tests for models
- Integration tests for API
- Configuration validation

## Data Flow

```
User Upload Image
      ↓
Frontend (index.html)
      ↓
API Backend (backend.py)
      ↓
Prediction Module (predict.py)
      ↓
Food Model (food_model.py)
      ↓
Results + Nutritional Data
      ↓
Frontend Display
```

## Technology Stack

- **Backend**: Python, Flask
- **ML Framework**: PyTorch
- **Frontend**: HTML, CSS, JavaScript
- **Data Processing**: Pandas, NumPy
- **Testing**: pytest
- **CI/CD**: GitHub Actions

## Model Architecture

1. **Input**: 224x224 RGB image
2. **Backbone**: Pre-trained CNN (nateraw/food)
3. **Classification Head**: 101 food categories
4. **Output**: Class probabilities + nutritional info

## API Architecture

- RESTful design
- JSON responses
- Multipart form data for image uploads
- Error handling and validation

## Deployment Considerations

- Model served via Flask
- Can be containerized with Docker
- Scalable with gunicorn/nginx
- GPU support optional (CPU fallback)
