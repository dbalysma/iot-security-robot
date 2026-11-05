import RPi.GPIO as GPIO
import time

GPIO.cleanup()
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(5, GPIO.IN)                             #Read output from PIR motion sensor on Pin 11

while True:
	i=GPIO.input(5)                                #i is the variable for when motion is detected
	if i==0:                                        #When output from motion sensor is LOW
		print ("No detection"),i
		time.sleep(1)
  
	elif i==1:                                      #When output from motion sensor is HIGH
		print ("Motion detected"),i
		time.sleep(1)
  