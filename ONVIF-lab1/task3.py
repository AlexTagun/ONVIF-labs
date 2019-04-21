from CameraManager import CameraManager
from time import sleep

if __name__ == "__main__":
    # User data
    address = '192.168.15.43'
    port = 80
    login = 'alextagun'
    password = 'HSrdajML01pn'
    wsdlFolder = '/etc/onvif/wsdl/wsdl'

    # Program
    cameraManager = CameraManager(address, port, login, password, wsdlFolder)
    cameraManager.moveCameraByNumPad()