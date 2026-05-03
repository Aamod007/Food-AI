# Food-AI API Documentation

## Overview

The Food-AI API provides endpoints for food recognition and nutritional analysis.

## Base URL

```
http://localhost:5000
```

## Endpoints

### 1. Predict Food

**Endpoint:** `/predict`  
**Method:** `POST`  
**Content-Type:** `multipart/form-data`

**Request:**
```bash
curl -X POST http://localhost:5000/predict \
  -F "image=@/path/to/food/image.jpg"
```

**Response:**
```json
{
  "success": true,
  "prediction": {
    "food_name": "pizza",
    "confidence": 0.95,
    "ingredients": ["flour", "tomato", "cheese", "basil"],
    "macros": {
      "calories": 266,
      "protein": 11.4,
      "carbs": 33.0,
      "fat": 10.0
    }
  }
}
```

### 2. Health Check

**Endpoint:** `/health`  
**Method:** `GET`

**Response:**
```json
{
  "status": "healthy",
  "version": "1.0.0"
}
```

## Error Responses

### 400 Bad Request
```json
{
  "success": false,
  "error": "No image provided"
}
```

### 500 Internal Server Error
```json
{
  "success": false,
  "error": "Prediction failed"
}
```

## Rate Limiting

Currently no rate limiting is implemented.

## Authentication

Currently no authentication is required.
