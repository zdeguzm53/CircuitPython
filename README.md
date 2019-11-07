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


- RGB
   - *Overview*
   \
     This file contains both the class rgb and the tester. The class contains the constructor to create an led object, as well as methods that can change the color of the led by assigning it different values for red, green, and blue. The class gets imported into the tester in order to minimize the amount of necessary code in the main file. It creates a real RGB object out of the class and employs the different methods that were created.
      
   - *Wiring Diagram*
   - *Reflections*


- ULTRASONIC_SENSOR
   - *Overview*
   \
     The circuitpython metro device comes with an internal RGB led, so it was unnecessary to wire an additional RGB led for this assignment. An HCSR04 ultrasonic sensor judges the distance of an object in centimeters, and then changes the color of the led based on that number. The light fades between colors by adjusting the values of red, green, and blue. If the distance is too large and out of range, it throws a runtime error and prints "Retrying" until the object is close enough to the sensor. Otherwise, it will just print the distance on the serial monitor. 
      
   - *Wiring Diagram*
   - *Reflections*


- TWO_FANCY
   - *Overview*
   \
     This folder contains two files: the class fancyLED and the main runner two_fancy. A fancyLED object is simply 3 separately wired leds that interact with each other because of the code in the class. It contains a contstructor and 5 methods: alternate(), blink(), chase(), sparkle(), and off(). The main file just declares a real object from the pin numbers of wired leds and calls the methods from the class.   
      
   - *Wiring Diagram*
   - *Reflections*


- HELLO_VS_CODE
   - *Overview*
   \
     This assignment was simply to test the program VS Code, so it didn't use the metro or a complicated code. The code I decided to write analyzed the number of seconds that passed since running it, then printed that value if it was an integer. 
      
   - *Reflections*


