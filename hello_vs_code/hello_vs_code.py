#basic code to test the program VS Code

import time #pylint: disable-msg=import-error

while True:
#print the number of seconds since the program began
#only if the number is an integer
 if time.monotonic() % 1 == 0:
    print(time.monotonic())