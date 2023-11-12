import random

# print random.randrange(3)
# print random randrange(0, 10, 2)

# random.randint(1, 3)
# random.randint(1, 10)




#   while True:
#      s = int(input("please enter a number between 1 to 100:"))
#     if n > s:
#          print("a bit small")
#      elif s > n:
#          print("a bit big")
#     elif n == s:
#         print("great")
#         break
# l = []
# print(l)
# l = [1, 2, 3,]
# print(l)
# l = [1, 2,3, 4] + [1, 2, 3]
# print(l)
# l = ["a", "b" ,"c"]


l = ["a","b", "c","D", "e" ,'f',"g","h", "i" ,"j"]
print(l)
print(l[0])
print(l[2])
print(l[-1])
print(l[-3])
print(l[0:3])
print(l[3:6])
print(l[0:10:2])
print(l[::2])

print(len(l))
for i in range(len(l))
print(l[i])
for i in range print(i)

juices_list = ["蘋果汁", "柳橙汁", "葡萄汁", "可樂", "系統關閉"]
while True:
    for i in range(len(juices_list)):
        print(str(i + 1) + ". " + juices_list[i])
    try:
        ans = int(input("請輸入編號:"))
    except:
        print("輸入錯誤查無此果汁，請重新輸入")
        continue
    if ans == len(juices_list):
        print("~~系統關閉~~")
        break
    elif ans > len(juices_list) or ans <= 0:
        print("輸入錯誤查無此果汁，請重新輸入")
    else:
        print("您點的商品是" + juices_list[ans - 1])

         這個城市能改審麼都會在listˊ中改