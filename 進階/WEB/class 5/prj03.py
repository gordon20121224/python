import requests
import datetime
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
import os
import sys
from ttkbootstrap import *
from PIL import Image, ImageTk

########################工作目錄######################
os.chdir(sys.path[0])  # 設定工作目錄
#######################定義常數########################
API_KEY = "892da2f13edf3c7f382637760e72d224"  # api key
BASE_URL = "http://api.openweathermap.org/data/2.5/forecast?"
UNITS = "metric"
LANG = "zh_tw"
#######################建立視窗########################


#######################定義函數########################
def draw_graph():

    city_name = "Los Angeles"

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
            time = datetime.strptime(dt_txt, "%Y-%m-%d %H:%M:%S").strftime("%m/%d/%H")
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
    plt.close()

    image = Image.open("weather_forecast.png")
    img = ImageTk.PhotoImage(image)

    canvas.config(width=image.width, height=image.height)
    canvas.create_image(image.width // 2, image.height // 2, image=img)
    canvas.image = img  # keep a reference!


#######################建立視窗########################
Window = tk.Tk()
Window.title("Weather App")

########################創建畫布########################
canvas = Canvas(Window, width=0, height=0, bg="white")
canvas.grid(row=0, column=0, padx=10, pady=10)

#######################設定字型########################
font_size = 20
Window.option_add("*font", ("Helvetica", font_size))

#######################設定主題########################
style = Style(theme="minty")
style.configure("my.TButton", font=("Helvetica", font_size))

#######################建立按鈕########################
draw_button = Button(Window, text="draw", command=draw_graph, style="my.TButton")
draw_button.grid(row=1, column=0, padx=10, pady=10)
#######################運行應用程式########################
Window.mainloop()
