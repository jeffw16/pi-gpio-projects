import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
pinraw = raw_input('Pin number: ')
pin = int(pinraw)
GPIO.setup(pin, GPIO.OUT)
state = False
while 1:
	GPIO.output(pin, state)
	cmd = raw_input('Press enter to turn LED on/off or press Q to quit: ')
	if cmd.strip().upper().startswith("Q"):
		GPIO.cleanup()
		break
	state = not state
GPIO.cleanup()
