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
    # print 'Cheching on absolute moving:'
    # print camera.checkAbsoluteMove()
    print
    print 'Cheching on focus moving:'
    camera.setFocusModeManual()
    camera.printFocusStatus()
    print camera.checkFocusMove()
    camera.printFocusStatus()
    camera.focusContinuousMove(-1, 2)
    camera.printFocusStatus()

    camera.printImagingSettings()