# CircuitPython
### CircuitPython Assignments 

- BUTTON_LCD:
\
   - **Overview**
   \
      An lcd displays the number of button presses, and a switch determines if the count is increasing or decreasing.

- CAPTOUCH_SERVO:

A servo spins in a certain direction depending on which wire is being touched, and if no wire is touched it stays still. The servo being used isn't continuous, so when it has traveled 180 degrees without a command for a direction change, it will quickly turn back and start the cycle again.

fading_led:
   code uses a pwm to fade an led

photointerrupter:
   keeps track on the number of times a photointerrupter has been blocked,
   displays the count every four seconds

rgb:
   contains the class rgb and the tester
   has functions to intialize the led and change the color

ultrasonic_sensor:
   led on metro fades into different colors depending on the distance of an object from the sensor
