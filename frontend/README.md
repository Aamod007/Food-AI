# Frontend

Web interface for Food-AI food recognition system.

## Files

- **index.html** - Main web interface

## Features

- Image upload for food recognition
- Real-time predictions
- Nutritional information display
- Responsive design

## Running

### Option 1: Direct File Access
Simply open `index.html` in your web browser.

### Option 2: Local Server
```bash
cd frontend
python -m http.server 8000
```

Then navigate to `http://localhost:8000`

## API Configuration

Make sure the backend API is running at `http://localhost:5000` before using the frontend.

Update the API endpoint in `index.html` if your backend runs on a different port.
