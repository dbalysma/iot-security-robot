from picamera import PiCamera
import picamera
from time import sleep
import time
from datetime import datetime
import datetime
import os

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
    print("Image Captured on:", today_date, "at", current_time, "and saved too", file_path)

folder_path = "/home/dylan/MobileSec/Logs"
take_photo(folder_path)

