#!/usr/local/bin/python
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
#ldr okuma pini tanimlama
pin_to_ldr = 40
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
		bl = open('/sys/class/backlight/rpi_backlight/brightness','w')
		okunan = 0
		okunan = rc_time(pin_to_ldr)
		if okunan <= 1500:
			bl.write('200')
		elif okunan <= 5000:
       			bl.write('160')
		elif okunan <= 15000:
        		bl.write('130')
		elif okunan <= 30000:
        		bl.write('100')
		elif okunan <= 50000:
        		bl.write('75')
		elif okunan <= 100000:
        		bl.write('50')
		elif okunan <= 140000:
			bl.write('30')
		else:
			bl.write('20')
		bl.close()
		time.sleep(5) 
finally:
	GPIO.cleanup()
