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

    try:
            camera.setFocusModeManual()
            print 'Focus mode was switched to MANUAL'
    except Exception as e:
        print 'AutoFocusMode cannot be switched to MANUAL'

    try:
        self.camera.focusAbsoluteMove(random.uniform(-1, 1), 1)
        print 'Camera was moved by absolute way'
    except Exception as e:
        print 'Absolute focus move is not supported'

    try:
            self.camera.focusRelativeMove(random.uniform(-1, 1))
            print 'Camera was moved by relative way'
    except Exception as e:
        print 'Relative focus move is not supported'
