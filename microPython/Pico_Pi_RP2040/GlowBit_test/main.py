import glowbit
import utime



# while True:
#     matrix.demo()

def runColors():
  colors = {
     "red": 0xFF0000,
     "green":0x00FF00,
     "blue": 0x0000FF,
     "yellow": 0xFFFF00,
     "purple": 0xFF00FF,
     "cyan": 0x00FFFF,
     "white": 0xFFFFFF,
     }

  matrix = glowbit.matrix8x8()
  for color in colors:
   for i in range(0,64):
      matrix.blankDisplay()
      matrix.pixelSet(i,colors[color])
      matrix.pixelsShow()
      utime.sleep_us(1)
     
  #matrix.pixelsShow()

def abc():
    matrix = glowbit.matrix8x8()
    matrix.blankDisplay()
    matrix.drawChar('D',0,0,0xFF0000)
    matrix.pixelsShow() 
     
def main():
   
  # runColors()
   abc()
    
if __name__ == '__main__':
    main()    
     
