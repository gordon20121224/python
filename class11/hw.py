list = {}
while True:
    print("目前已點的餐:" + str(list))
    print("1. 新增科目與成績")
    print("2. 刪除某個科目的成績")
    print("3. 關閉系統")
    option = input("請輸入你想要的功能:")
    if option == "1":
        x = input("請輸入想要新增的科目:")
        while True:
            try:
                y = int(input("請輸入成績"))
            except:
                print("error")
            else:
                list[x] = y
                break
    if option == "2":
        x = input("請輸入想要刪除的科目:")
        if x in list:
            list.pop(y, None)
            priint("delete successful")
        list.pop(x, None)
    if option == "3":
        print(sum(list.values()) / len(list))
        break
