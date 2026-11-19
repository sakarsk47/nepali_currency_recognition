from flask import Flask, render_template, Response, request
import cv2
import tensorflow as tf
import numpy as np
import os
import threading
from PIL import Image, ImageEnhance
import pyttsx3
import time

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# Load the trained model once
model = tf.keras.models.load_model('cashRec.h5')

# Define note categories
classes = ['fifty', 'five', 'fivehundred', 'hundred', 'ten', 'thousand', 'twenty']

# Initialize pyttsx3 for playing audio
engine = pyttsx3.init()
engine.setProperty('volume', 1)

def play_audio(note):
    audio_file = f"audio/{note}.mp3"  # Ensure correct path
    if os.path.exists(audio_file):
        os.system(f"afplay {audio_file}")  # Use system command to play audio on macOS

tts_lock = threading.Lock()

def tts_backup(text):
    """Run text-to-speech safely without conflicts"""
    with tts_lock:
        engine.say(text)
        engine.runAndWait()

def process_audio(note):
    if os.path.exists(f"audio/{note}.mp3"):
        play_audio(note)
    else:
        threading.Thread(target=tts_backup, args=(note,)).start()

# Open webcam only when requested
cap = None

def start_camera():
    global cap
    if cap is None or not cap.isOpened():
        cap = cv2.VideoCapture(0)
        if not cap.isOpened():
            cap = None

def stop_camera():
    global cap
    if cap is not None and cap.isOpened():
        cap.release()
        cap = None

# Store last detected note to avoid repetitive announcements
last_prediction = None

def preprocess_frame(frame):
    image = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
    image = ImageEnhance.Contrast(image).enhance(1.5)
    image = ImageEnhance.Sharpness(image).enhance(2.0)
    image = image.resize((150, 150))
    img_array = np.array(image) / 255.0
    img_array = np.expand_dims(img_array, axis=0)
    return img_array

def is_note_present(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 50, 150)
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    return len(contours) > 5

def generate_frames():
    global last_prediction, cap
    start_camera()
    if cap is None:
        return
    
    while cap.isOpened():
        success, frame = cap.read()
        if not success:
            break
        frame = cv2.flip(frame, 1)
        if is_note_present(frame):
            processed_frame = preprocess_frame(frame)
            predictions = model.predict(processed_frame)
            confidence = np.max(predictions)
            index = np.argmax(predictions)
            prediction = classes[index]
            if confidence > 0.7:
                cv2.putText(frame, f"Note: {prediction} rupees ({confidence:.2f})", (50, 50),
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
                if prediction != last_prediction:
                    last_prediction = prediction
                    threading.Thread(target=process_audio, args=(prediction,)).start()
            else:
                last_prediction = None
        else:
            cv2.putText(frame, "No note detected", (50, 50),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
            last_prediction = None
        ret, buffer = cv2.imencode('.jpg', frame)
        frame_bytes = buffer.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/start_video')
def start_video():
    start_camera()
    return "Camera Started"

@app.route('/stop_video')
def stop_video():
    stop_camera()
    return "Camera Stopped"

@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return "No file part"
    file = request.files['file']
    if file.filename == '':
        return "No selected file"
    if file:
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filepath)
        img = tf.keras.preprocessing.image.load_img(filepath, target_size=(150, 150))
        img_array = tf.keras.preprocessing.image.img_to_array(img)/255.0
        img_array = np.expand_dims(img_array, axis=0)
        predictions = model.predict(img_array)
        index = np.argmax(predictions)
        prediction = classes[index]
        output = f"The Note is {prediction} rupees."
        threading.Thread(target=process_audio, args=(prediction,)).start()
        return output

if __name__ == '__main__':
    app.run(debug=True)
