import control
import RPi.GPIO as GPIO
import time
try: 
  GPIO.setmode(GPIO.BOARD)
  pin = [None]*4
  pin[0] = int(raw_input('Forward pin: '))
  pin[1] = int(raw_input('Backward pin: '))
  pin[2] = int(raw_input('Left pin: '))
  pin[3] = int(raw_input('Right pin: '))
  GPIO.setup(pin, GPIO.OUT)
  ct = Control(pin)
  finished = False
  while not finished:
  	cmd = raw_input('Enter command or type Q to quit: ')
  	hlg = raw_input('How long (sec): ')
  	qry = cmd.strip().upper()
  	if qry.startswith("Q"):
  		break
  	elif qry == 'F':
  	  ct.forward_on()
  	  time.sleep(hlg)
  	  ct.forward_off()
  	elif qry == 'B':
  	  ct.backward_on()
  	  time.sleep(hlg)
  	  ct.backward_off()
  	elif qry == 'L':
  	  ct.left_on()
  	  time.sleep(hlg)
  	  ct.left_off()
  	elif qry == 'R':
  	  ct.right_on()
  	  time.sleep(hlg)
  	  ct.right_off()
finally:
  GPIO.cleanup()
