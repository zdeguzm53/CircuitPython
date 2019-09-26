from digitalio import DigitalInOut, Direction

class RGB:

     def __init__(self, red, green, blue):
         self.RED_LED = DigitalInOut(red)
         self.RED_LED.direction = Direction.OUTPUT
         self.GREEN_LED = DigitalInOut(green)
         self.GREEN_LED.direction = Direction.OUTPUT
         self.BLUE_LED = DigitalInOut(blue)
         self.BLUE_LED.direction = Direction.OUTPUT

     def red(self):
          self.RED_LED.value = 0
          self.GREEN_LED.value = 255
          self.BLUE_LED.value = 255

     def green(self):
          self.RED_LED.value = 255
          self.GREEN_LED.value = 0
          self.BLUE_LED.value = 255

     def blue(self):
          self.RED_LED.value = 255
          self.GREEN_LED.value = 255
          self.BLUE_LED.value = 0

     def yellow(self):
          self.RED_LED.value = 0
          self.GREEN_LED.value = 0
          self.BLUE_LED.value = 255

     def magenta(self):
          self.RED_LED.value = 0
          self.GREEN_LED.value = 255
          self.BLUE_LED.value = 0

     def cyan(self):
          self.RED_LED.value = 255
          self.GREEN_LED.value = 0
          self.BLUE_LED.value = 0