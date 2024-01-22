from machine import Pin,I2C
import ds1302
from ssd1306 import SSD1306_I2C
import utime

pix_res_x = 128
pix_res_y = 64

ds = ds1302.DS1302(Pin(0),Pin(1),Pin(2))

def init_i2c(scl_pin, sda_pin):
    # Initialize I2C device
    i2c_dev = I2C(1, scl=Pin(scl_pin), sda=Pin(sda_pin), freq=200000)
    i2c_addr = [hex(ii) for ii in i2c_dev.scan()]
    
    if not i2c_addr:
        print('No I2C Display Found')
        sys.exit()
    else:
        print("I2C Address      : {}".format(i2c_addr[0]))
        print("I2C Configuration: {}".format(i2c_dev))
    
    return i2c_dev


def display_text(oled):
    # Display text on the OLED
    while True:
      arr_date = ds.date_time()
      str_date_first = f"{arr_date[2]}/{arr_date[1]}/{arr_date[0]}"
      str_date_second = f"{arr_date[4]}:{arr_date[5]}:{arr_date[6]}"
      oled.fill(0) #заполняет экран черным цветом
      oled.text(str_date_first, 10, 5)
      oled.text(str_date_second, 5, 20)
      oled.show()
      utime.sleep_ms(1000)
      
     #print(ds.date_time())
     


def clock():
    #ds.date_time([2023, 12, 6, 3, 22, 52, 40, 0]) # set datetime.

    while True:
     print(ds.date_time()) # returns the current datetime.
     utime.sleep_ms(10000)
     
    #ds.hour() # returns hour.
    #print(ds.minute())
    #ds.second(10) # set second to 10.
 
def main():
    
    i2c_dev = init_i2c(scl_pin=27, sda_pin=26)
    oled = SSD1306_I2C(pix_res_x, pix_res_y, i2c_dev)
    display_text(oled)
    

if __name__ == '__main__':
    main() 
 
 
