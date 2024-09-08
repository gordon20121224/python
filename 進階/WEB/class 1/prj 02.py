#######################匯入模組#######################
# 匯入 tkinter 模組
from tkinter import *


#######################定義函數########################
def hi_fun():

    global change
    if change == False:
        display.config(text="green", fg="black", bg="green")
    else:
        display.config(text="red", fg="black", bg="red")
    change = not change


change = False


#######################建立視窗########################
windows = Tk()
windows.title("My first GUI")

#######################建立按鈕######################

# 創建按鈕,當被按下時,執行hi_fun函數
btn1 = Button(windows, text="Click me ", command=hi_fun)

# 按鈕加入主視窗中
btn1.pack()

# 創建按鈕,當被按下時,執行clear_fun函數


# 按鈕加入主視窗中


########################建立標籤########################

# 創建一個標籤是"Hi singular"，陳景顏色為紅色背景顏色為黑色對呀 對
# label參數說明:(名稱，文字內容，前景顏色，背景顏色)
# ranbow color 自動產生隨機顏色，設定範圍從#000000到#ffffff

display = Label(
    windows,
    text="green",
)

# 將標籤加入主視窗中
display.pack()

#######################運行應用程式########################
windows.mainloop()
