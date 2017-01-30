#!/usr/local/bin/python
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
#ldr okuma pini tanimlama
pin_to_ldr = 40
def smooth (deger):
	bli = open('/sys/class/backlight/rpi_backlight/brightness','w')
        bli.write(deger)
        bli.close()
def rc_time (pin_to_ldr):
	count = 0
  
	#Output on the pin for 
	GPIO.setup(pin_to_ldr, GPIO.OUT)
	GPIO.output(pin_to_ldr, GPIO.LOW)
	time.sleep(0.01)

	#Change the pin back to input
	GPIO.setup(pin_to_ldr, GPIO.IN)
	#Count until the pin goes high
	while (GPIO.input(pin_to_ldr) == GPIO.LOW):
        	count += 1

	return count

#Catch when script is interrupted, cleanup correctly
try:
	# Main loop
	while True:
		okunan = 0
		okunan = rc_time(pin_to_ldr)
		if okunan <= 1500:
			smooth('200')
		elif okunan <= 5000:
       			smooth('150')
		elif okunan <= 15000:
        		smooth('120')
		elif okunan <= 25000:
        		smooth('90')
		elif okunan <= 50000:
        		smooth('70')
		elif okunan <= 100000:
        		smooth('50')
		elif okunan <= 140000:
			smooth('30')
		else:
			smooth('20')
		time.sleep(3) 
finally:
	GPIO.cleanup()
