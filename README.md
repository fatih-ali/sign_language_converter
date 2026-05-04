# Sign Language Converter

This project is a real-time sign language detection system that converts hand gestures into text and speech using a trained deep learning model.

The application uses a webcam to capture live video, processes frames using a YOLO-based model, and displays the detected sign on screen along with voice output.

---

## Features

- Real-time sign detection using webcam  
- Text output of detected signs  
- Voice output for recognized gestures  
- Sentence formation from multiple signs  
- Fast and responsive detection  
- Simple and clean user interface  

---

## Technologies Used

Frontend:
- HTML
- CSS
- JavaScript

Backend:
- FastAPI

Machine Learning:
- YOLOv8 (Ultralytics)

Libraries:
- OpenCV
- NumPy

---

## Project Structure

sign_language_converter/
│
├── main.py  
├── best_v4.pt  
├── requirements.txt  
└── static/  
    └── index.html  

---

## How to Run

1. Clone the repository

2. Install dependencies:
   pip install -r requirements.txt

3. Run the server:
   python -m uvicorn main:app --reload

4. Open in browser:
   http://127.0.0.1:8000

---

## How It Works

The system captures frames from the webcam and sends them to the backend.  
The YOLO model processes each frame and predicts the sign.  
The result is returned to the frontend, where it is displayed and spoken aloud.  
A short delay mechanism is used to avoid repeated detection of the same sign.

---

## Current Limitations

- Some similar signs (like yes and no) may not be fully accurate  
- Performance depends on lighting and camera quality  
- Runs locally and is not deployed yet  

---

## Future Improvements

- Improve model accuracy with better dataset  
- Add support for more signs  
- Deploy as a web application  
- Add multi-language voice output  

---

## Author

Fatih Ali , Aadhiv MK, Abdul Shaheer
