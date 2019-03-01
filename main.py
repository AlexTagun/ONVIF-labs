from onvif import ONVIFCamera
from time import sleep
import math
from Camera import Camera

if __name__ == "__main__":
    camera = Camera()

    # camera.absoluteMove(-1, 0, 0)
    # sleep(4)
    # x = float(-1)
    # while(x < 0.99):

    #     camera.absoluteMove(x, y, 0)
    #     sleep(0.5)
    #     x += 0.01
    #     print 'x = {0:2f} y = {1:3f}'.format(x, y)

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
