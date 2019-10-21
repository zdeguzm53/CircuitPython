import board #pylint: disable-msg=import-error
import time
from fancyLED import FancyLED #imports the class and methods

#led pin numbers
two = board.D2
three = board.D3
four = board.D4
five = board.D5
six = board.D6
seven = board.D7

#defines an object as the class
fancy1 = FancyLED(two, three, four)
fancy2 = FancyLED(five, six, seven)

#goes through all the methods
#turns off for 3 seconds between each one
while True:
    fancy1.alternate()
    fancy1.off()
    fancy2.blink()
    fancy2.off()
    fancy1.chase()
    fancy1.off()
    fancy2.sparkle()
    fancy2.off()