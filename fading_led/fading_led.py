# fading led

import time

import board
import pulseio
from digitalio import DigitalInOut, Direction

pwm_leds = board.D0
pwm = pulseio.PWMOut(pwm_leds, frequency=1000, duty_cycle=0)

digital_leds = DigitalInOut(board.D2)
digital_leds.direction = Direction.OUTPUT
brightness = 0
fade_amount = 1285
counter = 0

while True:

    pwm.duty_cycle = brightness

    brightness = brightness + fade_amount

    print(brightness)

    if brightness <= 0:
        fade_amount = -fade_amount
        counter += 1
    elif brightness >= 65535:
        fade_amount = -fade_amount
        counter += 1

    time.sleep(.015)

    if counter % 4 == 0:
        digital_leds.value = True
    else:
        digital_leds.value = False