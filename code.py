import usb_hid
from adafruit_hid.mouse import Mouse
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
import digitalio
from file_handler import FileHandler
import time
import board
import bitbangio
import busio

i2c = bitbangio.I2C(board.GP1, board.GP0)  #connect RTC to correct pins on Pico: GP1-SDA, GP0-SCL

import adafruit_ds3231
rtc = adafruit_ds3231.DS3231(i2c)  #for real time clock

days = ("Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday")

set_time = False # Only set this to True when setting the time initially

if set_time:   
    rtc.datetime = time.struct_time((2024,  2,   4,   16,  22,  54,    2,   -1,    -1)) #setting year, mon, date, hour, min, sec and weekday
    print("Setting time to:", rtc.datetime)     

t = rtc.datetime
#print(t) #can uncomment to debug

#Initialize mouse
mouse = Mouse(usb_hid.devices)
# Initialize Keyboard
kbd = Keyboard(usb_hid.devices)

time.sleep(10) #remove so no delay
    
shutoff_hour = 14 #at least before midnight
shutoff_minute = 17
shutoff_time = (shutoff_hour*3600) + (shutoff_minute*60) #seconds
current_time = (t.tm_hour*3600) + (t.tm_min*60) #seconds
wait_time = shutoff_time - current_time  #seconds
#print("Seconds until shutdown:", wait_time) #uncomment to debug in thonny

if wait_time > 0: #if there is time remaining until shutdown
    time.sleep(wait_time) #wait until shutoff time
    Keyboard keys to shut off Somaris 7 interface scanner
    kbd.press(Keycode.ALT)  
    kbd.release(Keycode.ALT)
    time.sleep(0.2)
    kbd.press(Keycode.Y)
    kbd.release(Keycode.Y)
    time.sleep(0.2)
    kbd.press(Keycode.E)
    kbd.release(Keycode.E)
    time.sleep(0.2)
    kbd.press(Keycode.S)
    kbd.release(Keycode.S)
    time.sleep(0.2)
    kbd.press(Keycode.Y)
    kbd.release(Keycode.Y)
    time.sleep(10)
    kbd.press(Keycode.Y)
    kbd.release(Keycode.Y)
    time.sleep(0.2)
else:
    kbd.press(Keycode.ALT)  
    kbd.release(Keycode.ALT)
    time.sleep(0.2)
    kbd.press(Keycode.Y)
    kbd.release(Keycode.Y)
    time.sleep(0.2)
    kbd.press(Keycode.E)
    kbd.release(Keycode.E)
    time.sleep(0.2)
    kbd.press(Keycode.S)
    kbd.release(Keycode.S)
    time.sleep(0.2)
    kbd.press(Keycode.Y)
    kbd.release(Keycode.Y)
    time.sleep(10)
    kbd.press(Keycode.Y)
    kbd.release(Keycode.Y)
    time.sleep(0.2)
