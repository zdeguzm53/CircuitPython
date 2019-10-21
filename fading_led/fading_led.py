# fading led

import time #pylint: disable-msg=import-error
import board #pylint: disable-msg=import-error
import pulseio #pylint: disable-msg=import-error
from digitalio import DigitalInOut, Direction #pylint: disable-msg=import-error

#set up pwm (pulse)
pwm_leds = board.D0 
pwm = pulseio.PWMOut(pwm_leds, frequency=1000, duty_cycle=0)

digital_leds = DigitalInOut(board.D2) #led pin number
digital_leds.direction = Direction.OUTPUT #declare led as output
brightness = 0 #led is off at first
fade_amount = 1285 #how much the led will change at a time
counter = 0

while True:

    pwm.duty_cycle = brightness #send to LED as PWM level

    brightness = brightness + fade_amount #change the brightness for next loop

    print(brightness)

    #reverse direction at the end of the cycle
    if brightness <= 0:
        fade_amount = -fade_amount
        counter += 1
    elif brightness >= 65535:
        fade_amount = -fade_amount
        counter += 1

    time.sleep(.015) #wait 15 ms to see dimming effect

    if counter % 4 == 0:
        digital_leds.value = True
    else:
        digital_leds.value = False