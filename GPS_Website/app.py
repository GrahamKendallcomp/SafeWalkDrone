from flask import Flask, render_template, Response
from os import getcwd
import cv2

app = Flask(__name__)

class Camera(object):
    def __init__(self):
        self.camera = cv2.VideoCapture("http://10.242.215.212:8000/stream.mjpg")
        success, self.frame = self.camera.read()
    
    def __del__(self):
        self.camera.release()

    def get_frame(self):
        return self.frame

def gen_frames(camera):  
    while True:
        ret, buffer = cv2.imencode('.jpg', camera.get_frame())
        frame = buffer.tobytes()
        yield (b'--frame\r\n'
                b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route("/")
def home():
    return render_template("gps.html")

@app.route('/video_feed')
def video_feed():
    return Response(gen_frames(Camera()), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == "__main__":
    app.run(host="0.0.0.0")