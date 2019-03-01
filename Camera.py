from onvif import ONVIFCamera
from time import sleep

class Camera:
    def __init__(self):
        # IP camera initialization
        print 'IP camera initialization'
        self.mycam = ONVIFCamera('192.168.15.42', 80, 'ilyahandsup', 'rmvtJ8hGqETY5lnj', '/etc/onvif/wsdl/wsdl')
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
        status = self.imaging.GetStatus({'VideoSourceToken': self.media_profile.VideoSourceConfiguration.SourceToken})
        request = self.imaging.create_type("GetServiceCapabilities")
        imaging_service_capabilities = self.ptz.GetServiceCapabilities(request)
        # print imaging_service_capabilities
    
    # get camera position in this moment
    def getPosition(self):
        return self.ptz.GetStatus({'ProfileToken': self.media_profile._token})

    def stop(self):
        self.requestStop.PanTilt = True
        self.requestStop.Zoom = True
        self.ptz.Stop(self.requestStop)
        print('Stopping camera')
    
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
        position = self.getPosition()[0]
        print 'x = {0:2f} y = {1:3f} z = {2:4f}'.format(position.PanTilt[1], position.PanTilt[0], position.Zoom[0])

    # Get focus status
    def getFocusStatus(self):
        return self.imaging.GetStatus({'VideoSourceToken': self.media_profile.VideoSourceConfiguration.SourceToken})

    # Functions for continuous moving








    


