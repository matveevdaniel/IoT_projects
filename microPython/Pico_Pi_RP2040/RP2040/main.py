from time import sleep
import liba


while True:
 for layer in range(0,8):
    for led in range(0,8):
        liba.funcLed(layer,led,1)
        sleep(0.001)
        liba.funcLed(layer,led,0)
        sleep(0.001)
        
 for layer in range(7,-1,-1):
    for led in range(7,-1,-1):
        liba.funcLed(layer,led,1)
        sleep(0.001)
        liba.funcLed(layer,led,0)
        sleep(0.001)
        
 


 