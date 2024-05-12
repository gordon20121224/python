#########################匯入模組#########################
import time
import mcu
from umqtt.simple import MQTTClient
import sys
from machine import Pin, ADC

#########################函式與類別定義#########################

#########################宣告與設定#########################
wi = mcu.wifi("SingularClass", "Singular#1234")
wi.setup(ap_active=False, sta_active=True)
if wi.connect():
    print(f"IP={wi.ip}")

mqtt_client = mcu.MQTT(
    "gordon", "mqtt.singularinnovation-ai.com", "singular", "Singular#1234"
)
mqtt_client.connect()
light_sensor = ADC(0)
#########################主程式#########################
while True:
    msg = str(light_sensor.read())
    mqtt_client.publish("gordon", msg)
    time.sleep(0.1)
