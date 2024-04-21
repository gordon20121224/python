#########################匯入模組#########################
from umqtt.simple import MQTTClient
import sys
import time
import mcu
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
mq_server = "mqtt.singularinnovation-ai.com"
MQTTClientId = "gordon"
mqtt_username = "singular"
mqtt_password = "Singular#1234"
mqClient0 = MQTTClient(
    MQTTClientId, mq_server, user=mqtt_username, password=mqtt_password, keepalive=30
)

try:
    mqClient0.connect()
except:
    sys.exit()
finally:
    print("connect MQTT server")

mqClient0.set_callback(on_message)
mqClient0.subscribe("gw")

gpio = mcu.gpio()
light_sensor = ADC(0)  # 建立 ADC 物件
RED = Pin(gpio.D5, Pin.OUT)
GREEN = Pin(gpio.D6, Pin.OUT)
BLUE = Pin(gpio.D7, Pin.OUT)

RED.value(0)
BLUE.value(0)
GREEN.value(0)

m = "off"
#########################主程式#########################
while True:
    light_sensor_reading = light_sensor.read()
    mqClient0.check_msg()
    mqClient0.ping()
    if m == "off":
        RED.value(0)
        BLUE.value(0)
        GREEN.value(0)
    elif m == "on":
        RED.value(1)
        BLUE.value(1)
        GREEN.value(1)
    elif m == "auto":
        if light_sensor_reading > 700:
            RED.value(1)
            BLUE.value(1)
            GREEN.value(1)
        else:
            RED.value(0)
            BLUE.value(0)
            GREEN.value(0)

    time.sleep(0.1)
