#!/usr/local/bin/python
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
#backlight on off pin tanimlama
pin_onoff = 38
GPIO.setup(pin_onoff, GPIO.IN)
try:
        # Main loop
        while True:
                okunan = GPIO.input(pin_onoff)
                bl = open('/sys/class/backlight/rpi_backlight/bl_power','w')
                print(okunan)
                if okunan == 1 :
                        bl.write('1')
                else:
                        bl.write('0')
                bl.close()
                time.sleep(2)
finally:
        GPIO.cleanup()
