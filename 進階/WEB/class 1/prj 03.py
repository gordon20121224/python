#######################匯入模組#######################
# 匯入 tkinter 模組
from tkinter import *
import random


#######################定義函數########################
def hi_fun():
    bg_COLORS = "#" + "".join([random.choice("0123456789ABCDEF") for i in range(6)])
    fg_COLORS = "#" + "".join([random.choice("0123456789ABCDEF") for i in range(6)])
    display.config(text="Hi singular ", fg=fg_COLORS, bg=bg_COLORS)


#######################建立視窗########################
windows = Tk()
windows.title("My first GUI")

windows.option_add("*Font", "Helvetica 40")
#######################建立按鈕######################

# 創建按鈕,當被按下時,執行hi_fun函數
btn1 = Button(windows, text="Click me ", command=hi_fun)

# 按鈕加入主視窗中
btn1.pack()

########################建立標籤########################

# 創建一個標籤是"Hi singular"，陳景顏色為紅色背景顏色為黑色對呀 對
# label參數說明:(名稱，文字內容，前景顏色，背景顏色)
# ranbow color 自動產生隨機顏色，設定範圍從#000000到#ffffff
display = Label(
    windows,
    text="green",
)

display.pack()
#######################運行應用程式########################
windows.mainloop()
