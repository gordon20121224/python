from ttkbootstrap import *
import sys
import os

#######################設定工作目錄########################
os.chdir(sys.path[0])  # 設定工作目錄


#######################定義函數########################
def show_result():
    entry_text = entry.get()
    try:
        result = eval(entry_text)
    except:
        result = "error"
    label.config(text=result)


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

label = Label(window, text="計算結果")
label.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

#######################Entry物件########################

entry = Entry(window, width=30)
entry.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

#######################建立按鈕########################

button = Button(window, text="計算結果", command=show_result, style="my.TButton")

button.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

#######################運行應用程式########################
window.mainloop()
