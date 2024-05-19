#########################匯入模組#########################
import time
import mcu


#########################函式與類別定義#########################
def on_message(topic, msg):
    global m
    msg = msg.decode("utf-8")  # Byte to str
    topic = topic.decode("utf-8")
    print(f"my subscribe topic:{topic}, msg:{msg}")
    m = msg


#########################宣告與設定#########################
wi = mcu.wifi("SingularClass", "Singular#1234")
wi.setup(ap_active=False, sta_active=True)
if wi.connect():
    print(f"IP={wi.ip}")

mqtt_client = mcu.MQTT(
    "gordon", "mqtt.singularinnovation-ai.com", "singular", "Singular#1234"
)
mqtt_client.connect()
gpio = mcu.gpio()
servo = mcu.servo(gpio.D8)
mqtt_client.connect()
mqtt_client.subscribe("gordon", on_message)
m = 0

#########################主程式#########################
while True:
    mqtt_client.check_msg()  # 等待已訂閱的主題發送資料
    servo.angle(int(m))
    time.sleep(1)
