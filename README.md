# YOLOv8 Object Detection Web App

## Description
This is a simple web app using Flask and YOLOv8 to detect objects in uploaded images.

## How to Run Locally

1. Install dependencies:
```
pip install -r requirements.txt
```

2. Run the Flask app:
```
python app.py
```

3. Open http://localhost:5000 in your browser.

## Falcon Integration Plan

To ensure the YOLOv8 model remains accurate, we will use Falcon (an open-source LLM) to:
- Analyze detection logs
- Identify frequent misclassifications
- Recommend retraining schedules
