#######################匯入模組#######################
# 匯入 tkinter 模組
from tkinter import *
from PIL import Image, ImageTk
# pip install pillow
import sys
import os
#######################設定工作目錄########################
# 設定工作目錄
os.chdir(sys.path[0])
###################################定義函數###############################
def move_obj(event, object, dx, dy):
    # 定義函數，參數是事件
    canvas.move(object, dx, dy)
def quit():
    # 定義函數，參數是事件
    windows.destroy()
#######################創建主視窗#######################
# 創建主視窗
windows = Tk()
# 設定主視窗標題
windows.title("My first GUI")
#####################button############################
quit = Button(windows, text="quit", command=windows.quit)
quit.pack()
#######################創建畫布#######################
# 創建一個畫布，設定其寬度為 600，高度為 600
canvas = Canvas(windows, width=600, height=600, bg="white")
# 將畫布加入主視窗中
canvas.pack()
#######################設定視窗圖片########################
# 設定視窗圖片
windows.iconbitmap("crocodile2.ico")
#######################載入圖片########################
# 載入圖片，只支援 GIF、PGM、PPM、PNG、BMP 格式
# img = PhotoImage(file="crocodile2.gif")
# 載入圖片並轉換成Image物件
image = Image.open("crocodile2.gif")
# 這樣就可以將任意圖片轉換成Image物件
# 使用ImageTk模組的PhotoImage方法建立圖片物件
img = ImageTk.PhotoImage(image)
#######################顯示圖片########################
# 在畫布上顯示圖片
my_img = canvas.create_image(300, 300, image=img)
#############################畫圖############################
circle = canvas.create_oval(100, 100, 200, 200, fill="red")
rect = canvas.create_rectangle(100, 100, 200, 200, fill="blue")
msg = canvas.create_text(100, 100, text="yee", fill="black", font="Times 20 bold")
##############################綁定案件事件############################
canvas.bind_all("<Right>", lambda event: move_obj(event, circle, 10, 0))
canvas.bind_all("<Left>", lambda event: move_obj(event, circle, -10, 0))
canvas.bind_all("<Up>", lambda event: move_obj(event, circle, 0, -10))
canvas.bind_all("<Down>", lambda event: move_obj(event, circle, 0, 10))
canvas.bind_all("<w>", lambda event: move_obj(event, rect, 0, -10))
canvas.bind_all("<s>", lambda event: move_obj(event, rect, 0, 10))
canvas.bind_all("<a>", lambda event: move_obj(event, rect, -10, 0))
canvas.bind_all("<d>", lambda event: move_obj(event, rect, 10, 0))
#######################運行應用程式#######################
# 開始執行主迴圈，等待用戶操作
windows.mainloop()
8:59
