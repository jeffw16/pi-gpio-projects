import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
pinraw = raw_input('Pin number: ')
pin = int(pinraw)
secraw = raw_input('Interval in seconds: ')
sec = int(secraw)
GPIO.setup(pin, GPIO.OUT)
state = False
while 1:
	GPIO.output(pin, state)
	time.sleep(sec)
	state = not state
GPIO.cleanup()
