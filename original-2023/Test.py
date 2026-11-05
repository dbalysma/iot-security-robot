#import os

#os.system('mv /home/dylan/MobileSec/picture.jpg /home/dylan/MobileSec/image.jpg')

#import subprocess

#subprocess.call(['mv', '/home/dylan/MobileSec/image.jpg', '/home/dylan/MobileSec/picture.jpg']) 

from picamera.array import PiRGBArray
import picamera.array
from picamera import PiCamera
import picamera 
import time
import cv2

#Initialises the camera, grabs reference for raw capture
camera = PiCamera()
rawCapture = PiRGBArray(camera)

#Camera Warm up
time.sleep(0.1)

#Takes a photo from camera
camera.capture(rawCapture, format="bgr")
image = rawCapture.array

#Displays image on screen
cv2.imshow("image", image)
cv2.waitKey(0)
