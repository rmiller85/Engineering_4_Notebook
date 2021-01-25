import RPi.GPIO as GPIO
from time import sleep

count = 10
#sets number of times to loop
GPIO.setmode(GPIO.BOARD)
#setmode needed before setup
GPIO.setup(11, GPIO.OUT)
#number 11 for pin 17 on the pi

while count > 0:
  #loops (and LED blinks) until counter reaches zero
  GPIO.output(11, 1)
  sleep(0.5)
  GPIO.output(11, 0)
  sleep(0.5)
  count -= 1
