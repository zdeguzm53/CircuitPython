# CircuitPython
### CircuitPython Assignments 


- BUTTON_LCD
   - *Overview*
   \
      An lcd displays the number of button presses, and a switch determines if the count is increasing or decreasing.
      
   - *Wiring Diagram*
   \
   ![button_lcd_pic](pictures/button_lcd_pic.png)
   - *Reflections*
   \
   I think a confusing aspect of this was the fact that the switch or button value was considered "True" if it was off. This resulted in a few minor mistakes, such as the button counting the number of the time it *wasn't* pressed instead. Other than that, it was pretty simple; the only major error made at first was that the wrong type of LCD was initially declared so it couldn't compile. 
- CAPTOUCH_SERVO
   - *Overview*
   \
      A servo spins in a certain direction depending on which wire is being touched, and if no wire is touched it stays still. The servo        being used isn't continuous, so when it has traveled 180 degrees without a command for a direction change, it will quickly turn back      and start the cycle again.
      
   - *Wiring Diagram*
   - *Reflections*
   \
   A new initializer, touchio, was used to declare the location of the wires that would change the direction of the servos when they are touched. The only issue that occurred was needing to change the boundaries of the servo in the code. If it reached 180 or 0 degrees then the program would throw an error statement. I ended up changing the limits to 179.9 and 0.1.

- FADING_LED
   - *Overview*
   \
      The code uses a pwm to continuously alter the brightness value of the led, resulting in a fading effect.
      
   - *Wiring Diagram*
   - *Reflections*
   \
   This assignment was really straightforward, the only new syntax I used was the "elif" command, which is similar to an "else" statement.

- PHOTOINTERRUPTER
   - *Overview*
   \
      This keeps track of the number of times a photointerrupter's led has been blocked, and then will display the running total on the       serial monitor every four seconds. 
      
   - *Wiring Diagram*
   - *Reflections*
   \
   The code and wiring for this assignment was relatively easy because we have used photointerrupters before. But the one aspect that required some additional research was finding an method to delay the serial monitor output without using time.sleep(). I used time.monotonic(), which records the time in seconds since the program began running. I also used mod (%) which calculates the remainder of a division expression. 

- RGB
   - *Overview*
   \
     This file contains both the class rgb and the tester. The class contains the constructor to create an led object, as well as methods that can change the color of the led by assigning it different values for red, green, and blue. The class gets imported into the tester in order to minimize the amount of necessary code in the main file. It creates a real RGB object out of the class and employs the different methods that were created.
      
   - *Wiring Diagram*
   - *Reflections*
   \
   One of the errors I made was assigning the wrong values to red, green, and blue. Because of the way the leds were wired, a value of 255 for a color would pull it to ground, which would turn it off. So the brightest colors within the led would actually be the ones with a value closest to zero. Until I fixed this, the led would display the opposite of the intended color. The red() function would actually turn it cyan, and the yellow() function would turn it blue.


- ULTRASONIC_SENSOR
   - *Overview*
   \
     The circuitpython metro device comes with an internal RGB led, so it was unnecessary to wire an additional RGB led for this assignment. An HCSR04 ultrasonic sensor judges the distance of an object in centimeters, and then changes the color of the led based on that number. The light fades between colors by adjusting the values of red, green, and blue. If the distance is too large and out of range, it throws a runtime error and prints "Retrying" until the object is close enough to the sensor. Otherwise, it will just print the distance on the serial monitor. 
      
   - *Wiring Diagram*
   - *Reflections*
   \
   At first I used if/else statements to change the color based on the distance range that it was in, but then I changed the code to add or substract red, green, and blue values based on if the distance increased or decreased. These values were kept track of with a for loop, and resulted in the led fading colors instead of just switching between them abruptly.

- TWO_FANCY
   - *Overview*
   \
     This folder contains two files: the class fancyLED and the main runner two_fancy. A fancyLED object is simply 3 separately wired leds that interact with each other because of the code in the class. It contains a contstructor and 5 methods: alternate(), blink(), chase(), sparkle(), and off(). The main file just declares a real object from the pin numbers of wired leds and calls the methods from the class.   
      
   - *Wiring Diagram*
   - *Reflections*
   \
   Aside from having to wire six separate leds to the breadboard, the wiring and code was very straightforward. Once it was working I just experimented with the code to get the effect I wanted.

- HELLO_VS_CODE
   - *Overview*
   \
     This assignment was simply to test the program VS Code, so it didn't use the metro or a complicated code. The code I decided to write analyzed the number of seconds that passed since running it, then printed that value if it was an integer. 
      
   - *Reflections*
   \
   VS Code was a different program than the one we had been using, but the syntax was still the same. The only major difference is that you have to write *#pylint: disable-msg=import-error* when importing a library. It is also easier to upload to GitHub with this program because it allows you to add and commit your changes immediately, as opposed to having to open GitBash and go through a long process.

