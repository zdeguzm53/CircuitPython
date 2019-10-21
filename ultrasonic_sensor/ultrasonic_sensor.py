import time
import board #pylint: disable-msg=import-error
from adafruit_hcsr04 import HCSR04 #pylint: disable-msg=import-error
import neopixel #pylint: disable-msg=import-error 

 #declares light on the metro
light = neopixel.NeoPixel(board.NEOPIXEL, 1)

 #declares pins for the sensor
trig = board.D2
echo = board.D3
sonar = HCSR04(trig, echo)

#initial color values
red = 0
green = 0
blue = 0

while True:
    try: #if the diatance is in range
        print(int(sonar.distance)) #print distance in cm
        print(str(red) + " " + str(green) + " " + str(blue)) #print color values
        if int(sonar.distance) < 20:
            blue = int(sonar.distance) #blue decreases as distance decreases
            red = 20 - int(sonar.distance) #red increases as distance decreases
            green = 0 #light is never green when distance is under 20 cm
        if int(sonar.distance) >= 20 and int(sonar.distance) < 35:
            green = int(sonar.distance) #green increases as distance increases
            blue = 35 - int(sonar.distance) #blue decreases as distance increases
            red = 0 #never red between 20 and 35 cm
        if int(sonar.distance) >= 35:
            green = 35 #always green when distance is over 35 cm
            red = 0
            blue = 0
        light.fill((red, green, blue)) #turn on led with those color values
        time.sleep(.5)
    except RuntimeError: #when distance is too far away for the sensor
        print("Retrying!")
        time.sleep(.5) #waits until distance is in range
        pass
