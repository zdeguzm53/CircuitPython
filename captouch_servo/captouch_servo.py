import time #pylint: disable-msg=import-error
import board #pylint: disable-msg=import-error
import pulseio #pylint: disable-msg=import-error
import touchio #pylint: disable-msg=import-error
import adafruit_motor #pylint: disable-msg=import-error
from adafruit_motor import servo #pylint: disable-msg=import-error

pwm = pulseio.PWMOut(board.A2, duty_cycle=2 ** 15, frequency=50)
touch_pad = board.A3 #pin for first touch wire
touch_pad2 = board.A5 #pin for second touch wire
my_servo = servo.Servo(pwm)
touch = touchio.TouchIn(touch_pad) 
touch2 = touchio.TouchIn(touch_pad2)
my_servo.angle = 90 #puts servo in the middle

while True:

    if touch.value: #if first touch wire is being pushed
        if my_servo.angle > 179.1: #if it reached 180 degrees
            my_servo.angle = 1 #go back to 1 degree
        else: #if it is between 1 and 180 degrees
            my_servo.angle += 1 #keep moving to the right
        print(my_servo.angle) #print angle
        time.sleep(0.05)
    if touch2.value: #if second wire is touched
        if my_servo.angle < .9: #if it reached 1 degree
            my_servo.angle = 179 #go back to 179 degrees
        else: #if it is between 1 and 179
            my_servo.angle -= 1 #move to the left
        print(my_servo.angle)
        time.sleep(0.05)