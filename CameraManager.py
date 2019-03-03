from Camera import Camera
from NumPad import NumPad
from time import sleep
import random

class CameraManager:
    def __init__(self, address, port, login, password, wsdlFolder):
        self.address = address
        self.port = port
        self.login = login
        self.password = password
        self.wsdlFolder = wsdlFolder
        self.camera = self.initCamera()

    def initCamera(self):
        return Camera(self.address, self.port, self.login, self.password, self.wsdlFolder)

    def moveCameraByNumPad(self):
        numPad = NumPad()
        while(True):
            numPad.update()
            pressedKey = numPad.getPressedKey()
            if(pressedKey):
                sleep(0.5)
                if(pressedKey.value == 'z'):
                    numPad.decreaseSpeed()
                    continue
                if(pressedKey.value == 'x'):
                    numPad.increaseSpeed()
                    continue
                Velocity = numPad.getVelocity(pressedKey)

                speed = numPad.speed
                self.camera.continuousMove(Velocity.get('x', 0) * speed, Velocity.get('y', 0) * speed, Velocity.get('z', 0) * speed, 0)
            else:
                self.camera.stop()
            self.camera.printPTZ()

    def checkFocusMove(self):
        try:
            self.camera.setFocusModeManual()
            print 'Focus mode was switched to MANUAL'
        except Exception as e:
            print 'AutoFocusMode cannot be switched to MANUAL'

        try:
            self.camera.focusAbsoluteMove(random.uniform(-1, 1), 1)
            print 'Absolute focus move should be successful'
        except Exception as e:
            print 'Absolute focus move is not supported'

        try:
            self.camera.focusRelativeMove(random.uniform(-1, 1))
            print 'Relative focus move should be successful'
        except Exception as e:
            print 'Relative focus move is not supported'

        try:
            self.camera.focusContinuousMove(random.uniform(-1, 1))
            sleep(1)
            self.camera.focusContinuousMove(0)
            print 'Continuous focus move should be successful'
        except Exception as e:
            print 'Continuous focus move is not supported'


        
        
            