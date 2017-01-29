#!/bin/bash
sudo mkdir /opt/auto-backlight
cd /opt/auto-backlight
sudo wget https://raw.githubusercontent.com/ilhanakilli/rpi-auto-install/master/brightness.py --no-check-certificate
sudo wget https://raw.githubusercontent.com/ilhanakilli/rpi-auto-install/master/on-off.py --no-check-certificate
sudo echo 'sudo python /opt/auto-backlight/brightness.py &' >> /etc/rc.local
sudo echo 'sudo python /opt/auto-backlight/on-off.py &' >> /etc/rc.local
