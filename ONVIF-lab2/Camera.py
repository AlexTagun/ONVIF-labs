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

        self.imaging = self.mycam.create_imaging_service()

        # Create request for setting imaging settings
        self.requestSetImagingSettings = self.imaging.create_type("SetImagingSettings")
        self.requestSetImagingSettings.VideoSourceToken = self.media_profile.VideoSourceConfiguration.SourceToken
        
    
    def getImagingSettings(self):
        return self.imaging.GetImagingSettings({'VideoSourceToken': self.media_profile.VideoSourceConfiguration.SourceToken})
    
    def getPreview(self):
        return self.mycam.media.GetSnapshotUri({'ProfileToken': self.media_profile._token})

    def getBrightness(self):
        return self.getImagingSettings().Brightness

    def createImagingRequest(self):
        self.requestSetImagingSettings.ImagingSettings = self.getImagingSettings()
        return self.requestSetImagingSettings

    def setExposureMode(self, value):
        request = self.createImagingRequest()
        request.ImagingSettings.Exposure.Mode = value
        self.imaging.SetImagingSettings(request)
    
    def setWhiteBalanceMode(self, value):
        request = self.createImagingRequest()
        request.ImagingSettings.WhiteBalance.Mode = value
        self.imaging.SetImagingSettings(request)
    
    def setBrightness(self, value):
        request = self.createImagingRequest()
        request.ImagingSettings.Brightness = self.relativeSum(0, 100, value, request.ImagingSettings.Brightness)
        self.imaging.SetImagingSettings(request)

    def setContrast(self, value):
        request = self.createImagingRequest()
        request.ImagingSettings.Contrast = self.relativeSum(0, 100, value, request.ImagingSettings.Contrast)
        self.imaging.SetImagingSettings(request)

    def setExposureGain(self, value):
        request = self.createImagingRequest()
        request.ImagingSettings.Exposure.Gain = self.relativeSum(0, 100, value, request.ImagingSettings.Exposure.Gain)
        self.imaging.SetImagingSettings(request)

    def setExposureTime(self, value):
        request = self.createImagingRequest()
        request.ImagingSettings.Exposure.ExposureTime = self.relativeSum(0, 40000, value, request.ImagingSettings.Exposure.ExposureTime)
        self.imaging.SetImagingSettings(request)

    def setCrGain(self, value):
        request = self.createImagingRequest()
        request.ImagingSettings.WhiteBalance.CrGain = self.relativeSum(0, 255, value, request.ImagingSettings.WhiteBalance.CrGain)
        self.imaging.SetImagingSettings(request)

    def setCbGain(self, value):
        request = self.createImagingRequest()
        request.ImagingSettings.WhiteBalance.CbGain = self.relativeSum(0, 255, value, request.ImagingSettings.WhiteBalance.CbGain)
        self.imaging.SetImagingSettings(request)

    def relativeSum(self, minVal, maxVal, relVal, curVal):
        curVal += relVal
        if(curVal < minVal):
            return minVal
        if(curVal > maxVal):
            return maxVal
        return curVal
