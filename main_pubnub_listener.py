from pubnub import Pubnub
import json
import RPi.GPIO as GPIO
import sys


# setup pubnub

pubnub = Pubnub(
	publish_key = "pub-c-e58be9c3-c466-4efa-9da8-5382cd64792d",
	subscribe_key = "sub-c-c0bdecde-e682-11e6-a85c-0619f8945a4f")

channel = "nhan_pi_tinker_channel"



def error(message):
    print("ERROR : " + str(message))


def connect(message):
    print("CONNECTED")


def reconnect(message):
    print("RECONNECTED")


def disconnect(message):
    print("DISCONNECTED")

def callback(message, channel):
	print('[' + channel + ']: ' + "key pressed: " + str(message))
	wiresless_control(message)

pubnub.subscribe(channels=channel, callback=callback, error=callback,
                 connect=connect, reconnect=reconnect, disconnect=disconnect)

def wiresless_control(message):
		# define GPIO pin
		GPIO.setmode(GPIO.BOARD)
		GPIO.setup(7,GPIO.OUT)
		GPIO.setup(11,GPIO.OUT)
		GPIO.setup(13,GPIO.OUT)
		GPIO.setup(15,GPIO.OUT)

		key_input = message[u'text'].replace("u\"","\"").replace("u\'","\'")
		print key_input
		if key_input == "quit":
			print("QUIT")
			GPIO.cleanup()
			sys.exit(0)

		elif key_input == "up":
			GPIO.output(7,False)
			GPIO.output(11,True)
			GPIO.output(13,False)
			GPIO.output(15,True)
		elif key_input == "down":
			GPIO.output(7,True)
			GPIO.output(11,False)
			GPIO.output(13,True)
			GPIO.output(15,False)
		elif key_input == "right":
			GPIO.output(7,True)
			GPIO.output(11,False)
			GPIO.output(13,False)
			GPIO.output(15,True)
		elif key_input == "left":
			GPIO.output(7,False)
			GPIO.output(11,True)
			GPIO.output(13,True)
			GPIO.output(15,False)
		elif key_input == "pause":
			GPIO.output(7,False)
			GPIO.output(11,False)
			GPIO.output(13,False)
			GPIO.output(15,False)
