#import time
import board
import adafruit_bus_device
from digitalio import DigitalInOut, Direction, Pull
from lcd.lcd import LCD
from lcd.i2c_pcf8574_interface import I2CPCF8574Interface
lcd_columns = 16
lcd_rows = 2

lcd = LCD(I2CPCF8574Interface(0x3f), num_rows=lcd_rows, num_cols=lcd_columns)
lcd.pull = Pull.UP
lcd.backlight = True

button = DigitalInOut(board.A2)
button.direction = Direction.INPUT
button.pull = Pull.DOWN

switch = DigitalInOut(board.A4)
switch.direction = Direction.INPUT
switch.pull = Pull.UP

previousState = True
counter = 0
inc = 0;

lcd.set_cursor_pos(0,0)
lcd.print("Switch State: ")
lcd.set_cursor_pos(1,0)
lcd.print("Presses: ")


while True:
    if switch.value:
        inc = 1
        lcd.set_cursor_pos(0,13)
        lcd.print(" UP")
    else:
        inc = -1
        lcd.set_cursor_pos(0,13)
        lcd.print("DWN")
    if button.value:
        lcd.set_cursor_pos(1,9)
        lcd.print(str(counter) + "   ")
        previousState = False
    else:
        if previousState == False:
            counter += inc
            lcd.set_cursor_pos(1,9)
            lcd.print(str(counter))
        previousState = True
