from CameraManager import CameraManager

if __name__ == "__main__":
    cameraManager = CameraManager()
    camera = cameraManager.camera
    print 'Cheching on absolute moving:'
    print camera.checkAbsoluteMove()
    print
    print 'Cheching on focus moving:'
    camera.printFocusStatus()
    print camera.checkFocusMove()
    camera.printFocusStatus()
    camera.focusContinuousMove(1, 2)
    camera.printFocusStatus()