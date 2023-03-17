from base_camera import BaseCamera
import cv2


class Camera(BaseCamera):        
    @staticmethod
    def frames():
        camera = cv2.VideoCapture("http://10.242.215.212:8000/stream.mjpg")
        while True:
            _, img = camera.read()
            yield cv2.imencode('.jpg', img)[1].tobytes()
