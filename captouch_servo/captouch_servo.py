import time
import board
import pulseio
import touchio
import adafruit_motor
from adafruit_motor import servo

pwm = pulseio.PWMOut(board.A2, duty_cycle=2 ** 15, frequency=50)
touch_pad = board.A3
touch_pad2 = board.A5
my_servo = servo.Servo(pwm)
touch = touchio.TouchIn(touch_pad)
touch2 = touchio.TouchIn(touch_pad2)
my_servo.angle = 90

while True:

    if touch.value:
        if my_servo.angle > 179.1:
            my_servo.angle = 1
        else:
            my_servo.angle += 1
        print(my_servo.angle)
        time.sleep(0.05)
    if touch2.value:
        if my_servo.angle < .9:
            my_servo.angle = 179
        else:
            my_servo.angle -= 1
        print(my_servo.angle)
        time.sleep(0.05)