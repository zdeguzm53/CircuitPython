import board #pylint: disable-msg=import-error
import time
from fancyLED import FancyLED

two = board.D2
three = board.D3
four = board.D4
five = board.D5
six = board.D6
seven = board.D7

fancy1 = FancyLED(two, three, four)
fancy2 = FancyLED(five, six, seven)

while True:
    fancy1.alternate()
    fancy1.off()
    fancy2.blink()
    fancy2.off()
    fancy1.chase()
    fancy1.off()
    fancy2.sparkle()
    fancy2.off()