"""Configuration settings for Food-AI application."""

import os
from pathlib import Path

# Base directory
BASE_DIR = Path(__file__).resolve().parent.parent.parent

# Data directories
DATA_DIR = BASE_DIR / "data"
RAW_DATA_DIR = DATA_DIR / "raw"
PROCESSED_DATA_DIR = DATA_DIR / "processed"
SAMPLES_DIR = DATA_DIR / "samples"

# Model directories
MODELS_DIR = BASE_DIR / "models"
CHECKPOINTS_DIR = MODELS_DIR / "checkpoints"
PRETRAINED_DIR = MODELS_DIR / "pretrained"

# Model settings
MODEL_NAME = "phase2_best.pth"
MODEL_PATH = CHECKPOINTS_DIR / MODEL_NAME
PRETRAINED_MODEL_PATH = PRETRAINED_DIR / "nateraw-food"

# API settings
API_HOST = "0.0.0.0"
API_PORT = 5000
DEBUG = True

# Image settings
IMAGE_SIZE = (224, 224)
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

# Dataset files
INGREDIENTS_FILE = RAW_DATA_DIR / "food101_ingredients.csv"
MACROS_FILE = RAW_DATA_DIR / "food101_ingredient_macros.csv"
PROCESSED_MACROS_FILE = PROCESSED_DATA_DIR / "ingredients_macros_final.csv"
CONVERTED_INGREDIENTS_FILE = PROCESSED_DATA_DIR / "converted_ingredients_grams.csv"

# Food categories (Food-101 dataset)
NUM_CLASSES = 101

# Training settings
BATCH_SIZE = 32
LEARNING_RATE = 0.001
EPOCHS = 50
