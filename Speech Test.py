import speech_recognition as sr
import time
import RPi.GPIO as GPIO
import random

run = 1
command = ""
voiceOK = False
r = sr.Recognizer()
r.energy_threshold = 3250
blueled = "forward"
redled = "backward"
stop = "stop"
left = "left"
right = "right"
red = 20
blue = 21
motor1 = 16
motor2 = 12

GPIO.cleanup()
GPIO.setmode(GPIO.BCM)


GPIO.setup(16, GPIO.OUT)
GPIO.setup(12, GPIO.OUT)
GPIO.setup(26, GPIO.OUT)
GPIO.setup(19, GPIO.OUT)
GPIO.setup(25, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)
GPIO.output(19, GPIO.LOW)
GPIO.output(25, GPIO.LOW)
GPIO.output(16, GPIO.LOW)
GPIO.output(12, GPIO.LOW)
GPIO.output(24, GPIO.LOW)



GPIO.setwarnings(False)
while(run == 1):
    
    speechstring = input("Enter direction")
                
    if(speechstring == blueled):
        print("Moving Forwards")
        GPIO.cleanup()
        GPIO.setmode(GPIO.BCM)

        GPIO.setup(16, GPIO.OUT)
        GPIO.setup(12, GPIO.OUT)
        GPIO.setup(25, GPIO.OUT)
        GPIO.setup(24, GPIO.OUT)
        GPIO.output(16, GPIO.LOW)
        GPIO.output(12, GPIO.HIGH)
        GPIO.output(25, GPIO.HIGH)
        GPIO.output(24, GPIO.LOW)
        time.sleep(3)
        GPIO.cleanup()

    elif(speechstring == redled):
        print("Moving Backwards")
        GPIO.cleanup()
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(16, GPIO.OUT)
        GPIO.setup(12, GPIO.OUT)
        GPIO.setup(25, GPIO.OUT)
        GPIO.setup(24, GPIO.OUT)
        GPIO.output(16, GPIO.HIGH)
        GPIO.output(12, GPIO.LOW)
        GPIO.output(25, GPIO.LOW)
        GPIO.output(24, GPIO.HIGH)
        time.sleep(3)
        GPIO.cleanup()

    elif(speechstring == left):
        GPIO.cleanup()
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(16, GPIO.OUT)
        GPIO.setup(12, GPIO.OUT)
        GPIO.setup(25, GPIO.OUT)
        GPIO.setup(24, GPIO.OUT)
        GPIO.output(16, GPIO.LOW)
        GPIO.output(12, GPIO.HIGH)
        GPIO.output(25, GPIO.LOW)
        GPIO.output(24, GPIO.HIGH)
        print("Moving left")
        time.sleep(1.33)
        GPIO.cleanup()

    elif(speechstring == right):
        GPIO.cleanup()
        GPIO.setmode(GPIO.BCM)

        GPIO.setup(16, GPIO.OUT)
        GPIO.setup(12, GPIO.OUT)
        GPIO.setup(25, GPIO.OUT)
        GPIO.setup(24, GPIO.OUT)
        GPIO.output(16, GPIO.HIGH)
        GPIO.output(12, GPIO.LOW)
        GPIO.output(25, GPIO.HIGH)
        GPIO.output(24, GPIO.LOW)
        print("Moving right")
        time.sleep(1.33)
        GPIO.cleanup()

    elif(speechstring == stop):
        GPIO.cleanup()
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(16, GPIO.OUT)
        GPIO.setup(12, GPIO.OUT)
        GPIO.setup(25, GPIO.OUT)
        GPIO.setup(24, GPIO.OUT)
        GPIO.output(16, GPIO.LOW)
        GPIO.output(12, GPIO.LOW)
        GPIO.output(25, GPIO.LOW)
        GPIO.output(24, GPIO.LOW)
        print("Movement stopped")

    elif(speechstring != redled or blueled or stop or left or right):
        print("Sorry, unclear. Try again!")
        GPIO.cleanup()
        GPIO.setmode(GPIO.BCM)

        GPIO.setup(16, GPIO.OUT)
        GPIO.setup(12, GPIO.OUT)
        GPIO.setup(25, GPIO.OUT)
        GPIO.setup(24, GPIO.OUT)
        GPIO.output(16, GPIO.LOW)
        GPIO.output(12, GPIO.LOW)
        GPIO.output(25, GPIO.LOW)
        GPIO.output(24, GPIO.LOW)

