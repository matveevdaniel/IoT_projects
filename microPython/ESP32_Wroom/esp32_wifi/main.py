## This file is executed on every boot (including wake-boot from deepsleep)
#import esp
#esp.osdebug(None)
#import webrepl_setup
#import webrepl
#webrepl.start()
#import utime
from time import sleep_ms
import network


#print(wlan.scan())             # scan for access points
#wlan.connect('M51','Qwe123rty') # connect to an AP
#print("Connected = " + str(wlan.isconnected()))     # check if the station is connected to an AP
#wlan.config('mac')      # get the interface's MAC address
#print(wlan.ifconfig())
#print(wlan.status())

def connection():
 wlan = network.WLAN(network.STA_IF) # create station interface
 
 
 if not wlan.isconnected():
   #wlan.disconnect()
   #wlan.active(False)
   sleep_ms(1000)
   wlan.active(True)
   sleep_ms(1000) # activate the interface
   while True:
	  try:
		 wlan.connect('ZTE_Home','Qwe123rty@')
		 sleep_ms(1000)
	  except OSError as e:
		 print("Error = " + str(e))
	  
	  if wlan.isconnected():
	     print('Connected') 
	     break



def main():
 connection()  
 #print("123")
if __name__ == '__main__':
  main()

 

