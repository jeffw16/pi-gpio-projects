import RPi.GPIO as GPIO
import time
try:
	GPIO.setmode(GPIO.BOARD)
	GPIO.setwarnings(False)
	combien = int(raw_input('How many pins? '))
	if combien < 2:
		print('Not possible')
		exit()
	j = 0
	pin = [None]*combien
	while j < combien:
		pin[j] = int(raw_input('Pin ' + str(j+1) + ' location: '))
		GPIO.setup(pin[j], GPIO.OUT)
		GPIO.output(pin[j], False)
		j = j+1
	sec = float(raw_input('Interval in seconds: '))
	duoshao = int(raw_input('How many sequences? '))
	go = True
	while go:
		statediff = int(raw_input('Same (0), alternate (1), or sequential boolean (2): '))
		pinstate = [None]*combien
		for k in xrange(0, len(pin)):
			pinstate[k] = False
		count = 0
		while count < (duoshao * combien):
			if statediff == 1:
				GPIO.output(pin[count%combien], True)
				time.sleep(sec)
				#pinstate[count%combien] = not pinstate[count%combien]
				GPIO.output(pin[count%combien], False)
			elif statediff == 2:
				GPIO.output(pin[count%combien], pinstate[count%combien])
				time.sleep(sec)
				pinstate[count%combien] = not pinstate[count%combien]
				GPIO.output(pin[count%combien], pinstate[count%combien])
			else:
				for m in xrange(0, len(pin)):
					GPIO.output(pin[m], pinstate[m])
					pinstate[m] = not pinstate[m]
					time.sleep(sec)
			count = count + 1
		time.sleep(sec)
		queryagain = int(raw_input('Go again? Yes - 1, No, 0: '))
		if queryagain == 0:
			go = False
	print ( 'Finished' )
finally:
	GPIO.cleanup()
