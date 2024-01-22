#from ST7735 import tft
from sysfont import sysfont
from machine import SPI,Pin
import time
import math
from st7735_new import TFT

#LCD        ESP32-DevKitC
#VLED       3V3
#RST         IO17
#A0            IO16(DC)
#SDA         IO13(MOSI)
#SCK         IO14(CLK)
#VCC         3V3
#CS            IO18
#GND       GND

#VCC            3V3
#GND            GND
tft_CS = 12     #CS 
tft_RESET=14    #RESET
tft_A0=27       #DC
tft_SDA=26      #MOSI
tft_SCK=25      #CLK

spi = SPI(1, baudrate=20000000, polarity=0, phase=0,sck=Pin(25), mosi=Pin(26),miso=None)
tft = TFT(spi,tft_A0,tft_RESET,tft_CS)
tft.initr()
tft.rgb(True)

def testlines(color):
    tft.fill(TFT.BLACK)
    for x in range(0, tft.size()[0], 6):
        tft.line((0,0),(x, tft.size()[1] - 1), color)
    for y in range(0, tft.size()[1], 6):
        tft.line((0,0),(tft.size()[0] - 1, y), color)

    tft.fill(TFT.BLACK)
    for x in range(0, tft.size()[0], 6):
        tft.line((tft.size()[0] - 1, 0), (x, tft.size()[1] - 1), color)
    for y in range(0, tft.size()[1], 6):
        tft.line((tft.size()[0] - 1, 0), (0, y), color)

    tft.fill(TFT.BLACK)
    for x in range(0, tft.size()[0], 6):
        tft.line((0, tft.size()[1] - 1), (x, 0), color)
    for y in range(0, tft.size()[1], 6):
        tft.line((0, tft.size()[1] - 1), (tft.size()[0] - 1,y), color)

    tft.fill(TFT.BLACK)
    for x in range(0, tft.size()[0], 6):
        tft.line((tft.size()[0] - 1, tft.size()[1] - 1), (x, 0), color)
    for y in range(0, tft.size()[1], 6):
        tft.line((tft.size()[0] - 1, tft.size()[1] - 1), (0, y), color)

def testfastlines(color1, color2):
    tft.fill(TFT.BLACK)
    for y in range(0, tft.size()[1], 5):
        tft.hline((0,y), tft.size()[0], color1)
    for x in range(0, tft.size()[0], 5):
        tft.vline((x,0), tft.size()[1], color2)

def testdrawrects(color):
    tft.fill(TFT.BLACK);
    for x in range(0,tft.size()[0],6):
        tft.rect((tft.size()[0]//2 - x//2, tft.size()[1]//2 - x/2), (x, x), color)

def testfillrects(color1, color2):
    tft.fill(TFT.BLACK);
    for x in range(tft.size()[0],0,-6):
        tft.fillrect((tft.size()[0]//2 - x//2, tft.size()[1]//2 - x/2), (x, x), color1)
        tft.rect((tft.size()[0]//2 - x//2, tft.size()[1]//2 - x/2), (x, x), color2)


def testfillcircles(radius, color):
    for x in range(radius, tft.size()[0], radius * 2):
        for y in range(radius, tft.size()[1], radius * 2):
            tft.fillcircle((x, y), radius, color)

def testdrawcircles(radius, color):
    for x in range(0, tft.size()[0] + radius, radius * 2):
        for y in range(0, tft.size()[1] + radius, radius * 2):
            tft.circle((x, y), radius, color)

def testtriangles():
    tft.fill(TFT.BLACK);
    color = 0xF800
    w = tft.size()[0] // 2
    x = tft.size()[1] - 1
    y = 0
    z = tft.size()[0]
    for t in range(0, 15):
        tft.line((w, y), (y, x), color)
        tft.line((y, x), (z, x), color)
        tft.line((z, x), (w, y), color)
        x -= 4
        y += 4
        z -= 4
        color += 100

def testroundrects():
    tft.fill(TFT.BLACK);
    color = 100
    for t in range(5):
        x = 0
        y = 0
        w = tft.size()[0] - 2
        h = tft.size()[1] - 2
        for i in range(17):
            tft.rect((x, y), (w, h), color)
            x += 2
            y += 3
            w -= 4
            h -= 6
            color += 1100
        color += 100

def tftprinttest():
    tft.fill(TFT.BLACK);
    v = 30
    tft.text((0, v), "Hello World!", TFT.RED, sysfont, 1, nowrap=True)
    v += sysfont["Height"]
    tft.text((0, v), "Hello World!", TFT.YELLOW, sysfont, 2, nowrap=True)
    v += sysfont["Height"] * 2
    tft.text((0, v), "Hello World!", TFT.GREEN, sysfont, 3, nowrap=True)
    v += sysfont["Height"] * 3
    tft.text((0, v), str(1234.567), TFT.BLUE, sysfont, 4, nowrap=True)
    time.sleep_ms(1500)
    tft.fill(TFT.BLACK);
    v = 0
    tft.text((0, v), "Hello World!", TFT.RED, sysfont)
    v += sysfont["Height"]
    tft.text((0, v), str(math.pi), TFT.GREEN, sysfont)
    v += sysfont["Height"]
    tft.text((0, v), " Want pi?", TFT.GREEN, sysfont)
    v += sysfont["Height"] * 2
    tft.text((0, v), hex(8675309), TFT.GREEN, sysfont)
    v += sysfont["Height"]
    tft.text((0, v), " Print HEX!", TFT.GREEN, sysfont)
    v += sysfont["Height"] * 2
    tft.text((0, v), "Sketch has been", TFT.WHITE, sysfont)
    v += sysfont["Height"]
    tft.text((0, v), "running for: ", TFT.WHITE, sysfont)
    v += sysfont["Height"]
    tft.text((0, v), str(time.ticks_ms() / 1000), TFT.PURPLE, sysfont)
    v += sysfont["Height"]
    tft.text((0, v), " seconds.", TFT.WHITE, sysfont)


def test_programm():
    tft.fill(TFT.BLACK)
    tft.text((0, 0), "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Curabitur adipiscing ante sed nibh tincidunt feugiat. Maecenas enim massa, fringilla sed malesuada et, malesuada sit amet turpis. Sed porttitor neque ut ante pretium vitae malesuada nunc bibendum. Nullam aliquet ultrices massa eu hendrerit. Ut sed nisi lorem. In vestibulum purus a tortor imperdiet posuere. ", TFT.WHITE, sysfont, 1)
    time.sleep_ms(1000)

    tftprinttest()
    time.sleep_ms(4000)

    testlines(TFT.YELLOW)
    time.sleep_ms(500)

    testfastlines(TFT.RED, TFT.BLUE)
    time.sleep_ms(500)

    testdrawrects(TFT.GREEN)
    time.sleep_ms(500)

    testfillrects(TFT.YELLOW, TFT.PURPLE)
    time.sleep_ms(500)

    tft.fill(TFT.BLACK)
    testfillcircles(10, TFT.BLUE)
    testdrawcircles(10, TFT.WHITE)
    time.sleep_ms(500)

    testroundrects()
    time.sleep_ms(500)

    testtriangles()
    time.sleep_ms(500)

def text_scroll():
    delay = 500
    
    count = 0
    
    for num in range(len("Hello World!")+2):
      print("Hello World!"[11])
      if num > 13:
          count = 0
      tft.fill(TFT.BLACK)    
      tft.text((count, 0), "Hello World!", TFT.RED, sysfont, 2,nowrap=True)
      time.sleep_ms(delay)
      count = count + 10
      

def text_scroll_1():
    delay = 500
    
    count = 0
    decount = 11
    string = ""
    
    for num in range(24):
      if decount >=0 and num <12: 
        string = "Hello World!"[decount] + string   
      print(string)
      if 24 > num > 11 :
          string = " " + string
      tft.fill(TFT.BLACK)    
      tft.text((0, 0), string, TFT.RED, sysfont, 2,nowrap=True)
      count += 10
      if decount > 0:
         decount -= 1
      time.sleep_ms(delay)
      
      
def text_scroll_2(message):
    delay = 500
    
    count = 0
    decount = len(message)-1
    string = ""
    space = 10
                 # len(message)+24-len(message)
    for num in range(space+len(message)):
      if decount >=0 and num <len(message): 
        string = message[decount] + string   
      print(string)
      if space+len(message) > num > len(message)-2 :
          string = " " + string
      tft.fill(TFT.BLACK)    
      tft.text((0, 0), string, TFT.RED, sysfont, 2,nowrap=True)
      count += 10
      if decount > 0:
         decount -= 1
      time.sleep_ms(delay)       
      
    
def main():
  while True: 
    #test_programm()
    text_scroll_2("Hello!")    
    #text_scroll_1() 

main()

if __name__ == '__main__':
  main()



