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
                Velocity = numPad.getVelocity(pressedKey)
                self.camera.continuousMove(Velocity.get('x', 0), Velocity.get('y', 0), Velocity.get('z', 0), 0)
            else:
                self.camera.stop()
            self.camera.printPTZ()
            sleep(0.3)