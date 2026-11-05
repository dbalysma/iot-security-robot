import RPi.GPIO as GPIO
from time import sleep
import time
import os
from time import gmtime, strftime
from datetime import datetime
import datetime
from picamera import PiCamera
import picamera

GPIO.cleanup()
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

GPIO.setup(29, GPIO.IN)                             #Read output from PIR motion sensor on Board Pin 37

i = 1                                               #'i' is iteration
while True:
    i = GPIO.input(29)                              #i is the variable for PIR when motion is detected
    
    now = datetime.datetime.now()
    today_date = datetime.date.today()
    current_time = now.strftime('%H:%M:%S')
    date_time = datetime.datetime.strftime(today_date, current_time)
    
    if i == 0:                                      #When output from motion sensor is LOW
        print ("No detection"),i
        time.sleep(1)
        
    elif i == 1:                                      #When output from motion sensor is HIGH
        print ("Motion detected"),i
        def take_photo(folder_path):
            camera = picamera.PiCamera()
    
            try:
        #camera = PiCamera()
                camera.start_preview()
                sleep(2)

                today_date = datetime.date.today()
                current_time = time.strftime('%H:%M:%S')

                file_name = f"{current_time}.jpg"
                file_path = os.path.join(folder_path, file_name)
    
            finally:
                camera.capture(file_path)
                camera.stop_preview()
                camera.close()
            print("Image Captured on:", today_date, "at", current_time, "and saved too", file_path)

        folder_path = "/home/dylan/MobileSec/Logs"
        take_photo(folder_path)
        
        time.sleep(3)