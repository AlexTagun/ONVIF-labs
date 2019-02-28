from onvif import ONVIFCamera
from time import sleep

class Camera:
    def __init__(self):
        # IP camera initialization
        print 'IP camera initialization'
        self.mycam = ONVIFCamera('192.168.15.43', 80, 'admin', 'Supervisor', '/etc/onvif/wsdl/wsdl')
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
        self.request_continuous_move = self.ptz.create_type('ContinuousMove')
        self.request_continuous_move.ProfileToken = self.media_profile._token
        # print self.request_continuous_move

        # Relative move
        self.request_relative_move = self.ptz.create_type('RelativeMove')
        self.request_relative_move.ProfileToken = self.media_profile._token

        # Stop move
        self.request_stop = self.ptz.create_type('Stop')
        self.request_stop.ProfileToken = self.media_profile._token
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
        # print status
    
    # get camera position in this moment
    def getPosition(self):
        return self.ptz.GetStatus({'ProfileToken': self.media_profile._token})

    def stop(self):
        self.request_stop.PanTilt = True
        self.request_stop.Zoom = True
        self.ptz.Stop(self.request_stop)
        print('Stopping camera')
    
    # Continuous move functions
    def performContinuousMove(self, timeout):
        # Start continuous move
        self.ptz.ContinuousMove(self.request_continuous_move)

        # Wait a certain time
        sleep(timeout)

        # Stop continuous move
        self.stop()

        # print('Continuous move completed')
        sleep(2)

    # Print camera position x, y and zoom
    def printPTZ(self):
        position = self.getPosition()[0]
        print 'x = {0:2f} y = {1:3f} z = {2:4f}'.format(position.PanTilt[1], position.PanTilt[0], position.Zoom[0])

