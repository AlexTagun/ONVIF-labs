from CameraManager import CameraManager

if __name__ == "__main__":

    cameraManager = CameraManager()
    camera = cameraManager.initCamera(0)

    cameraManager.correctImageSettings(camera)
