# Example from: https://sourceforge.net/p/raspberry-gpio-python/wiki/PWM/
# Addition of customization by Jeffrey Wang
import time
import RPi.GPIO as GPIO
# Default channel, frequency
channel = 5
frequency = 50 # Hz
# Prompt
channel = int( raw_input( "Channel: " ) )
frequency = int( raw_input( "Frequency (default 50Hz): " ) )
GPIO.setmode(GPIO.BOARD)
GPIO.setup(channel, GPIO.OUT)

p = GPIO.PWM(channel, frequency)  # channel=12 frequency=50Hz
p.start(0)
try:
    while 1:
        for dc in range(0, 101, 5):
            p.ChangeDutyCycle(dc)
            time.sleep(0.1)
        for dc in range(100, -1, -5):
            p.ChangeDutyCycle(dc)
            time.sleep(0.1)
except KeyboardInterrupt:
    pass
p.stop()
GPIO.cleanup()
