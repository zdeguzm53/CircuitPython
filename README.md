# CircuitPython
### CircuitPython Assignments 


- BUTTON_LCD
   - *Overview*
   \
      An lcd displays the number of button presses, and a switch determines if the count is increasing or decreasing.
      
   - *Wiring Diagram*
   - *Reflections*

- CAPTOUCH_SERVO
   - *Overview*
   \
      A servo spins in a certain direction depending on which wire is being touched, and if no wire is touched it stays still. The servo        being used isn't continuous, so when it has traveled 180 degrees without a command for a direction change, it will quickly turn back      and start the cycle again.
      
   - *Wiring Diagram*
   - *Reflections*


- FADING_LED
   - *Overview*
   \
      The code uses a pwm to continuously alter the brightness value of the led, resulting in a fading effect.
      
   - *Wiring Diagram*
   - *Reflections*


- PHOTOINTERRUPTER
   - *Overview*
   \
      This keeps track of the number of times a photointerrupter's led has been blocked, and then will display the running total on the       serial monitor every four seconds. 
      
   - *Wiring Diagram*
   - *Reflections*



rgb:
   contains the class rgb and the tester
   has functions to intialize the led and change the color

ultrasonic_sensor:
   led on metro fades into different colors depending on the distance of an object from the sensor
