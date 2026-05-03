"""Unit tests for model functionality."""

import unittest
import sys
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))


class TestFoodModel(unittest.TestCase):
    """Test cases for food classification model."""

    def setUp(self):
        """Set up test fixtures."""
        pass

    def test_model_import(self):
        """Test that model can be imported."""
        try:
            from models import food_model
            self.assertTrue(True)
        except ImportError:
            self.fail("Failed to import food_model")

    def test_predict_import(self):
        """Test that predict module can be imported."""
        try:
            from models import predict
            self.assertTrue(True)
        except ImportError:
            self.fail("Failed to import predict module")


class TestConfig(unittest.TestCase):
    """Test cases for configuration."""

    def test_config_import(self):
        """Test that config can be imported."""
        try:
            from config import config
            self.assertTrue(True)
        except ImportError:
            self.fail("Failed to import config")

    def test_paths_exist(self):
        """Test that configured paths exist."""
        from config.config import BASE_DIR, DATA_DIR, MODELS_DIR
        
        self.assertTrue(BASE_DIR.exists(), "Base directory should exist")
        self.assertTrue(DATA_DIR.exists(), "Data directory should exist")
        self.assertTrue(MODELS_DIR.exists(), "Models directory should exist")


if __name__ == "__main__":
    unittest.main()
