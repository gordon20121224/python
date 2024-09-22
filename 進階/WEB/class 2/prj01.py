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

#######################創建主視窗#######################
# 創建主視窗
windows = Tk()

# 設定主視窗標題
windows.title("My first GUI")

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
#######################畫圖片########################
# 在畫布上畫一個圓形起始位置為(250,150)，結束位置為(300,200)，
# 填充顏色為紅色
circle = canvas.create_oval(250, 150, 300, 200, fill="red")

rect = canvas.create_rectangle(220, 400, 300, 200, fill="red")

msg = canvas.create_text(300, 100, text="Crocodile", font=("Arial", 20))
#######################運行應用程式#######################
# 開始執行主迴圈，等待用戶操作
windows.mainloop()
