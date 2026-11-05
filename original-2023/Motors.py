import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

A1A = 18
B1A = 12
A1B = 17
B1B = 6
GPIO.setup((18, 12, 17, 6), GPIO.OUT)

def runner(): 
    GPIO.setmode(GPIO.BCM)
    GPIO.setup((A1A,B1A,A1B,B1B), GPIO.OUT)
    
def Stop(sec):
    runner()
    GPIO.output(A1A, True)
    GPIO.output(A1B, True)
    GPIO.output(B1A, True)
    GPIO.output(B1B, True)
    time.sleep(sec)
    GPIO.cleanup()

def Forward(sec):
    runner()
    GPIO.output(A1A, False)
    GPIO.output(A1B, True)
    GPIO.output(B1A, False)
    GPIO.output(B1B, True)
    time.sleep(sec)
    GPIO.cleanup()
    
def PivotLeft(sec):
    runner()
    GPIO.output(A1A, True)
    GPIO.output(A1B, True)
    GPIO.output(B1A, True)
    GPIO.output(B1B, False)
    time.sleep(sec)
    GPIO.cleanup()

def PivotRight(sec):
    runner()
    GPIO.output(A1A, False)
    GPIO.output(A1B, True)
    GPIO.output(B1A, True)
    GPIO.output(B1B, True)
    time.sleep(sec)
    GPIO.cleanup()

def ChangeDirectionRight(sec):
    runner()
    GPIO.output(A1A, False)
    GPIO.output(A1B, True)
    GPIO.output(B1A, True)
    GPIO.output(B1B, False)
    time.sleep(sec)
    GPIO.cleanup()
    
def ChangeDirectionLeft(sec):
    runner()
    GPIO.output(A1A, False)
    GPIO.output(A1B, True)
    GPIO.output(B1A, True)
    GPIO.output(B1B, False)
    time.sleep(sec)
    GPIO.cleanup()    

Forward(2)
time.sleep(1)

ChangeDirectionLeft(0.75)
time.sleep(1)

Forward(2)
time.sleep(1)

ChangeDirectionRight(0.75)
time.sleep(1)

Forward(2)
time.sleep(2)
