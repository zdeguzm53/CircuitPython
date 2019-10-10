#import all necessary libraries
import board #pylint: disable-msg=import-error
import adafruit_bus_device #pylint: disable-msg=import-error
from digitalio import DigitalInOut, Direction, Pull #pylint: disable-msg=import-error
from lcd.lcd import LCD #pylint: disable-msg=import-error
from lcd.i2c_pcf8574_interface import I2CPCF8574Interface #pylint: disable-msg=import-error
lcd_columns = 16
lcd_rows = 2

#set up LCD
lcd = LCD(I2CPCF8574Interface(0x3f), num_rows=lcd_rows, num_cols=lcd_columns)
lcd.pull = Pull.UP
lcd.backlight = True

#declare button, send it to ground
button = DigitalInOut(board.A2)
button.direction = Direction.INPUT
button.pull = Pull.DOWN

#declare switch, don't ground it
switch = DigitalInOut(board.A4)
switch.direction = Direction.INPUT
switch.pull = Pull.UP


previousState = True #variable to determine if it switched from on/off
counter = 0 #number of button presses
inc = 0 #variable to determine if counting up or down

#initial LCD message
lcd.set_cursor_pos(0,0)
lcd.print("Switch State: ")
lcd.set_cursor_pos(1,0)
lcd.print("Presses: ")


while True:
    if switch.value: #if switch is on
        inc = 1 #counting up
        lcd.set_cursor_pos(0,13)
        lcd.print(" UP") #print "UP" on end of first line
    else: #if switch is off
        inc = -1 #counting down
        lcd.set_cursor_pos(0,13)
        lcd.print("DWN") #print "DWN" on end of first line
    if button.value: #if button is off
        lcd.set_cursor_pos(1,9) #middle of second line
        lcd.print(str(counter) + "   ") #print current button count
        previousState = False #most recent state is "off"
    else: #if button is being pressed
        if previousState == False: #if it was just off
            counter += inc #add a button press to total
            lcd.set_cursor_pos(1,9) #middle of second line
            lcd.print(str(counter)) #print new counter
        previousState = True #most recent state is on
