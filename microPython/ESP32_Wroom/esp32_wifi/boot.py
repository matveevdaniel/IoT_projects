## This file is executed on every boot (including wake-boot from deepsleep)
#import esp
#esp.osdebug(None)
#import webrepl_setup
#import webrepl
#webrepl.start()
import utime
from time import sleep
import network


#print(wlan.scan())             # scan for access points
#wlan.connect('M51','Qwe123rty') # connect to an AP
#print("Connected = " + str(wlan.isconnected()))     # check if the station is connected to an AP
#wlan.config('mac')      # get the interface's MAC address
#print(wlan.ifconfig())
#print(wlan.status())

def connection():
 wlan = network.WLAN(network.STA_IF) # create station interface
 wlan.active(False)
 utime.sleep(1)
 wlan.active(True)       # activate the interface
 wlan.disconnect()   
 if not wlan.isconnected():
   while True:
	  try:
		 wlan.connect('M51','Qwe123rty')
		 utime.sleep(1)
	  except OSError as e:
		 print("Error = " + str(e))
	  
	  if wlan.isconnected():
	     print('Connected') 
	     break



def main():
 #connection()  
 print("123")
if __name__ == '__main__':
  main()

 
