from ttkbootstrap import *
import sys
import os
from tkinter import filedialog
from PIL import Image, ImageTk

#######################設定工作目錄########################
os.chdir(sys.path[0])  # 設定工作目錄


def open_file():
    global file
    file = filedialog.askopenfilename(initialdir=sys.path[0])
    label2.config(text=file)


def show_file():
    global file
    image = Image.open(file)
    image = image.resize((canvas.winfo_width(), canvas.winfo_height()))
    photo = ImageTk.PhotoImage(image)
    canvas.create_image(0, 0, anchor="nw", image=photo)
    canvas.image = photo


#######################建立視窗########################
window = tk.Tk()
window.title("my gui")
#######################設定字型########################
font_size = 12
window.option_add("*Font", ("微軟正黑體", font_size))
#######################設定主題########################
style = Style(theme="darkly")
style.configure("Darkly.TButton", font=("微軟正黑體", font_size))
style.configure("Darkly.TLabel", font=("微軟正黑體", font_size))
#######################建立標籤########################
label = Label(window, text="choose:", style="Darkly.TLabel")
label.grid(row=0, column=0, sticky="nsew")
label2 = Label(window, text="no", style="Darkly.TLabel")
label2.grid(row=0, column=1, sticky="nsew")
#######################建立按鈕########################
button = Button(window, text="put", command=open_file, style="Darkly.TButton")
button.grid(row=0, column=2, sticky="EW")
button2 = Button(window, text="show", command=show_file, style="Darkly.TButton")
button2.grid(row=2, column=0, columnspan=3, sticky="EW")
canvas = Canvas(window, width=500, height=500)
canvas.grid(row=3, column=0, columnspan=3, sticky="NSEW")
#######################運行應用程式########################
window.mainloop()
