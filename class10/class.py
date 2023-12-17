# "1,2,3" . split (',')
# '2020/1/1'.split('/')
# img=['1', '2', '3']
# '-'.join(img)  to make a new str

# img = ["2023/10/20"]
# img.split("/")
# "-".join(img)
# print(img)

# l = [1, 2, 3]
# l.append(4)
# print(l)

# l = ['a', 'b', 'c', 'a']
# l.remove('a')
# print(l)

# l = [1, 2, 3]
# l.insert(0, 'a')
# print(l)

order_list = []
while True:
    print("1. 新增餐點到點餐清單")
    print("2. 從點餐清單中移除特定餐點")
    print("3. 在指定位置加入餐點")
    print("4. 計算點餐清單中某餐點的數量")
    print("5. 取消點餐清單中的最後一項餐點")
    print("6. 取消點餐清單中特定位置的餐點")
    print("7. 顯示升序排序的點餐清單")
    print("8. 顯示降序排序的點餐清單")
    print("9. 反轉點餐清單的順序")
    print("10. 查詢餐點在點餐清單中的位置")
    print("11. 退出點餐機")
    option = input("welcome to use the machine ! please enter the option u want:")

    if option == "1":
        x = input("請輸入想要新增點餐清單:")
        order_list.append(x)
    elif option == "2":
        x = input("請輸入想要新增點餐清單:")
        if x in order_list:
            order_list.remove(x)
            print("已已經點餐清單中移除特定!")
        else:
            print("error")
    elif option == "3":
        x = int(input("請輸入想要新增點餐清單:"))
        y = input("在指定位置加入餐點:")
        order_list.insert(x, y)
    elif option == "4":
        ans = input("請輸入你想要的餐點名稱")
        print(order_list.count(ans))
    elif option == "5":
        order_list.pop()
    elif option == "6":
        l = int(input("請輸入特定位置:"))
        order_list.pop(l)
    elif option == "7":
        order_list.sort()
        print(order_list)
    elif option == "8":
        order_list.sort(reverse=True)
        print(order_list)
    elif option == "9":
        order_list.reverse()
        print(order_list)
    elif option == "10":
        x = input("餐點名稱是什麼:")
        order_list.index(x)
        print(order_list)
    elif option == "11":
        print("thank u to use the order machine!")
        break
    else:
        print("please enter a useful option!")
        continue
    print("目前的點餐清單:" + str(order_list))
# 取得元素值
# 元素走訪
# key :
# items :
# for item in items:
d = {}
items = d.items()
for key, value in items:
    print(key, value)
