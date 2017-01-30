import curses
import RPi.GPIO as GPIO

"""
This basic python program is a sample test to see if pi could retrieve keyboard response and thus control the robot
"""
# define GPIO pin
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7,GPIO.OUT)
GPIO.setup(11,GPIO.OUT)
GPIO.setup(13,GPIO.OUT)
GPIO.setup(15,GPIO.OUT)


# retrieve the curses window then disable the keyboard echoing to screen. Turn on instant response and cursors key are special value
screen = curses.initscr()
curses.noecho() 
curses.cbreak()
screen.keypad(True)

try:
        while True:   
            char = screen.getch()
            if char == ord('q'):
                break
            elif char == curses.KEY_UP:
                GPIO.output(7,False)
                GPIO.output(11,True)
                GPIO.output(13,False)
                GPIO.output(15,True)
            elif char == curses.KEY_DOWN:
                GPIO.output(7,True)
                GPIO.output(11,False)
                GPIO.output(13,True)
                GPIO.output(15,False)
            elif char == curses.KEY_RIGHT:
                GPIO.output(7,True)
                GPIO.output(11,False)
                GPIO.output(13,False)
                GPIO.output(15,True)
            elif char == curses.KEY_LEFT:
                GPIO.output(7,False)
                GPIO.output(11,True)
                GPIO.output(13,True)
                GPIO.output(15,False)
            elif char == ord('s'):
                GPIO.output(7,False)
                GPIO.output(11,False)
                GPIO.output(13,False)
                GPIO.output(15,False)
             
finally:
    # Close curses and turn echo back on
    curses.nocbreak(); screen.keypad(0); curses.echo()
    curses.endwin()
    GPIO.cleanup()
    
