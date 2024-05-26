#########################匯入模組#########################
from machine import Pin
import mcu
import time

#########################函式與類別定義#########################

#########################宣告與設定#########################
gpio = mcu.gpio()
earthquake = Pin(gpio.D3, Pin.IN)

#########################主程式#########################
while True:
    print(earthquake.value())
    if earthquake.value() == 1:
        print("Emergency!")
    time.sleep(1)
