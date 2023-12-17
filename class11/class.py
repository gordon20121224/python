food_list = {"蛋糕": 1, "三明治": 10, "果汁": 20, "薯條": 15, "披薩": 2}
for key, value in food_list.items():
    if key == "果汁":
        print(key + ": " + str(value) + "杯")
    else:
        print(key + ": " + str(value) + "份")


food_list["冰淇淋"] = 10
food_list["果汁"] = 25
food_list["熱狗"] = 20
parents_food_list = {"蛋糕": 1, "三明治": 10, "果汁": 20, "薯條": 15, "披薩": 2}
print("還需購買的食物及數量:")
for key, value in food_list.items():
    if key in parents_food_list:
        if value > parents_food_list[key]:
            print(key + ": " + str(value - parents_food_list[key]))
    else:
        print(key + ": " + str(value))
print("party over")

food_list["蛋糕"] = 0
food_list["三明治"] = 5
food_list["果汁"] = 8
food_list["薯條"] = 10
food_list["披薩"] = 1
food_list["冰淇淋"] = 3
food_list["熱狗"] = 0
delete_list = []

for key, value in food_list.items():
    if value == 0:
        delete_list.append(key)

for i in delete_list:
    food_list.pop(i)

for key, value in food_list.items():
    if key == "果汁":
        print(key + ": " + str(value) + "杯")
    else:
        print(key + ": " + str(value) + "份")

gifts = {
    "小明": "樂高積木",
    "小花": "畫筆",
    "小強": "足球",
    "小美": "書",
    "小偉": "遙控車",
}
# 顯示一共收到了多少個禮物
print("一共收到了" + str(len(gifts)) + "個禮物")
for name, gift in gifts.items():
    print(name + "送了你一個" + gift)
