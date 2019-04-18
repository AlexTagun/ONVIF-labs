from Camera import Camera
from time import sleep
import random
import math
import urllib2

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

    def downloadPreviewImage(self):
        previewUri = self.camera.getPreview().Uri
        # print previewUri
        manager = urllib2.HTTPPasswordMgrWithDefaultRealm()
        manager.add_password(None, previewUri, self.login, self.password)

        #Create an authentication handler using the password manager
        auth = urllib2.HTTPBasicAuthHandler(manager)

        #Create an opener that will replace the default urlopen method on further calls
        opener = urllib2.build_opener(auth)
        urllib2.install_opener(opener)

        #Here you should access the full url you wanted to open
        image_on_web = urllib2.urlopen(previewUri)
        buf = image_on_web.read()
        # print buf
        filename = "img.jpg"
        downloaded_image = open(filename, "wb")
        downloaded_image.write(buf)
        downloaded_image.close()
        image_on_web.close()
            