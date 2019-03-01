from onvif import ONVIFCamera
from time import sleep
from Camera import Camera

if __name__ == "__main__":
    camera = Camera()
    while(True):
        camera.printPTZ()
        sleep(0.1)