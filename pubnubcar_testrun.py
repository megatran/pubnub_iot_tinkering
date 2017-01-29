import RPi.GPIO as GPIO
import time

# set up raspberry pi pins that are connected to the H-Bridge L298N
# The motors are wired to the H-Bridge which are plugged in to the corresponding pins on the Pi (7,11,13,15)
# CAUTION: plugging the motors to the pi will damage it. An H-Bridge or motor controller is needed.

GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.OUT)
GPIO.setup(11, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)

print("get ready")

GPIO.output(7, True)
time.sleep(1)

GPIO.output(7, False)
GPIO.output(11, True)
time.sleep(1)

GPIO.output(11, False)
GPIO.output(13, True)
time.sleep(1)

GPIO.output(11, False)
GPIO.output(13, True)
time.sleep(1)

GPIO.output(13, False)
GPIO.output(15, True)
time.sleep(1)

GPIO.output(15, False)

print("test run finish")
GPIO.cleanup()

