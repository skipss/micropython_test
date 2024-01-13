# This is a test file of the OTA code
import machine
from machine import Pin, SoftI2C
from network import WLAN, STA_IF
from time import sleep, time
from ssd1306 import SSD1306_I2C
I2C_ADDR = 0x27
led=Pin(2,Pin.OUT)
totalRows = 2
totalColumns = 16
i2c = SoftI2C(scl=Pin(22), sda=Pin(21), freq=10000) #I2C for ESP32
#i2c = I2C(scl=Pin(5), sda=Pin(4), freq=10000) #I2C for ESP8266
display=SSD1306_I2C(128,64,i2c,addr=0x3c)
wlan = WLAN(STA_IF)
wlan.active(True)
start_time = time()
if not wlan.isconnected():
    print('Connecting to network...')
    wlan.connect('ingsys_5G', 't1024768')

    while not wlan.isconnected():
        led.value(1)
        sleep(1)
        led.value(0)
        sleep(1)

        if time() - start_time > 15 :
            print('WIFI Connected Timeout!')
            break

if wlan.isconnected():
    led.value(1)
    sleep(1)
    led.value(0)
    sleep(1)
    print('ingsystem network : ', wlan.ifconfig())

    display.fill(0)
    display.text('ingsystem network', 0, 0)
    display.text(wlan.ifconfig()[0], 0, 20)
    display.text(wlan.ifconfig()[1], 0, 38)
    display.text(wlan.ifconfig()[2], 0, 56)
    display.show()
    




