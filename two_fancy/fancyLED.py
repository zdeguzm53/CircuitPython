from digitalio import DigitalInOut, Direction #pylint: disable-msg=import-error
import time

class FancyLED:

     #declare object as 3 separate leds
     #define pin number and that it is an output
     def __init__(self, led1, led2, led3):
         self.LED1 = DigitalInOut(led1)
         self.LED1.direction = Direction.OUTPUT
         self.LED2 = DigitalInOut(led2)
         self.LED2.direction = Direction.OUTPUT
         self.LED3 = DigitalInOut(led3)
         self.LED3.direction = Direction.OUTPUT

     #slowly switches which led is on
     def alternate(self):
        for x in range(0, 5): #loop through 5 times
            print(x)
            self.LED1.value = True
            self.LED2.value = False
            self.LED3.value = False
            time.sleep(1) #stay on for 1 second
            self.LED1.value = False
            self.LED2.value = True
            self.LED3.value = False
            time.sleep(1)
            self.LED1.value = False
            self.LED2.value = False
            self.LED3.value = True
            time.sleep(1)

     #slowly blinks all leds at the same time     
     def blink(self):
         for x in range(0, 5): #turn on and off 5 times
            print(x)
            self.LED1.value = True
            self.LED2.value = True
            self.LED3.value = True
            time.sleep(1)
            self.LED1.value = False
            self.LED2.value = False
            self.LED3.value = False
            time.sleep(1)
            
     #quickly alternates which led is on
     def chase(self):
        for x in range(0, 10): #loops through 10 times
            print(x)
            self.LED1.value = True
            self.LED2.value = False
            self.LED3.value = False
            time.sleep(.1) #only rests for 1/10th of a second
            self.LED1.value = False
            self.LED2.value = True
            self.LED3.value = False
            time.sleep(.1)
            self.LED1.value = False
            self.LED2.value = False
            self.LED3.value = True
            time.sleep(.1)

     #all leds are off for 3 seconds
     def off(self):
        self.LED1.value = False
        self.LED2.value = False
        self.LED3.value = False
        time.sleep(3)

     #all 3 leds blink very quickly at the same time
     def sparkle(self):
         for x in range(0, 30): #blinks 30 times
            print(x)
            self.LED1.value = True
            self.LED2.value = True
            self.LED3.value = True
            time.sleep(.05) #stays on for 1/20th of a second
            self.LED1.value = False
            self.LED2.value = False
            self.LED3.value = False
            time.sleep(.05)
