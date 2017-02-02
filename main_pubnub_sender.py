from __future__ import print_function
from pubnub import Pubnub
import curses

pubnub = Pubnub(
	publish_key = "pub-c-e58be9c3-c466-4efa-9da8-5382cd64792d",
	subscribe_key = "sub-c-c0bdecde-e682-11e6-a85c-0619f8945a4f")

channel = "nhan_pi_tinker_channel"
ultrasonic_channel = "nhan_ultrasonic_channel"
message = "Test message"
send_message = ""

# retrieve the curses window then disable the keyboard echoing to screen. Turn on instant response and cursors key are special value
screen = curses.initscr()
curses.noecho() 
curses.cbreak()
screen.keypad(True)

screen.addstr(0,0, "Welcome to Pubnub Robot Remote Control -- created by Nhan Tran")
screen.addstr(1,0, "Control your robot and get sensor input from anywhere in the world in real time!")

screen.addstr(3,0, "First, make sure you RUN Pubnub listener 'main_pubnub_listener.py' on the raspberry pi")
screen.addstr(4,0, "Press the Arrow keys: UP, DOWN, LEFT, RIGHT to control the motors in real time")
screen.addstr(5,0, "Press 's' for Pause/Stop and 'q' to QUIT the program")
screen.addstr(7,0, "=============================")

screen.addstr(9,0, "Robot's movement direction: ")
screen.addstr(11,0, "Distance of the object from Robot's Ultrasonic sensor (cm): ")


def callback(message, channel):
	var = message
	screen.addstr(12,0, str(message)+" centimeters     ")
	screen.refresh()

pubnub.subscribe(channels=ultrasonic_channel, callback=callback)

try:
	while True:   
		char = screen.getch()
		if char == ord('q'):
			screen.addstr(10,0, "EXITING PROGRAM...")
			screen.refresh()
			send_message = "quit"
			# send last message before quitting
			pubnub.publish(channel = channel, message = send_message)
			break
		elif char == curses.KEY_UP:
			screen.addstr(10,0, "FORWARD         ")
			screen.refresh()
			send_message = "up"
		elif char == curses.KEY_DOWN:
			screen.addstr(10,0, "BACKWARD        ")
			screen.refresh()
			send_message = "down"
		elif char == curses.KEY_RIGHT:
			screen.addstr(10,0, "TURNING RIGHT         ")
			screen.refresh()
			send_message = "right"
		elif char == curses.KEY_LEFT:
			screen.addstr(10,0, "TURNING LEFT       ")
			screen.refresh()
			send_message = "left"
		elif char == ord('s'):
			screen.addstr(10,0, "PAUSED        ")
			screen.refresh()
			send_message = "pause"

		pubnub.publish(
			channel = channel,
			message = send_message)

finally:
    # Close curses and turn echo back on
    curses.nocbreak(); screen.keypad(0); curses.echo()
    curses.endwin()
    
