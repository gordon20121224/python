#######################匯入模組#######################
import requests
import os
import sys

#########################定義常數######################
API_KEY = "892da2f13edf3c7f382637760e72d224"  # api key
BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
UNITS = "metric"
LANG = "zh_tw"
ICON_BASE_URL = "https://openweathermap.org/img/wn/"
######################主程式######################
os.chdir(sys.path[0])  # 設定工作目錄
city_name = input("請輸入要查詢的城市名稱：")

send_url = f"{BASE_URL}appid={API_KEY}&q={city_name}&units={UNITS}&lang={LANG}"

print(f"發送的url是：{send_url}")
response = requests.get(send_url)
info = response.json()

if "weather" in info and "main" in info:
    current_weather = info["main"]["temp"]
    weather_description = info["weather"][0]["description"]

    print(f"city: {city_name}")
    print(f"current weather: {current_weather} ℃")
    print(f"weather description: {weather_description}")
    icon_code = info["weather"][0]["icon"]

    icon_url = f"{ICON_BASE_URL}{icon_code}@2x.png"
    print(f"下載天氣圖片: {icon_url}")
    icon_response = requests.get(icon_url)

    if icon_response.status_code == 200:
        with open("weather.png", "wb") as icon_file:
            icon_file.write(icon_response.content)
            print(f"圖標以保存{icon_code}.png ")
    else:
        print("無法下載天氣圖標")

else:
    print("無法查詢天氣資訊")
