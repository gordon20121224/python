#########################匯入模組#########################
import paho.mqtt.client as mqtt
import time
import getpass
import os
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage


#########################函式與類別定義#########################
def on_publish(client, userdata, mid, reason_code, properties):
    print(f"Message {mid} has been published.")


def on_connect(client, userdata, connect_flags, reason_code, properties):
    print(f"連線結果:{reason_code}")
    client.subscribe("gordon_home")  # 訂閱主題


def on_message(client, userdata, msg):
    global home_config
    # print(f"我訂閱的主題是:{msg.topic}, 收到訊息:{msg.payload.decode('utf-8')}")
    home_config = str(msg.payload.decode("utf-8"))


#########################宣告與設定#########################
client = mqtt.Client(callback_api_version=mqtt.CallbackAPIVersion.VERSION2)
client.on_publish = on_publish
client.on_connect = on_connect
client.on_message = on_message
client.username_pw_set("singular", "Singular#1234")
client.connect("mqtt.singularinnovation-ai.com", 1883, 60)
client.loop_start()
os.environ["OPENAI_API_KEY"] = getpass.getpass()
model = ChatOpenAI(model="gpt-4o", temperature=0.2)
home_config = "None"
#########################主程式#########################
while True:
    ans = input("請輸入想跟AI說的話: ")
    msg = model.invoke(
        [
            HumanMessage(
                content="""
    你是一個負責開燈跟關燈的管理員
    'ON'代表開燈
    'OFF'代表關燈
    'None'代表不要做任何事
    'home_config'代表正在詢問目前家裡的狀態
    你只能根據使用者的回應來決定要回答'ON'或'OFF'或'None'或'home_config'
    不能回答其他的字串
                """
            ),
            HumanMessage(content=ans),
        ]
    ).content
    print(msg)
    result = client.publish("hello_AI", msg)  # 發布訊息
    result.wait_for_publish()  # 等待發布完成

    if msg == "home_config":
        msg = model.invoke(
            [
                HumanMessage(
                    content="""
                你是一個負責解釋家裡狀態的小幫手，目前家裡的狀態是:
                """
                ),
                HumanMessage(content=home_config),
            ]
        ).content
        print(msg)

    # 檢查發布是否成功
    if result.rc == mqtt.MQTT_ERR_SUCCESS:
        print("Message published successfully")
    else:
        print("Failed to publish message")
    time.sleep(0.1)
