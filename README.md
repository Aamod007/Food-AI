# Food-AI 🍔🤖

An AI-powered food recognition and nutritional analysis system using deep learning.

## 📁 Project Structure

```
Food-AI/
├── src/                          # Source code
│   ├── models/                   # Model architectures
│   ├── api/                      # Backend API
│   ├── utils/                    # Utility functions
│   └── config/                   # Configuration files
├── data/                         # Datasets
│   ├── raw/                      # Raw data files
│   ├── processed/                # Processed datasets
│   └── samples/                  # Sample images
├── myth/                         # Pre-trained model (nateraw/food)
│   ├── food_model.py            # Model wrapper
│   └── nateraw-food/            # Pre-trained weights
├── Models/                       # Trained model checkpoints
│   └── phase2_best.pth          # Phase 2 model
├── scripts/                      # Data processing scripts
│   └── preprocessing/            # Data preprocessing
├── notebooks/                    # Jupyter notebooks
├── frontend/                     # Web interface
├── tests/                        # Unit tests
├── docs/                         # Documentation
├── .github/                      # GitHub workflows
├── run.py                        # Main entry point
└── requirements.txt              # Python dependencies
```

## 🚀 Features

- **Food Recognition**: Classify 101 different food categories
- **Nutritional Analysis**: Get detailed macro and micronutrient information
- **REST API**: Easy-to-use Flask backend
- **Web Interface**: Interactive UI for food recognition
- **Data Processing**: Comprehensive ingredient and macro datasets

## 🛠️ Installation

```bash
# Clone the repository
git clone https://github.com/Aamod007/Food-AI.git
cd Food-AI

# Create virtual environment
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

## 📊 Usage

### Running the API Server

```bash
python run.py
```

Or directly:

```bash
python src/api/backend.py
```

### Making Predictions

```python
from src.models.predict import predict_food

result = predict_food('path/to/food/image.jpg')
print(result)
```

## 🧪 Model Performance

- **Architecture**: CNN-based food classifier
- **Training Dataset**: Food-101
- **Accuracy**: [Add your metrics]

## 📝 License

MIT License

## 👥 Contributors

- Aamod007

## 🙏 Acknowledgments

- Food-101 Dataset
- Pre-trained models from nateraw
