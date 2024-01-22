from machine import Pin, SPI
from max7219 import Matrix8x8


spi = SPI(0, baudrate=10000000, polarity=1, phase=0, sck=Pin(2), mosi=Pin(3))
ss = Pin(5, Pin.OUT)

display = Matrix8x8(spi, ss, 4)  #number of ledMatrix

# change brightness 1-15
display.brightness(1)

# clear display
display.zero()
display.show()

# show text using FrameBuffer's font
display.text("CODE")
display.show()
