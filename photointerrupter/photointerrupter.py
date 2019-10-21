import time #pylint: disable-msg=import-error
import board #pylint: disable-msg=import-error
import adafruit_bus_device #pylint: disable-msg=import-error
from digitalio import DigitalInOut, Direction, Pull #pylint: disable-msg=import-error

photoint = DigitalInOut(board.D2) #pin number on board
photoint.direction = Direction.INPUT #declares as input 
photoint.pull = Pull.UP #doesn't send it to ground

previousState = False #most recent state is uninterrupted
counter = 0 #number of interrupts

while True:
    if photoint.value: #if interrupted
        if previousState == False: #if it was just off
            counter += 1 #add another interrupt to the total
            previousState = True #change most recent state to interrupted
    else: #if unblocked
        previousState = False #no change
    if time.monotonic() % 4 == 0: #prints every 4 seconds
        print("The number of interrupts is: " + str(counter))