from CameraManager import CameraManager

def printFocusPosition(camera, word):
    try:
        print str(word) +' focus position: ' + str(camera.getFocusStatus().FocusStatus20.Position)
    except Exception as e:
        print 'Can\'t get focus position'

if __name__ == "__main__":
    # User data
    address = '192.168.15.43'
    port = 80
    login = 'admin'
    password = 'Supervisor'
    wsdlFolder = '/etc/onvif/wsdl/wsdl'

    # Program
    cameraManager = CameraManager(address, port, login, password, wsdlFolder)
    camera = cameraManager.camera
    print 'Cheching on absolute moving:'
    if(camera.checkAbsoluteMove()):
        print 'Absolute moving is supported'
    else:
        print 'Absolute moving is not supported'
    print 
    print 'Cheching on focus moving:'
    printFocusPosition(camera, 'Previous')
    cameraManager.checkFocusMove()
    printFocusPosition(camera, 'Current')

