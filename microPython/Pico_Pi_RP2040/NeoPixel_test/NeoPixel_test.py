import math
import neopixel

from machine import Pin

xres = 8
yres = 8
pin = 22

wall = neopixel.NeoPixel(machine.Pin(pin), xres, yres)
wall.write()

def mapPixel(x,y):
    if y % 2 == 1:
        return xres * y + x
    else:
        return xres * y + xres - 1 - x
    
a0 = 0
a1 = 0

# show color
while True:
    a0 += 0.1
    a1 += 0.2
    for y in range(yres):
      for x in range(xres):
          r = 128 + math.floor((math.sin(a0 + x * 0.4 ) + math.cos(a1 + y * 0.4 )) * 63)
          g = 128 + math.floor((math.sin(a0 + y * 0.4 ) + math.cos(a1 + x * 0.4 )) * 63)
          b = 255 - r
          wall[mapPixel(x,y)] = (r >> 3, g >> 3, b >> 4)
    wall.write()      
    
