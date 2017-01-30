from pubnub import Pubnub
import curses

pubnub = Pubnub(
	publish_key = "pub-c-e58be9c3-c466-4efa-9da8-5382cd64792d",
	subscribe_key = "sub-c-c0bdecde-e682-11e6-a85c-0619f8945a4f")

channel = "nhan_pi_tinker_channel"
message = "Test message"
send_message = ""

# retrieve the curses window then disable the keyboard echoing to screen. Turn on instant response and cursors key are special value
screen = curses.initscr()
curses.noecho() 
curses.cbreak()
screen.keypad(True)

try:
	while True:   
		char = screen.getch()
		if char == ord('q'):
			send_message = "quit"
			# send last message before quitting
			pubnub.publish(channel = channel, message = send_message)
			break
		elif char == curses.KEY_UP:
			send_message = "up"
		elif char == curses.KEY_DOWN:
			send_message = "down"
		elif char == curses.KEY_RIGHT:
			send_message = "right"
		elif char == curses.KEY_LEFT:
			send_message = "left"
		elif char == ord('s'):
			send_message = "pause"

		pubnub.publish(
			channel = channel,
			message = send_message)

finally:
    # Close curses and turn echo back on
    curses.nocbreak(); screen.keypad(0); curses.echo()
    curses.endwin()
    
    