
from machine import Pin , UART
import time

led = Pin(13, Pin.OUT)

while True:
    led.value(1)
    time.sleep(.75)
    led.value(0)
    time.sleep(.75)

