import RPi.GPIO as GPIO
import time
from time import gmtime, strftime
from datetime import datetime
import datetime
from picamera import PiCamera
from time import sleep


GPIO.cleanup()
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

GPIO.setup(37, GPIO.IN)                             #Read output from PIR motion sensor on Board Pin 37
camera = PiCamera()

i = 1                                               #'i' is iteration
while True:
    i = GPIO.input(37)                              #i is the variable for when motion is detected
    
    now = datetime.datetime.now()
    today_date = datetime.date.today()
    current_time = now.strftime('%H:%M:%S')
    date_time = datetime.datetime.strftime(today_date, current_time)
    
    if i == 0:                                      #When output from motion sensor is LOW
        print ("No detection"),i
        time.sleep(1)
    elif i == 1:                                    #When output from motion sensor is HIGH
        print ("Movement detected"),i
        time.sleep(1)
        camera.start_preview()
        sleep(2)
        camera.capture('Capture.jpg')
        print ("Image Captured on:", today_date, "at", current_time)
        camera.stop_preview()
