#########################匯入模組#########################
from machine import Pin, PWM
from time import sleep

#########################函式與類別定義#########################

#########################宣告與設定#########################
# p2 = Pin(2, Pin.OUT)
frequency = 1000
duty_cycle = 0
led = PWM(Pin(2), freq=frequency, duty=duty_cycle)

#########################主程式#########################
while True:
    # led.duty(0)
    # sleep(1)
    # led.duty(700)
    # sleep(1)
    # led.duty(1023)
    # sleep(1)
    for i in range(1024):
        led.duty(i)
        sleep(0.002)
    for i in range(1023, -1, -1):
        led.duty(i)
        sleep(0.002)
