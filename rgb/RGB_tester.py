import board #pylint: disable-msg=import-error
import time
from rgb import RGB

#pin numbers for each color
r1 = board.D2
g1 = board.D3
b1 = board.D4
r2 = board.D5
g2 = board.D6
b2 = board.D7

#declare objects
LED1 = RGB(r1,g1,b1)
LED2 = RGB(r2,g2,b2)

#call methods from class
LED1.red()
LED2.green()
time.sleep(1)
LED1.blue()
LED2.cyan()
time.sleep(1)
LED1.magenta()
LED2.yellow()
time.sleep(1)