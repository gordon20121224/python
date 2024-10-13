import requests
import datetime
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
import os
import sys

########################工作目錄######################
os.chdir(sys.path[0])  # 設定工作目錄
#######################定義函數########################
API_KEY = "892da2f13edf3c7f382637760e72d224"  # api key
BASE_URL = "http://api.openweathermap.org/data/2.5/forecast?"
UNITS = "metric"
LANG = "zh_tw"
#######################建立視窗########################

#######################主程式########################
city_name = "New York"

send_url = f"{BASE_URL}appid={API_KEY}&q={city_name}&units={UNITS}&lang={LANG}"

print(f"發送的:{send_url}")
response = requests.get(send_url)
response.raise_for_status()
info = response.json()
xlist = []
ylist = []
if "city" in info:
    for forecast in info["list"]:
        dt_txt = forecast["dt_txt"]
        temp = forecast["main"]["temp"]
        time = datetime.datetime.strptime(dt_txt, "%Y-%m-%d %H:%M:%S").strftime(
            "%m/%d/%H"
        )
        xlist.append(time)
        ylist.append(temp)
        print(f"{dt_txt} - 溫度:{temp}度")
        weather_description = forecast["weather"][0]["description"]
        print(f"{dt_txt} - 溫度:{temp}度 - 天氣狀況:{weather_description}")
else:
    print("沒有天氣資訊")
#########################繪圖########################
# https://fonts.google.com/
font = FontProperties(fname="NotoSerifTC-VariableFont_wght.ttf", size=14)
fig, ax = plt.subplots(figsize=(12, 6))
ax.plot(
    xlist,
    ylist,
)
ax.set_title("5 天氣預報", fontproperties=font)
ax.set_ylabel("溫度", fontproperties=font)
ax.set_xlabel("時間", fontproperties=font)
plt.xticks(rotation=45)
plt.tight_layout()
fig.savefig("weather_forecast.png")
plt.show()
