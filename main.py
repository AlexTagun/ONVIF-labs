from onvif import ONVIFCamera
from time import sleep
import math
from Camera import Camera
from NumPad import NumPad
from CameraManager import CameraManager


def prA():
    print 'A key pressed'

    # camera.absoluteMove(-1, 0, 0)
    # sleep(4)
    # x = float(-1)
    # while(x < 0.99):

    #     camera.absoluteMove(x, y, 0)
    #     sleep(0.5)
    #     x += 0.01
    #     print 'x = {0:2f} y = {1:3f}'.format(x, y)

def rotareOneCircle(camera):
    angle = 0
    camera.absoluteMove(0, 0, 0)
    sleep(10)
    flag = True
    r = 0.2
    circleTime = 75
    while(flag):
        x = math.cos(math.radians(angle))
        y = math.sin(math.radians(angle))
        if(-0.001 < x < 0.001): x = 0
        if(-0.001 < y < 0.001): y = 0
        print x, y
        print angle
        camera.continuousMove(x*r, y*r, 0, 0)
        
        angle += 10
        sleep((circleTime * 5 )/360)
        # camera.stop()
        
        if(angle > 360):
            break
    camera.stop()


if __name__ == "__main__":
    # camera = Camera()

    # while True:  # making a loop
    #     try:  # used try so that if user pressed other than the given key error will not be shown
    #         if keyboard.is_pressed('a'):  # if key 'q' is pressed 
    #             print('You Pressed A Key!')
    #             # break  # finishing the loop
    #         else:
    #             print('nothing')
    #             pass
    #         sleep(0.1)
    #     except:
    #         break  # if user pressed a key other than the given key the loop will break

    # keyboard.add_hotkey('a', prA())
    # keyboard.wait()
    cameraManager = CameraManager()
    # cameraManager.camera.focusContinuousMove(0, 3)
    # cameraManager.camera.focusAbsoluteMove(0, 1)
    cameraManager.moveCameraByNumPad()