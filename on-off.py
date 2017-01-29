#!/usr/local/bin/python
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
#backlight on off pin tanımlama
pin_onoff = 38
GPIO.setup(pin_onoff, GPIO.IN)
try:
	# Main loop
	while True:
		okunan = GPIO.input(pin_onoff)
		if okunan == HIGH:
			echo 0 > /sys/class/backlight/rpi_backlight/bl_power
		else:
			echo 1 > /sys/class/backlight/rpi_backlight/bl_power
		time.sleep(2) 
finally:
	GPIO.cleanup()
