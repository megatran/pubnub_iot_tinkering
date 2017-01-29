import RPi.GPIO as GPIO
import time

# set up raspberry pi pins that are connected to the H-Bridge L298N
# The motors are wired to the H-Bridge which are plugged in to the corresponding pins on the Pi (7,11,13,15)
# CAUTION: plugging the motors to the pi will damage it. An H-Bridge or motor controller is needed.

# This test the robot car to draw a square: Go straight then turn right 4 times

GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.OUT)
GPIO.setup(11, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)

print("get ready")

for x in xrange(0,4):
    GPIO.output(7, True)
    GPIO.output(13, True)
    time.sleep(2)

    GPIO.output(7, False)
    GPIO.output(13, False)
    time.sleep(.2)

    GPIO.output(7, True)
    GPIO.output(15, True)
    time.sleep(.97)

    GPIO.output(7, False)
    GPIO.output(15, False)

GPIO.cleanup()
