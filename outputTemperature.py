#!/usr/bin/env python
# -*- coding: utf-8 -*-

HOST = "localhost"
PORT = 4223
UID_MASTER      = "9yCqfWBSqDQ"
UID_LCD         = "bmA"
UID_TEMPERATURE = "bPf"
UID_BAROMETER   = "bNs"

from tinkerforge.ip_connection import IPConnection
from tinkerforge.brick_master import Master
from tinkerforge.bricklet_lcd_20x4 import LCD20x4
from tinkerforge.bricklet_temperature import Temperature
from tinkerforge.bricklet_barometer import Barometer

from string_magic import unicode_to_ks0066u

if __name__ == "__main__":
    ipcon = IPConnection(HOST, PORT) # Create IP connection to brick

    master = Master(UID_MASTER) # Create device object
    ipcon.add_device(master) # Add device to IP connection
    # Don't use device before it is added to a connection

    ## Get voltage and current from stack (in mV / mA)
    #voltage = master.get_stack_voltage()
    #current = master.get_stack_current()

    ##print('Stack Voltage: ' + str(voltage / 1000.0) + ' V')
    ##print('Stack Current: ' + str(current / 1000.0) + ' A')
 
    t = Temperature(UID_TEMPERATURE) # Create temperature object
    ipcon.add_device(t) # Add device to IP connection
    # Don't use device before it is added to connection

    # Get current temperature (unit is °C/ 100)
    temperature = t.get_temperature() / 100.0

    b = Barometer(UID_BAROMETER) # Create barometer object
    ipcon.add_device(b) # Add device to IP connection
    # Don't use device before it is added to the connection

    # Get the current air pressure (unit is mbar/1000)
    air_pressure = round(b.get_air_pressure()/1000.0, 1)

    #print('Temperature: ' + str(temperature) + ' °C')

    lcd = LCD20x4(UID_LCD) # Create LCD object
    ipcon.add_device(lcd)  # Add device to IP connection
    # Don't use device before it is added to a connection

    # Clear display
    lcd.clear_display()

    # Turn backlight on
    lcd.backlight_on()

    # Write on the LCD
    lcd.write_line(0, 0, unicode_to_ks0066u('°C:   ' + str(temperature)))
    lcd.write_line(1, 0, unicode_to_ks0066u('mbar: ' + str(air_pressure)))

    raw_input('Press key to exit\n')

    # Turn backlight off
    lcd.backlight_off()
 
    ipcon.destroy()


