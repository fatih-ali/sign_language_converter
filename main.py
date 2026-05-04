from fastapi import FastAPI, File, UploadFile
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from ultralytics import YOLO
import numpy as np
import cv2
import os

app = FastAPI()

# Load model once at startup
model = YOLO("best_v4.pt")

# Mount static folder
app.mount("/static", StaticFiles(directory="static"), name="static")

# Serve frontend properly
@app.get("/")
async def root():
    return FileResponse(os.path.join("static", "index.html"))

# Detection API
@app.post("/detect")
async def detect(file: UploadFile = File(...)):
    contents = await file.read()

    # Convert image bytes to OpenCV format
    nparr = np.frombuffer(contents, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

    # Run model
    results = model.predict(img, conf=0.5, verbose=False)

    detections = []
    for r in results:
        for box in r.boxes:
            cls_id = int(box.cls[0])
            conf = float(box.conf[0])
            x1, y1, x2, y2 = map(int, box.xyxy[0])

            detections.append({
                "sign": model.names[cls_id],
                "confidence": round(conf * 100),
                "box": [x1, y1, x2, y2]
            })

    return {"detections": detections}