#######################匯入模組#######################
# 匯入 tkinter 模組
from tkinter import *
import sys
import os

#######################設定工作目錄######################
os.chdir(sys.path[0])
#######################建立主視窗########################
window = Tk()
window.title("My first GUI")

#######################建立畫布######################
canvas = Canvas(window, width=500, height=500)
canvas.pack()
#######################設定視窗圖片######################
window.iconbitmap("crocodile2.ico")

#######################仔入圖片######################
img = PhotoImage(file="crocodile2.gif")

#######################顯示圖片######################
my_image = canvas.create_image(300, 300, image=img)

#######################運行應用程式########################
window.mainloop()
