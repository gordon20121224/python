#########################匯入模組#########################
from umqtt.simple import MQTTClient
import sys
import time
import adv08.mcu as mcu
from machine import Pin, ADC


#########################函式與類別定義#########################
def on_message(topic, msg):
    global m
    msg = msg.decode("utf-8")
    m = msg
    topic = topic.decode("utf-8")
    print(f"my subscribe topic:{topic}, msg:{msg}")


#########################宣告與設定#########################
wi = mcu.wifi("SingularClass", "Singular#1234")
wi.setup(ap_active=False, sta_active=True)
if wi.connect():
    print(f"IP={wi.ip}")


MQTT = mcu.MQTT("gordon", "mqtt.singularinnovation-ai.com", "singular", "singular")
MQTT.connect
MQTT.subscribe("hello", on_message)

gpio = mcu.gpio()
LED = mcu.LED(gpio.D5, gpio.D6, gpio.D7, PWM=False)
LED.RED.value(0)
LED.BLUE.value(0)
LED.GREEN.value(0)
light_sensor = ADC(0)  # 建立 ADC 物件
m = ""

#########################主程式#########################
while True:
    MQTT.check_msg()
    light_sensor_reading = light_sensor.read()

    if m == "off":
        LED.RED.value(0)
        LED.BLUE.value(0)
        LED.GREEN.value(0)
    elif m == "on":
        LED.RED.value(1)
        LED.BLUE.value(1)
        LED.GREEN.value(1)
    elif m == "auto":
        if light_sensor_reading > 700:
            LED.RED.value(1)
            LED.BLUE.value(1)
            LED.GREEN.value(1)
        else:
            LED.RED.value(0)
            LED.BLUE.value(0)
            LED.GREEN.value(0)

    time.sleep(0.1)
