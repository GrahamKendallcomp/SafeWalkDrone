from importlib import import_module
import os
from flask import Flask, render_template, Response

from camera import Camera

print(os.getcwd())
app = Flask(__name__)

def gen(camera):
    yield b'--frame\r\n'
    while True:
        frame = camera.get_frame()
        yield b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n--frame\r\n'

@app.route("/")
def home():
    return render_template("gps.html")

@app.route('/video_feed')
def video_feed():
    return Response(gen(Camera()), mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == "__main__":
    app.run(host="0.0.0.0", threaded = True)