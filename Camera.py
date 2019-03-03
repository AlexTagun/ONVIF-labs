from onvif import ONVIFCamera
from time import sleep
import random

class Camera:
    def __init__(self, address, port, login, password, wsdlFolder):
        # IP camera initialization
        print 'IP camera initialization'
        self.mycam = ONVIFCamera(address, port, login, password, wsdlFolder)
        # print self.mycam.devicemgmt.GetDeviceInformation()

        print 'Connected to ONVIF camera'

        # Create media service object
        self.media = self.mycam.create_media_service()
        print 'Created media service object'
        print
        # Get target profile
        self.media_profile = self.media.GetProfiles()[0]
        # Use the first profile and Profiles have at least one
        
        # Creating PTZ service
        self.ptz = self.mycam.create_ptz_service()
        # get PTZ status
        self.statusPTZ = self.ptz.GetStatus({'ProfileToken': self.media_profile._token})
        
        nodes = self.ptz.GetNodes()
        nodetoken = nodes[0]._token
        self.node = nodes[0]
        # print node._token
        # print self.ptz.GetNode({'NodeToken': node._token})

        # Getting available PTZ services
        request = self.ptz.create_type('GetServiceCapabilities')
        service_capabilities = self.ptz.GetServiceCapabilities(request)
        # print("Service capabilities: " + str(service_capabilities))

        # Getting PTZ configuration options for getting option ranges
        request = self.ptz.create_type('GetConfigurationOptions')
        request.ConfigurationToken = self.media_profile.PTZConfiguration._token
        ptz_configuration_options = self.ptz.GetConfigurationOptions(request)
        # print ptz_configuration_options

        # Getting needed requests

        # Continuous move
        self.requestContinuousMove = self.ptz.create_type('ContinuousMove')
        self.requestContinuousMove.ProfileToken = self.media_profile._token
        # print self.request_continuous_move

        # Absolute move
        self.requestAbsoluteMove = self.ptz.create_type("AbsoluteMove")
        self.requestAbsoluteMove.ProfileToken = self.media_profile._token

        # Relative move
        self.requestRelativeMove = self.ptz.create_type('RelativeMove')
        self.requestRelativeMove.ProfileToken = self.media_profile._token

        # Stop move
        self.requestStop = self.ptz.create_type('Stop')
        self.requestStop.ProfileToken = self.media_profile._token
        # print self.request_stop

        # Creating imaging service
        self.imaging = self.mycam.create_imaging_service()
        # print self.imaging

        # Getting available imaging services
        request = self.imaging.create_type('GetServiceCapabilities')
        service_capabilities = self.ptz.GetServiceCapabilities(request)
        # print service_capabilities

        # Getting imaging status
        self.imagingStatus = self.imaging.GetStatus({'VideoSourceToken': self.media_profile.VideoSourceConfiguration.SourceToken})
        request = self.imaging.create_type("GetServiceCapabilities")
        imaging_service_capabilities = self.ptz.GetServiceCapabilities(request)
        # print imaging_service_capabilities

        # Create request for setting imaging settings
        self.requestSetImagingSettings = self.imaging.create_type("SetImagingSettings")
        self.requestSetImagingSettings.VideoSourceToken = self.media_profile.VideoSourceConfiguration.SourceToken

    # get camera position in this moment
    def getStatus(self):
        return self.ptz.GetStatus({'ProfileToken': self.media_profile._token})

    def stop(self):
        self.requestStop.PanTilt = True
        self.requestStop.Zoom = True
        self.ptz.Stop(self.requestStop)
        # print('Stopping camera')
    
    # Continuous move (xSpeed, ySpeed, zoomSpeed, timeout)
    def continuousMove(self, x, y, z, timeout):
        # Start continuous move
        # status = self.ptz.GetStatus({"ProfileToken": self.media_profile._token})
        # status.Position.PanTilt[0] = str(x)
        self.requestContinuousMove.Velocity.PanTilt._x = str(x)
        self.requestContinuousMove.Velocity.PanTilt._y = str(y)
        self.requestContinuousMove.Velocity.Zoom._x = str(z)
        # self.requestContinuousMove[1].PanTilt[1] = str(y)
        # self.requestContinuousMove[1].Zoom[0] = str(z)
        # print self.requestContinuousMove.Velocity.PanTilt
        # print status.Position.PanTilt._x
        # print self.requestContinuousMove
        # print self.requestContinuousMove
        self.ptz.ContinuousMove(self.requestContinuousMove)

        # Wait a certain time
        sleep(timeout)

        # # Stop continuous move
        # self.stop()

        # # print('Continuous move completed')
        # sleep(2)

    # Absolute move
    def absoluteMove(self, x, y, z):
        self.requestAbsoluteMove.Position.PanTilt._x = str(x)
        self.requestAbsoluteMove.Position.PanTilt._y = str(y)
        self.requestAbsoluteMove.Position.Zoom._x = str(z)
        self.ptz.AbsoluteMove(self.requestAbsoluteMove)

    # Print camera position x, y and zoom
    def printPTZ(self):
        position = self.getStatus()[0]
        print 'x = {0:2f} y = {1:3f} z = {2:4f}'.format(position.PanTilt[1], position.PanTilt[0], position.Zoom[0])

    # Get focus status
    def getFocusStatus(self):
        return self.imaging.GetStatus({'VideoSourceToken': self.media_profile.VideoSourceConfiguration.SourceToken})
    
    # Focus continuous moving 
    def focusContinuousMove(self, speed, timeout):
        self.requestFocusChange = self.createFocusMoveRequest()
        self.requestFocusChange.Focus = {
            "Continuous": {
                "Speed": speed
            }
        }
        self.imaging.Move(self.requestFocusChange)
        sleep(timeout)
        self.stop()
        sleep(2)

    # Focus absolute moving 
    def focusAbsoluteMove(self, position, speed):
        self.requestFocusChange = self.createFocusMoveRequest()
        self.requestFocusChange.Focus.Absolute.Position = float(position)
        self.requestFocusChange.Focus.Absolute.Speed = float(speed)
        self.imaging.Move(self.requestFocusChange)
        sleep(2)

    #Focus relative moving
    def focusRelativeMove(self, speed):
        self.requestFocusChange = self.createFocusMoveRequest()
        self.requestFocusChange.Focus.Relative.Speed = speed
        self.imaging.Move(self.requestFocusChange)
        sleep(2)

    # Create pattern of focus move request
    def createFocusMoveRequest(self)
        requestFocusChange = self.imaging.create_type("Move")
        requestFocusChange.VideoSourceToken = self.media_profile.VideoSourceConfiguration.SourceToken
        return requestFocusChange

    
    
    # print supported PTZ spaces and focus status
    def printData(self):
        print self.node.SupportedPTZSpaces
        print '=========================='
        print self.imagingStatus

    # functions for cheching camera opportunities
    # return True if camera supports absolute moving, else false
    def checkAbsoluteMove(self):
        position = self.getStatus()
        self.absoluteMove(random.uniform(-1, 1), random.uniform(-1, 1), random.uniform(0, 1))
        sleep(3)
        self.printPTZ()
        if(self.comparePTZ(position, self.getStatus())):
            return False
        else:
            return True

    def checkFocusMove(self):
        status = self.getFocusStatus()
        self.focusContinuousMove(random.uniform(-1, 1), 1)
        sleep(1)
        if(self.compareFocus(status, self.getFocusStatus())):
            return False
        else:
            return True
    
    def printFocusStatus(self):
        print 'x = {0:2f}'.format(self.getFocusStatus().FocusStatus20.Position)

    def printImagingSettings(self):
        print self.imaging.GetImagingSettings({'VideoSourceToken': self.media_profile.VideoSourceConfiguration.SourceToken})
    
    def setFocusModeAuto(self):
        # request = self.imaging.GetImagingSettings({'VideoSourceToken': self.media_profile.VideoSourceConfiguration.SourceToken})
        self.requestSetImagingSettings.ImagingSettings.Focus.AutoFocusMode = "AUTO"
        self.imaging.SetImagingSettings(self.requestSetImagingSettings)

    def setFocusModeManual(self):
        currentSettings = self.imaging.GetImagingSettings({'VideoSourceToken': self.media_profile.VideoSourceConfiguration.SourceToken})
        self.requestSetImagingSettings.ImagingSettings = currentSettings
        self.requestSetImagingSettings.ImagingSettings.Focus.AutoFocusMode = "MANUAL"
        print self.requestSetImagingSettings
        self.imaging.SetImagingSettings(self.requestSetImagingSettings)

    # Compare PTZ of two objects status
    def comparePTZ(self, a, b):
        ax = a[0].PanTilt._x
        ay = a[0].PanTilt._y
        az = a[0].Zoom._x

        bx = b[0].PanTilt._x
        by = b[0].PanTilt._y
        bz = b[0].Zoom._x

        if(ax == bx and ay == by and az == bz):
            return True
        else:
            return False

    # Compare focus of two objects status
    def compareFocus(self, a, b):
        if(a.FocusStatus20.Position == b.FocusStatus20.Position):
            return True
        else:
            return False





    


