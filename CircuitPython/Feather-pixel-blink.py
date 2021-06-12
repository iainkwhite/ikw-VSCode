import time
import board
import digitalio
import neopixel

COLOR = (255, 50, 150)  # color to blink
CLEAR = (0, 0, 0)  # clear (or second color)
DELAY = 0.5  # blink rate in seconds

led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT
pixel = neopixel.NeoPixel(board.NEOPIXEL, 1)
pixel.brightness = 0.1

while True:
    led.value = True
    pixel.fill((255, 0, 0))
    time.sleep(1)
    pixel.fill((0, 255, 0))
    time.sleep(1)
    led.value = False
    pixel.fill((0, 0, 255))
    time.sleep(1)
