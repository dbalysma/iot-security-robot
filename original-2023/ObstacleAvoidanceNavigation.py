import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

#Ultrasonic Sensor
TRIG = 19
ECHO = 26
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

#Motors
A1A = 18
B1A = 12
A1B = 17
B1B = 6
GPIO.setup(A1A, GPIO.OUT)
GPIO.setup(B1A, GPIO.OUT)
GPIO.setup(A1B, GPIO.OUT)
GPIO.setup(B1B, GPIO.OUT)

#Truth Table functions for H-Bridge
def Stop(sec):
    GPIO.output(A1A, True)
    GPIO.output(A1B, True)
    GPIO.output(B1A, True)
    GPIO.output(B1B, True)

def Forward(sec):
    GPIO.output(A1A, False)
    GPIO.output(A1B, True)
    GPIO.output(B1A, False)
    GPIO.output(B1B, True)
    
def PivotLeft(sec):
    GPIO.output(A1A, True)
    GPIO.output(A1B, True)
    GPIO.output(B1A, True)
    GPIO.output(B1B, False)
    
def PivotRight(sec):
    GPIO.output(A1A, False)
    GPIO.output(A1B, True)
    GPIO.output(B1A, True)
    GPIO.output(B1B, True)

def RotateClockwise(sec):
    GPIO.output(A1A, False)
    GPIO.output(A1B, True)
    GPIO.output(B1A, True)
    GPIO.output(B1B, False)
    
def RotateAntiClockwise(sec):
    GPIO.output(A1A, False)
    GPIO.output(A1B, True)
    GPIO.output(B1A, True)
    GPIO.output(B1B, False)

count = 0 

while True:
    i = 0
    Forward(10)
    
    for i in range(2):
        print("Distance Measurement In Progress")

        GPIO.output(TRIG, False)
        print ("Waiting For Sensor")
        time.sleep(1)
        
        GPIO.output(TRIG, True)                                     #A pulse signal is required to start sensor 
        time.sleep(0.00001)
        GPIO.output(TRIG, False)

    while GPIO.input(ECHO) == 0:                                  #Starts recording input for ECHO when puls is Low 
        #Forward(5)
        print("Roaming...")
        
    pulse_start = time.time()
    
    while GPIO.input(ECHO) == 1:                                  #Starts recording input signal when pulse is high
        #Forward(2)
        print("Hold up")
        
    pulse_end = time.time()

    pulse_duration = pulse_end - pulse_start

    averagedistance = pulse_duration * 17150                           #Speed of Sound(343 m/s) = Distance/Time
    averagedistance = round(averagedistance,2)                                #This is divided by 2 to calculate the distance to and from
    print ("Distance:", averagedistance, "cm")                         #Nearest 2 decimal places

    flag = 0

    if averagedistance < 60:
        count = count + 1
        Stop(2)
        time.sleep(1)
        RotateClockwise(0.75)
        #time.sleep(1.5)
        
        #Forward(3)
        #print("Obstacle in front, changing direction")
        
        if(count%3 == 1) & (flag == 0):
            Stop(1)
            PivotRight(0.25)
            flag = 1
            print ("Object on the left, Turning right")
            
        else:
            Stop(1)
            PivotLeft(0.25)
            flag = 0
            print ("Object on the right, Turning left")
        time.sleep(1.5)
        #Stop(0.5)
        #time.sleep(1)
        
    else:
        Forward(10)
        time.sleep(0.5)
        flag = 0 