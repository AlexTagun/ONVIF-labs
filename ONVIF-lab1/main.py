from onvif import ONVIFCamera
from time import sleep
import math
from Camera import Camera
from NumPad import NumPad
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
    cameraManager.rotareOneCircle()