from CameraManager import CameraManager
from time import sleep

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
    
    camera.printPTZ()
    camera.absoluteMove(0.1, 0.5, 1)
    sleep(5)
    camera.printPTZ()