#!/usr/bin/env python
"""Main entry point for Food-AI application."""

import sys
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent / "src"))

from api.backend import main

if __name__ == "__main__":
    main()
