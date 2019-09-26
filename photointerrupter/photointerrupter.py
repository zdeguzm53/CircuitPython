import time
import board
import adafruit_bus_device
from digitalio import DigitalInOut, Direction, Pull

photoint = DigitalInOut(board.D2)
photoint.direction = Direction.INPUT
photoint.pull = Pull.UP

previousState = False
counter = 0

while True:
    if photoint.value:
        if previousState == False:
            counter += 1
            previousState = True
    else:
        previousState = False
    if time.monotonic() % 4 == 0:
        print("The number of interrupts is: " + str(counter))