import time

while True:
 if time.monotonic() % 1 == 0:
    print(time.monotonic())