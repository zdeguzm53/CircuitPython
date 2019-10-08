from digitalio import DigitalInOut, Direction
import time

class FancyLED:

     def __init__(self, led1, led2, led3):
         self.LED1 = DigitalInOut(led1)
         self.LED1.direction = Direction.OUTPUT
         self.LED2 = DigitalInOut(led2)
         self.LED2.direction = Direction.OUTPUT
         self.LED3 = DigitalInOut(led3)
         self.LED3.direction = Direction.OUTPUT

     def alternate(self):
        for x in range(0, 5):
            self.LED1.value = True
            self.LED2.value = False
            self.LED3.value = False
            time.sleep(1)
            self.LED1.value = False
            self.LED2.value = True
            self.LED3.value = False
            time.sleep(1)
            self.LED1.value = False
            self.LED2.value = False
            self.LED3.value = True
          
     def blink(self):
         for x in range(0, 5):
            self.LED1.value = True
            self.LED2.value = True
            self.LED3.value = True
            time.sleep(1)
            self.LED1.value = False
            self.LED2.value = False
            self.LED3.value = False

     def chase(self):
        for x in range(0, 5):
            self.LED1.value = True
            self.LED2.value = False
            self.LED3.value = False
            time.sleep(.05)
            self.LED1.value = False
            self.LED2.value = True
            self.LED3.value = False
            time.sleep(.05)
            self.LED1.value = False
            self.LED2.value = False
            self.LED3.value = True

   #  def sparkle(self):
