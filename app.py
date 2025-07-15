from flask import Flask, render_template, request
from PIL import Image
import os
import torch
import uuid

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Load YOLOv8 model
model = torch.hub.load('ultralytics/yolov5', 'custom', path='yolov8_model.pt')

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        file = request.files['image']
        if file:
            filepath = os.path.join(UPLOAD_FOLDER, str(uuid.uuid4()) + file.filename)
            file.save(filepath)

            # Inference
            results = model(filepath)
            results.save(save_dir=UPLOAD_FOLDER)

            result_img_path = os.path.join(UPLOAD_FOLDER, os.path.basename(filepath))
            return render_template('index.html', result_img=result_img_path)

    return render_template('index.html', result_img=None)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
