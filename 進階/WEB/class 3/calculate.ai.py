from ttkbootstrap import *
import sys
import os
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage
import getpass

#######################設定工作目錄########################
os.chdir(sys.path[0])  # 設定工作目錄


#######################定義函數########################


# 顯示計算結果的函式
def show_result():
    entry_text = entry.get()  # 取得Entry的文字
    msg = model.invoke(
        [
            HumanMessage(
                content="""
你是一個專門計算數學問題的AI助手。你只使用繁體中文回應，並且只會回答數學問題的答案。你不會回答任何其他類型的問題。
請按照以下步驟思考並解答問題：

1. 將問題分解成具體步驟
2. 進行必要的計算
3. 將計算結果轉換成文字描述
4. 準備回答給使用者
現在，請解答上述數學問題。
                """
            ),
            HumanMessage(content=entry_text),
        ]
    ).content
    label.config(text=msg)


#######################建立視窗########################
window = tk.Tk()
window.title("my gui")

os.environ["OPENAI_API_KEY"] = getpass.getpass()
model = ChatOpenAI(model="gpt-4o-2024-08-06", temperature=0.2)
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
