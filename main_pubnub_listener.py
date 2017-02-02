from pubnub import Pubnub
from multiprocessing import Process
import RPi.GPIO as GPIO
import sys
import time


# setup pubnub

pubnub = Pubnub(
	publish_key = "pub-c-e58be9c3-c466-4efa-9da8-5382cd64792d",
	subscribe_key = "sub-c-c0bdecde-e682-11e6-a85c-0619f8945a4f")

channel = "nhan_pi_tinker_channel"
ultrasonic_channel = "nhan_ultrasonic_channel"


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

def ultrasonic_wiresless():

	# ultrasonic sensor (HC-SR04) measures the distance to an object by using sound wave. Good choice for object avoidance.
	# This publisher runs concurrently (using Python's multiprocessing) with the subscriber.
	# All ultrasonic data (distance from robot to surrounding object) is published to the ultrasonic_channel.


	GPIO.setmode(GPIO.BOARD)
	# trig pin of the distance measurement sensor
	TRIG = 36
	# Define the echo pin of the distance measurement sensor
	ECHO = 38

	# set up ultrasonic sensor
	GPIO.setwarnings(False)
	GPIO.setup(TRIG,GPIO.OUT)                  
	GPIO.setup(ECHO,GPIO.IN)

	while True:    
		pulse_start = 0
		GPIO.output(TRIG, False)                
		time.sleep(2)                            

		GPIO.output(TRIG, True)                  
		time.sleep(0.00001)                      
		GPIO.output(TRIG, False)     

		while GPIO.input(ECHO)==0:              
		  pulse_start = time.time()            

		while GPIO.input(ECHO)==1:               
		  pulse_end = time.time()               

		pulse_duration = pulse_end - pulse_start 
		distance = pulse_duration * 17150
		distance = int(distance)

		print ("\nDistance of the object from Robot's sensor = "+str(distance)+" cm.")
		pubnub.publish(channel = ultrasonic_channel, message = distance)

def wiresless_control(message):

	# this method subscribes to nhan_pi_tinker_channel which awaits for user's keyboard input from the sender to tell the motor what to do.
	# this method and the ultrasonic_wiresless method both run at the same time!

	# define GPIO pin
	GPIO.setmode(GPIO.BOARD)

	GPIO.setup(7,GPIO.OUT)
	GPIO.setup(11,GPIO.OUT)
	GPIO.setup(13,GPIO.OUT)
	GPIO.setup(15,GPIO.OUT)


	# only use this when send message via pubnub console. For example, it would retrieve {"text":"quit"}
	#key_input = message[u'text'].replace("u\"","\"").replace("u\'","\'")

	# comment this line below if use pubnub console
	key_input = message
	
	print key_input
	if key_input == "quit":
		print("QUIT")
		pubnub.unsubscribe(channel=channel)
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

if __name__=='__main__':
	# Having two process run concurrently:
	# - the ultrasonic sensor publishes data to ultrasonic_channel
	# - pubnub subscriber also waiting for command from remote user
	# - when user pressed 'q', program will quit thus kill both processes.
	p2 = Process(target= ultrasonic_wiresless)
	# parent process will kill child process if q is pressed
	p2.daemon = True
	p2.start()

pubnub.subscribe(channels=channel, callback=callback, error=callback,
                 connect=connect, reconnect=reconnect, disconnect=disconnect)
