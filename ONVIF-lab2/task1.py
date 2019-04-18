from CameraManager import CameraManager
import cv2
import matplotlib.pyplot as plt
import time
import numpy

def draw_axis(axis, vals, color):
	axis.cla()
	axis.plot(vals, color)
	axis.set_xlim(0, 255)
	axis.set_yticklabels([])

def calc_move(values, coef, accur, max_step):
	values = [i[0] for i in values]
	if values[0] >= values[1]:
		_max = 0
		_min = 1
		move_to = 1
	else:
		_max = 1
		_min = 0
		move_to = -1
	if values[_max] * accur > values[_min]:
		move = (1 - (values[_min] / values[_max])) * coef * max_step
		move *= move_to
		return move
	return 0

def isNeedToStop(array):
	cnt = 0
	numZero = 0
	array = [i[0] for i in array]
	for val in array:
		cnt += 1
		if (val <= 5000):
			numZero += 1
	coef = numZero * 1.0 / cnt
	print coef
	return coef < 0.15

def isNeedToStop2(array):
	perc = numpy.percentile(array, [5, 95])
	print perc
	return perc[0] > 200 and perc[0] < 1000 and perc[1] < 40000 and perc[1] > 15000
    
if __name__ == "__main__":
    # User data
    address = '192.168.15.42'
    port = 80
    login = 'alextagun'
    password = 'HSrdajML01pn'
    wsdlFolder = '/etc/onvif/wsdl/wsdl'

    # Program
    cameraManager = CameraManager(address, port, login, password, wsdlFolder)
    camera = cameraManager.camera



    y_ax = plt.subplot(121)
    cb_ax = plt.subplot(222)
    cr_ax = plt.subplot(224)
    plt.ion()
    plt.show()

    
    camera.setExposureMode("MANUAL")
    camera.setWhiteBalanceMode("MANUAL")
    # print camera.getImagingSettings()

    while True:
        cameraManager.downloadPreviewImage()
        im = cv2.imread('img.jpg')

        ycbcr = cv2.cvtColor(im, cv2.COLOR_BGR2YCrCb)

        hist_y = cv2.calcHist([ycbcr],[0],None,[256],[0,256])
        hist_cr = cv2.calcHist([ycbcr],[1],None,[256],[0,256])
        hist_cb = cv2.calcHist([ycbcr],[2],None,[256],[0,256])

        draw_axis(y_ax, hist_y, 'b')
        draw_axis(cb_ax, hist_cb, 'b')
        draw_axis(cr_ax, hist_cr, 'r')
        plt.pause(0.01)

        hist_cb_2 = cv2.calcHist([ycbcr],[2],None,[2],[0,256])
        hist_cr_2 = cv2.calcHist([ycbcr],[1],None,[2],[0,256])


        hist_y_6 = cv2.calcHist([ycbcr], [0], None, [6], [0,256])

        if not isNeedToStop2(hist_y):
            b = len(hist_y_6) - 1
            w = 1
            for i in range(1, len(hist_y_6)):
                if hist_y_6[i][0] > 300000:
                    b = i
                    break
            for i in range(len(hist_y_6) - 1, 0, -1):
                if hist_y_6[i][0] > 300000:
                    w = i
                    break
            black = hist_y_6[0][0] > 300000
            white = hist_y_6[-1][0] > 300000
            if black and white:
                val = max(hist_y_6[0][0], hist_y_6[-1][0])
                dif = val / 2000000.0 * 20.0
                dif = round(dif)
                print('contrast -', dif)
                camera.setContrast(-dif)
            elif black:
                dif = (len(hist_y_6) - w) * 20.0 / len(hist_y_6)
                dif = round(dif)
                print('exp +', dif)
                camera.setExposureGain(dif)
            elif white:
                dif = b * 20.0 / len(hist_y_6)
                dif = round(dif)
                print('exp -', dif)
                camera.setExposureGain(-dif)
            else:
                val = min(b, len(hist_y_6) - w)
                dif = val * 20.0 / (len(hist_y_6) / 2.0)
                dif = round(dif)
                print('contrast +', dif)
                camera.setContrast(dif)

        try:
            Cb = calc_move(hist_cb_2, 2.56, 0.9, 2)
            print('Cb:', Cb)
            camera.setCbGain(imaging, token, Cb)
            Cr = calc_move(hist_cr_2, 2.56, 0.9, 2)
            print('Cr:', Cr)
            camera.setCrGain(imaging, token, Cr)
        except Exception as e:
            print 'WhiteBalance err'

        time.sleep(1)