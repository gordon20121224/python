"""
以下功能說明:
1. 新增餐點
    1.1 顯示餐點列表
    1.2 輸入餐點編號
    1.3 將餐點加入my_list
2. 移除餐點
    2.1 輸入想移除的餐點完整名稱
    2.2 將餐點從my_list移除
3. 提交菜單
    3.1 顯示my_list中的餐點及數量
    3.2 顯示"菜單已提交囉!"
"""
list = []
menu = ["apple", "orange", "banana"]
while True:
    print("目前已點的餐:" + str(list))
    print("1. 新增餐點")
    print("2. 移除餐點")
    print("3. 提交菜單")
    option = input("請輸入你想要的功能:")

    if option == "1":
        for i in range(len(menu)):
            print(str(i + 1) + ". " + menu[i])
            x = int(input("請輸入想要新增點餐清單:"))
            list.append(menu[x - 1])
        except:
            print("輸入錯誤查無此餐點，請重新輸入餐點編號")
    elif option == "2":
        x = input("請輸入想要移除的東西:")
        while x in list:
            list.remove(x)
            print("已經點餐清單中移除特定!")
    elif option == "3":
        for i in range(len(menu)):
            print(menu[i] + str(":") + str(list.count(menu[i])))
            break

    else:
        print("error")
