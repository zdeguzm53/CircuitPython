import time
import board
from adafruit_hcsr04 import HCSR04
import neopixel

light = neopixel.NeoPixel(board.NEOPIXEL, 1)

trig = board.D2
echo = board.D3
sonar = HCSR04(trig, echo)

red = 0
green = 0
blue = 0

while True:
    try:
        print(int(sonar.distance))
        print(str(red) + " " + str(green) + " " + str(blue))
        if int(sonar.distance) < 20:
            blue = int(sonar.distance)
            red = 20 - int(sonar.distance)
            green = 0
        if int(sonar.distance) >= 20 and int(sonar.distance) < 35:
            green = int(sonar.distance)
            blue = 35 - int(sonar.distance)
            red = 0
        if int(sonar.distance) >= 35:
            green = 35
            red = 0
            blue = 0
        light.fill((red, green, blue))
        time.sleep(.5)
    except RuntimeError:
        print("Retrying!")
        time.sleep(.5)
        pass
