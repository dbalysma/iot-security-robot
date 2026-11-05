import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
TRIG = 19
ECHO = 26

while True:
    print("Distance Measurement In Progress")

    GPIO.setup(TRIG, GPIO.OUT)
    GPIO.setup(ECHO, GPIO.IN)

    GPIO.output(TRIG, False)
    print ("Waiting For Sensor")
    time.sleep(1)


    GPIO.output(TRIG, True)                                     #A pulse signal is required to start sensor 
    time.sleep(0.00001)
    GPIO.output(TRIG, False)

    while GPIO.input(ECHO)==0:                                  #Starts recording input for ECHO when puls is Low
        pulse_start = time.time()
    
    while GPIO.input(ECHO)==1:                                  #Starts recording input signal when pulse is high
        pulse_end = time.time()

    pulse_duration = pulse_end - pulse_start

    averagedistance = pulse_duration * 17150                           #Speed of Sound(343 m/s) = Distance/Time
    averagedistance = round(averagedistance,2)                                #This is divided by 2 to calculate the distance to and from
    print ("Distance:", averagedistance, "cm")                         #Nearest 2 decimal places
    
#if avgeragedistance < 15:
    #count = count + 1
    #stop()
    #time.sleep(1)
    #back()
    #time.sleep(1.5)
    #if(count%3 ==1) & (flag ==0):
        #right()
        #flag = 1
        #print ("Object on the left, Turning right")
    #else:
        #left()
        #flag = 0
        #print ("Object on the right, Turning left")
    #time.sleep(1.5)
    #stop()
    #time.sleep(1)
#else:
    #forward()
    #flag = 0 