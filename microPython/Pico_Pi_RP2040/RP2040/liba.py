from machine import Pin

minusLed = [0]*8
plusLed  = [0]*8

minusLed[0] = Pin(0, Pin.OUT)
minusLed[1] = Pin(1, Pin.OUT)
minusLed[2] = Pin(2, Pin.OUT)
minusLed[3] = Pin(3, Pin.OUT)
minusLed[4] = Pin(4, Pin.OUT)
minusLed[5] = Pin(5, Pin.OUT)
minusLed[6] = Pin(6, Pin.OUT)
minusLed[7] = Pin(7, Pin.OUT)

minusLed[0].value(1)
minusLed[1].value(1)
minusLed[2].value(1)
minusLed[3].value(1)
minusLed[4].value(1)
minusLed[5].value(1)
minusLed[6].value(1)
minusLed[7].value(1)

plusLed[0] = Pin(10, Pin.OUT)
plusLed[1] = Pin(11, Pin.OUT)
plusLed[2] = Pin(12, Pin.OUT)
plusLed[3] = Pin(13, Pin.OUT)
plusLed[4] = Pin(14, Pin.OUT)
plusLed[5] = Pin(15, Pin.OUT)
plusLed[6] = Pin(16, Pin.OUT)
plusLed[7] = Pin(17, Pin.OUT)



def funcLed(level,led,val):
    
    if (val == 1):
       plusLed[level].value(1)
       minusLed[led].value(0)
       #print('YES')
       
    if (val == 0):
       plusLed[level].value(0)
       minusLed[led].value(1)
       #print('NO')
       


   