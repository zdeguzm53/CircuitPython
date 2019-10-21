from digitalio import DigitalInOut, Direction #pylint: disable-msg=import-error

class RGB:
     
     #declare object with a red pin, green pin, blue pin
     def __init__(self, red, green, blue):
         self.RED_LED = DigitalInOut(red)
         self.RED_LED.direction = Direction.OUTPUT
         self.GREEN_LED = DigitalInOut(green)
         self.GREEN_LED.direction = Direction.OUTPUT
         self.BLUE_LED = DigitalInOut(blue)
         self.BLUE_LED.direction = Direction.OUTPUT

     #only red is on
     def red(self):
          self.RED_LED.value = 0
          self.GREEN_LED.value = 255
          self.BLUE_LED.value = 255

     #only green is on
     def green(self):
          self.RED_LED.value = 255
          self.GREEN_LED.value = 0
          self.BLUE_LED.value = 255

     #only blue is on
     def blue(self):
          self.RED_LED.value = 255
          self.GREEN_LED.value = 255
          self.BLUE_LED.value = 0

     #only red and green are on
     def yellow(self):
          self.RED_LED.value = 0
          self.GREEN_LED.value = 0
          self.BLUE_LED.value = 255

     #only red and blue are on
     def magenta(self):
          self.RED_LED.value = 0
          self.GREEN_LED.value = 255
          self.BLUE_LED.value = 0

     #only blue and green are on
     def cyan(self):
          self.RED_LED.value = 255
          self.GREEN_LED.value = 0
          self.BLUE_LED.value = 0