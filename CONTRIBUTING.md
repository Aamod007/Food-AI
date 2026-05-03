# Contributing to Food-AI

Thank you for your interest in contributing to Food-AI! 🎉

## How to Contribute

### Reporting Bugs

1. Check if the bug has already been reported in Issues
2. Create a new issue with a clear title and description
3. Include steps to reproduce, expected behavior, and actual behavior
4. Add relevant screenshots or error messages

### Suggesting Features

1. Check if the feature has already been suggested
2. Create a new issue with the "enhancement" label
3. Clearly describe the feature and its benefits
4. Provide examples of how it would work

### Pull Requests

1. Fork the repository
2. Create a new branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Write or update tests as needed
5. Ensure all tests pass
6. Commit your changes (`git commit -m 'Add amazing feature'`)
7. Push to your branch (`git push origin feature/amazing-feature`)
8. Open a Pull Request

## Development Setup

```bash
# Clone your fork
git clone https://github.com/YOUR_USERNAME/Food-AI.git
cd Food-AI

# Create virtual environment
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Install development dependencies
pip install pytest black flake8 isort
```

## Code Style

- Follow PEP 8 guidelines
- Use Black for code formatting: `black src/`
- Use isort for import sorting: `isort src/`
- Run flake8 for linting: `flake8 src/`

## Testing

Run tests before submitting:

```bash
pytest tests/
```

## Commit Messages

- Use clear and descriptive commit messages
- Start with a verb in present tense (Add, Fix, Update, etc.)
- Keep the first line under 50 characters
- Add detailed description if needed

Examples:
- `Add ingredient search functionality`
- `Fix model loading error on Windows`
- `Update API documentation`

## Questions?

Feel free to open an issue for any questions or concerns!
