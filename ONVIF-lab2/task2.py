from CameraManager import CameraManager
import threading
import time

def correctImageSettings(camera, cameraManager):
    cameraManager.correctImageSettings(camera)

if __name__ == "__main__":

    cameraManager = CameraManager()
    camera42 = cameraManager.initCamera(0)
    camera43 = cameraManager.initCamera(1)

    threading.Thread(target=correctImageSettings, args=(camera42, cameraManager,)).start()
    threading.Thread(target=correctImageSettings, args=(camera43, cameraManager,)).start()
    