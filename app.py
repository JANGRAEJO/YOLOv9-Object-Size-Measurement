from flask import Flask, render_template, Response
import cv2
from yolo_midas_utils import detect_and_measure
import time

app = Flask(__name__)
camera = cv2.VideoCapture(0)


def generate_frames():
    while True:
        success, frame = camera.read()
        if not success:
            print("❌ [ERROR] Failed to read from camera")
            time.sleep(1)
            continue
        annotated = detect_and_measure(frame)
        ret, buffer = cv2.imencode('.jpg', annotated)
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + buffer.tobytes() + b'\r\n')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(debug=True)
