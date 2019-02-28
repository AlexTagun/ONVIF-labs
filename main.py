from onvif import ONVIFCamera
from time import sleep
from Camera import Camera

if __name__ == "__main__":
    camera = Camera()
    camera.printPTZ()
    # camera.performContinuousMove(1)
    # print camera.getPosition()
