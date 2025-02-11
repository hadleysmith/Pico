# Pico
Contains code for Raspberry Pi Pico to perform automatic CT shutdown

code.py contains preliminary code for performing automatic CT shutdown on a Somaris 7 interface. 
NOTE: this code is NOT robust to all system states, and is provided here in the interest of education and giving open access for a low-cost, implementable solution for automated CT shutdown. Code and processes should not be used without customization.

Additional modules for lib:
  adafruit_bus_device \\
  adafruit_hid \\
  adafruit_ds3231.py (for RTC functionality, specific for DS3231 timeclock. For more information, see: https://learn.adafruit.com/adafruit-ds3231-precision-rtc-breakout/circuitpython)\\
  adafruit_register\\
  
