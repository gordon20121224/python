#########################匯入模組#########################
import time
import mcu
from machine import Pin, I2C
import ssd1306


#########################函式與類別定義#########################
def on_message(topic, msg):
    global m
    msg = msg.decode("utf-8")  # Byte to str
    topic = topic.decode("utf-8")
    print(f"my subscribe topic:{topic}, msg:{msg}")
    m = msg


#########################宣告與設定#########################
gpio = mcu.gpio()
i2c = I2C(scl=Pin(gpio.D1), sda=Pin(gpio.D2))
oled = ssd1306.SSD1306_I2C(128, 64, i2c)

wi = mcu.wifi("SingularClass", "Singular#1234")
wi.setup(ap_active=False, sta_active=True)
if wi.connect():
    print(f"IP={wi.ip}")

mqtt_client = mcu.MQTT(
    "gordon", "mqtt.singularinnovation-ai.com", "singular", "Singular#1234"
)
mqtt_client.connect()
mqtt_client.subscribe("gordon", on_message)
m = "no message"

#########################主程式#########################
while True:
    mqtt_client.check_msg()  # 等待已訂閱的主題發送資料
    oled.fill(0)  # 清除螢幕
    oled.text(f"{wi.ip}", 0, 0)
    oled.text("topic : gordon", 0, 10)
    oled.text(f"msg : {m}", 0, 20)
    oled.show()
    time.sleep(0.1)
