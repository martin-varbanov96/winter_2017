import picamera
import calendar
import time
path_time = 000
format_img = ".jpg"
while True:
    path_time=str(calendar.timegm(time.gmtime()))
    camera = picamera.PiCamera()
    camera.capture(path_time+format_img)
    camera.hflip = True
    camera.vflip = True
