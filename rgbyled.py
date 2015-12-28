import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
red = int(raw_input('Red pin: '))
green = int(raw_input('Green pin: '))
blue = int(raw_input('Blue pin: '))
yellow = int(raw_input('Yellow pin: '))
secraw = raw_input('Interval in seconds: ')
sec = float(secraw)
duoshaoraw = raw_input('Blink ? num of times?: ')
duoshao = int(duoshaoraw)
statediffraw = raw_input('Same (0) or alternate (1): ')
statediff = int(statediffraw)
GPIO.setup(red, GPIO.OUT)
GPIO.setup(green, GPIO.OUT)
GPIO.setup(blue, GPIO.OUT)
GPIO.setup(yellow, GPIO.OUT)
if ( statediff == 1 ):
	state1 = False
	state2 = True
	state3 = False
	state4 = True
else:
	state1 = False
	state2 = False
	state3 = False
	state4 = False
count = 0
while count < (duoshao * 2):
	GPIO.output(red, state1)
	GPIO.output(green, state2)
	GPIO.output(blue, state3)
	GPIO.output(yellow, state4)
	time.sleep(sec)
	state1 = not state1
	state2 = not state2
	state3 = not state3
	state4 = not state4
	count = count + 1
print ( 'Finished' )
GPIO.cleanup()
