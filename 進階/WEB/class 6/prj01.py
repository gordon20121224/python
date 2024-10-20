from ttkbootstrap import *
import sys
import os
from PIL import Image, ImageTk
import requests
import datetime
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

########################定義常數######################
API_KEY = "892da2f13edf3c7f382637760e72d224"  # api key
BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
FORECAST_URL = "https://api.openweathermap.org/data/2.5/forecast?"
UNITS = "metric"
LANG = "zh_tw"
ICON_BASE_URL = "https://openweathermap.org/img/wn/"

#######################設定工作目錄#################
os.chdir(sys.path[0])  # 設定工作目錄


#######################定義函數########################
def on_switch_change():
    global UNITS, current_temperature
    UNITS = "metric" if check_type.get() else "imperial"
    if temp_label["text"] != "temperature:?°C":
        if UNITS == "metric":
            current_temperature = round((current_temperature - 32) * 5 / 9, 2)
        else:
            current_temperature = round(current_temperature * 9 / 5 + 32, 2)
        temp_label.config(
            text=f"temperature:{current_temperature}°{'C' if UNITS == 'metric' else 'F'}"
        )


def get_weather_info():
    global UNITS, current_temperature
    city_name = entry.get()
    send_url = f"{BASE_URL}appid={API_KEY}&q={city_name}&units={UNITS}&lang={LANG}"
    response = requests.get(send_url)
    info = response.json()
    if "weather" in info and "main" in info:
        current_temperature = info["main"]["temp"]
        weather_description = info["weather"][0]["description"]
        icon_code = info["weather"][0]["icon"]
        icon_url = f"{ICON_BASE_URL}{icon_code}@2x.png"
        icon_response = requests.get(icon_url)
        if icon_response.status_code == 200:
            with open(f"{icon_code}.png", "wb") as icon_file:
                icon_file.write(icon_response.content)
        image = Image.open(f"{icon_code}.png")
        tk_image = ImageTk.PhotoImage(image)
        icon_label.config(image=tk_image)
        icon_label.image = tk_image

        temp_label.config(
            text=f"temperature:{current_temperature}°{'C' if UNITS == 'metric' else 'F'}"
        )
        descrpition_label.config(text=weather_description)
        draw_graph(city_name)
    else:
        descrpition_label.config(text="no weather info")


def draw_graph(city_name):

    send_url = f"{FORECAST_URL}appid={API_KEY}&q={city_name}&units={UNITS}&lang={LANG}"

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
    plt.close()

    image = Image.open("weather_forecast.png")
    img = ImageTk.PhotoImage(image)

    canvas.config(width=image.width, height=image.height)
    canvas.create_image(image.width // 2, image.height // 2, image=img)
    canvas.image = img  # keep a reference!


#######################建立視窗########################
Window = tk.Tk()
Window.title("weather.app")


#######################設定字型########################
font_size = 20
Window.option_add("*font", ("Helvetica", font_size))

#######################設定主題########################
style = Style(theme="minty")
style.configure("my.TButton", font=("Helvetica", font_size))
style.configure("my.TCheckbutton", font=("Helvetica", font_size))

######################建立變數########################
check_type = BooleanVar()
check_type.set(True)
########################創建畫布########################
canvas = Canvas(Window, width=0, height=0, bg="white")
canvas.grid(row=3, column=0, columnspan=3, padx=10, pady=10)
#######################建立標籤########################
descrpition_label = Label(Window, text="descrpition")
descrpition_label.grid(row=1, column=2, padx=10, pady=10)

label = Label(Window, text="name a city")
label.grid(row=0, column=0, padx=10, pady=10)

icon_label = Label(Window, text="icon")
icon_label.grid(row=1, column=0, padx=10, pady=10)


temp_label = Label(Window, text="temperature")
temp_label.grid(row=1, column=1, padx=10, pady=10)
#######################建立按鈕########################
button = Button(
    Window, text="name a city's weather", command=get_weather_info, style="my.TButton"
)
button.grid(
    row=0,
    column=2,
)

######################建立Entry物件########################
entry = Entry(Window, width=30)
entry.grid(row=0, column=1, padx=10, pady=10)

######################建立Checkbutton########################
check_button = Checkbutton(
    Window,
    variable=check_type,
    onvalue=True,
    offvalue=False,
    command=on_switch_change,
    style="my.TCheckbutton",
    text="temperature(°C/°F)",
)
check_button.grid(row=2, column=1, padx=10, pady=10)

#######################運行應用程式########################
Window.mainloop()
