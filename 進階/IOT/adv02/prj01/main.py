import os

print(os.listdir())
with open("new_file.txt", "w") as f:  # 新增檔案
    f.write("Hello, Micropython!")

print(os.listdir())

os.remove("new_file.txt")  # 刪除檔案
print(os.listdir())
