import getpass
import os
import paho.mqtt.client as mqtt
import time

os.environ["OPENAI_API_KEY"] = getpass.getpass()


def on_publish(client, userdata, mid, reason_code, properties):
    print(f"Message {mid} has been published.")


from langchain_openai import ChatOpenAI

model = ChatOpenAI(model="gpt-4o", temperature=0.2)
from langchain_core.messages import HumanMessage

client = mqtt.Client(callback_api_version=mqtt.CallbackAPIVersion.VERSION2)
client.on_publish = on_publish
client.username_pw_set("singular", "Singular#1234")
client.connect("mqtt.singularinnovation-ai.com", 1883, 60)
client.loop_start()
while True:
    ans = input("請輸入想跟AI說的話: ")
    msg = model.invoke(
        [
            HumanMessage(
                content="""
    你是一個負責開關和車庫門的管理員
    'ON'代表開燈 
    'OFF' 代表關燈
    'close'代表車庫門關閉
    'open'代表車庫門開啟
    'None'代表什麼都不要做 
    你只能根據使用者的回應來決定要回答'ON'或'OFF'或'None'或'close'或 'open'
                """
            ),
            HumanMessage(content=ans),
        ]
    ).content
    result = client.publish("gordon_AI", msg)  # 發布訊息
    result.wait_for_publish()  # 等待發布完成
    print(msg)
    if result.rc == mqtt.MQTT_ERR_SUCCESS:
        print("Message published successfully")
    else:
        print("Failed to publish message")
    time.sleep(0.1)
