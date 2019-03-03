from onvif import ONVIFCamera
from time import sleep
from Camera import Camera
from CameraManager import CameraManager

if __name__ == "__main__":
    # User data
    address = '192.168.15.42'
    port = 80
    login = 'alextagun'
    password = 'HSrdajML01pn'
    wsdlFolder = '/etc/onvif/wsdl/wsdl'

    # Program
    cameraManager = CameraManager(address, port, login, password, wsdlFolder)
    camera = cameraManager.camera
    while(True):
        camera.printPTZ()
        sleep(0.1)