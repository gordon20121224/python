#########################匯入模組#########################
from machine import Pin, PWM
from time import sleep
import adv08.mcu as mcu

#########################函式與類別定義#########################

#########################宣告與設定#########################
frequecy = 1000
duty_cycle = 0
gpio = mcu.gpio()
RED = PWM(Pin(gpio.D5), freq=frequecy, duty=duty_cycle)
BLUE = PWM(Pin(gpio.D6), freq=frequecy, duty=duty_cycle)
GREEN = PWM(Pin(gpio.D7), freq=frequecy, duty=duty_cycle)
delay = 0.0020
#########################主程式#########################


while True:
    for duty_cycle in range(1023, -1, -1):
        RED.duty(duty_cycle)
        GREEN.duty(1023 - duty_cycle)
        sleep(delay)
    for duty_cycle in range(1023, -1, -1):
        GREEN.duty(duty_cycle)
        BLUE.duty(1023 - duty_cycle)
        sleep(delay)

    for duty_cyCle in range(1023, -1, -1):
        BLUE.duty(duty_cycle)
        RED.duty(1023 - duty_cycle)
        sleep(delay)

    # led.duty(0)
    # sleep(1)
    # led.duty(700)
    # sleep(1)
    # led.duty(1023)
    # sleep(1)

    # for i in range(1024):
    #     led.duty(i)
    #     sleep(0.002)
    # for i in range(1023, -1, -1):
    #     led.duty(i)
    #     sleep(0.002)
