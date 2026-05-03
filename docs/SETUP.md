# Setup Guide

## Prerequisites

- Python 3.8 or higher
- pip package manager
- Virtual environment (recommended)

## Installation Steps

### 1. Clone the Repository

```bash
git clone https://github.com/Aamod007/Food-AI.git
cd Food-AI
```

### 2. Create Virtual Environment

**Windows:**
```bash
python -m venv .venv
.venv\Scripts\activate
```

**Linux/Mac:**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Download Model Weights

The model weights are tracked with Git LFS. Make sure you have Git LFS installed:

```bash
git lfs install
git lfs pull
```

### 5. Verify Installation

```bash
python -c "import torch; print(torch.__version__)"
```

## Running the Application

### Start the API Server

```bash
python src/api/backend.py
```

The server will start at `http://localhost:5000`

### Open the Web Interface

Open `frontend/index.html` in your browser or serve it with:

```bash
cd frontend
python -m http.server 8000
```

Then navigate to `http://localhost:8000`

## Testing

Run the test suite:

```bash
pytest tests/
```

## Troubleshooting

### CUDA/GPU Issues

If you encounter GPU-related errors, install the CPU version of PyTorch:

```bash
pip install torch torchvision --index-url https://download.pytorch.org/whl/cpu
```

### Module Import Errors

Make sure you're in the project root directory and the virtual environment is activated.

### Model Loading Errors

Ensure the model checkpoint exists at `models/checkpoints/phase2_best.pth`
