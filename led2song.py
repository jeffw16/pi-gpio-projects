import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
pinraw1 = raw_input('Pin 1 number: ')
pin1 = int(pinraw1)
pinraw2 = raw_input('Pin 2 number: ')
pin2 = int(pinraw2)
minutesraw = raw_input('Song length (min): ')
minutes = float(minutesraw)
secondsraw = raw_input('Song length (sec): ')
seconds = float(secondsraw)
length = (minutes * 60) + seconds
bpmraw = raw_input('Beats per minute: ')
bpm = float(bpmraw)
bps = bpm / 60
sec = 1.0 / bps
statediffraw = raw_input('Same (0) or alternate (1): ')
statediff = int(statediffraw)
GPIO.setup(pin1, GPIO.OUT)
GPIO.setup(pin2, GPIO.OUT)
if ( statediff == 1 ):
	state1 = False
	state2 = True
else:
	state1 = False
	state2 = False
count = 0
while count < ( bps * length ):
	GPIO.output(pin1, state1)
	GPIO.output(pin2, state2)
	time.sleep(sec)
	state1 = not state1
	state2 = not state2
	count = count + 1
print ( 'Finished' )
GPIO.cleanup()
