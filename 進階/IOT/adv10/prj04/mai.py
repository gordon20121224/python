#########################匯入模組#########################
from machine import Pin, I2C
import dht
import time
import mcu
import json
import ssd1306
from umqtt.simple import MQTTClient
import sys
from machine import Pin, ADC

#########################函式與類別定義#########################

#########################宣告與設定#########################
gpio = mcu.gpio()

wi = mcu.wifi("SingularClass", "Singular#1234")
wi.setup(ap_active=False, sta_active=True)
if wi.connect():
    print(f"IP={wi.ip}")

mqtt_client = mcu.MQTT(
    "gordon", "mqtt.singularinnovation-ai.com", "singular", "Singular#1234"
)
mqtt_client.connect()

i2c = I2C(scl=Pin(gpio.D1), sda=Pin(gpio.D2))
oled = ssd1306.SSD1306_I2C(128, 64, i2c)

d = dht.DHT11(Pin(gpio.D0, Pin.IN))
msg_json = {}
light_sensor = ADC(0)
#########################主程式#########################
while True:
    msg = str(light_sensor.read())
    d.measure()
    temp = d.temperature()
    hum = d.humidity()
    sensor = light_sensor.read()
    oled.fill(0)  # 清除螢幕
    oled.text(f"Humidity:{hum:02d}", 0, 0)  # 顯示文字, x座標, y座標
    oled.text(f"Temperature:{temp:02d}C", 0, 10)
    oled.show()
    msg_json["light_sensor.read"] = sensor
    msg_json["humidity"] = hum
    msg_json["temperature"] = temp
    msg = json.dumps(msg_json)
    mqtt_client.publish("gordon", msg)
    time.sleep(1)
