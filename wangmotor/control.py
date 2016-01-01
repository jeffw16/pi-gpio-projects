import RPi.GPIO as GPIO
import time
class control:
	
	# pins for
	# left, right, forward, backward
	pinf = 13
	pinb = 19
	pinl = 29
	pinr = 40
	
	def __init__ ( gpio ):
		GPIO.setmode(GPIO.BOARD)
		GPIO.setwarnings(False)
		# Set up GPIO pins
		# goes through array gpio, sets up each GPIO to be outputs
		for x in xrange(0, len(gpio)):
			GPIO.setup( gpio[x], GPIO.OUT)
	
	def __del__ ():
		GPIO.cleanup()
	
	def forward_on ():
		GPIO.output( pinf, True )
	
	def forward_off ():
		GPIO.output( pinf, False )
	
	def backward_on ():
		GPIO.output( pinb, True )
	
	def backward_off ():
		GPIO.output( pinb, False )
	
	def left_on ():
		GPIO.output( pinl, True )
	
	def left_off ():
		GPIO.output( pinl, False )
	
	def right_on ():
		GPIO.output( pinr, True )
	
	def right_off ():
		GPIO.output( pinr, False )
