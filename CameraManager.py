from Camera import Camera
from NumPad import NumPad
from time import sleep

class CameraManager:
    def __init__(self, address, port, login, password, wsdlFolder):
        self.address = '192.168.15.42'
        self.port = 80
        self.login = 'admin'
        self.password = 'Supervisor'
        self.wsdlFolder = '/etc/onvif/wsdl/wsdl'
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
            