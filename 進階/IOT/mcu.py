import sys
import network
from machine import Pin, PWM
from umqtt.simple import MQTTClient

# mcu.py
# class gpio:
#     def __init__(self):
#         self.D0 = 16
#         self.D1 = 5
#         self.D2 = 4
#         self.D3 = 0
#         self.D4 = 2
#         self.D5 = 14
#         self.D6 = 12
#         self.D7 = 13
#         self.D8 = 15
#         self.SDD3 = 10
#         self.SDD2 = 9


class gpio:
    def __init__(self):
        self._D0 = 16
        self._D1 = 5
        self._D2 = 4
        self._D3 = 0
        self._D4 = 2
        self._D5 = 14
        self._D6 = 12
        self._D7 = 13
        self._D8 = 15
        self._SDD3 = 10
        self._SDD2 = 9

    @property  # 這個裝飾器會將這個函式變成屬性
    def D0(self):  # 這樣就可以用gpio.D0來取得16
        return self._D0

    @property
    def D1(self):
        return self._D1

    @property
    def D2(self):
        return self._D2

    @property
    def D3(self):
        return self._D3

    @property
    def D4(self):
        return self._D4

    @property
    def D5(self):
        return self._D5

    @property
    def D6(self):
        return self._D6

    @property
    def D7(self):
        return self._D7

    @property
    def D8(self):
        return self._D8

    @property
    def SDD3(self):
        return self._SDD3

    @property
    def SDD2(self):
        return self._SDD2


class wifi:
    def __init__(self, ssid=None, password=None):
        self.sta = network.WLAN(network.STA_IF)
        self.ap = network.WLAN(network.AP_IF)
        self.ssid = ssid
        self.password = password
        self.ap_active = False
        self.sta_active = False
        self.ip = None

    def setup(self, ap_active=False, sta_active=False):

        self.ap_active = ap_active
        self.sta_active = sta_active
        self.ap.active(ap_active)
        self.sta.active(sta_active)

    def scan(self):
        if self.sta_active:
            wifi_list = self.sta.scan()
            print("Scan result")
            for i in range(len(wifi_list)):
                print(wifi_list[i][0])
        else:
            print("Sta未啟用")

    def connect(self, ssid=None, password=None) -> bool:
        ssid = ssid if ssid is not None else self.ssid
        password = password if password is not None else self.password

        if not self.sta_active:
            print("Sta未啟用")
            return False

        if self.sta_active:
            self.sta.connect(ssid, password)
            while not (self.sta.isconnected()):
                pass
            self.ip = self.sta.ifconfig()[0]
            print("connect successfully", self.sta.ifconfig())
            return True


class LED:
    def __init__(self, r_pin, g_pin, b_pin, pwm: bool = False):
        if pwm == False:
            self.RED = Pin(r_pin, Pin.OUT)
            self.GREEN = Pin(g_pin, Pin.OUT)
            self.BLUE = Pin(b_pin, Pin.OUT)
        else:
            frequency = 1000
            duty_cycle = 0
            self.RED = PWM(Pin(r_pin), freq=frequency, duty=duty_cycle)
            self.GREEN = PWM(Pin(g_pin), freq=frequency, duty=duty_cycle)
            self.BLUE = PWM(Pin(b_pin), freq=frequency, duty=duty_cycle)


class MQTT:
    def __init__(
        self,
        MQTTClientId,
        mq_server,
        mqtt_username,
        mqtt_password,
    ):
        self.mq_server = mq_server
        self.MQTTClientId = MQTTClientId
        self.mqtt_username = mqtt_username
        self.mqtt_password = mqtt_password
        self.client = MQTTClient(
            MQTTClientId,
            mq_server,
            user=mqtt_username,
            password=mqtt_password,
            keepalive=30,
        )

    def connect(self):
        try:
            self.client.connect()
        except:
            sys.exit()
        finally:
            print("connect MQTT server")

    def subscribe(self, topic, on_message):
        self.client.set_callback(on_message)
        self.client.subscribe(topic)

    def check_msg(self):
        self.client.check_msg()
        self.client.ping()

    def publish(self, topic: str, msg: str):

        topic = topic.encode("utf-8")
        msg = msg.encode("utf-8")
        self.client.publish(topic, msg)
