import mcu

gpio = mcu.gpio()

LED = mcu.LED(gpio.D5, gpio.D6, gpio.D7, pwm=False)
LED.RED.value(0)  # 0 or 1
LED.GREEN.value(0)  # 0 or 1
LED.BLUE.value(0)  # 0 or 1

# LED.RED.duty(1023)  # 0~1023
# LED.GREEN.duty(1023)  # 0~1023
# LED.BLUE.duty(1023)  # 0~1023
