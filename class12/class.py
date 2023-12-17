# def hello():
#     print("hello")
# def hello(name):
#     print("Hello" + str(name))
# hello("little pig")
# def my_min(a, b):
#     if a < b :
#         return a
#     else:
#         return b
# x = my_min(1, 2)
# print("my_min:" + str (x))

# def my_func(a, b)
#     print(a, b)
# my_func(1, 2)
# print(a)
# length = 5
# area = 3.14 *10**2


# def calculate_square_area():
#     global area
#     area = length **2
#     # len is global area

# calculate-square__area():
# print("is that" , area)
list = {}

# import random

# def roll_dice(n: int ):
#     dice = []
#     for i in range(n)
#     dice.append(random.randint(1, 6))
#     return dice


# sum = int(input('please enter a number :'))
# print(roll_dice(sum      ))
# 當寒寒士有預設值的變數應將這些變數放在函式參數列表的最後面
def my_function(a, b, c=0, d=0):
    print("a =", a)
    print("b =", b)
    print("c =", c)
    print("d =", d)


# my_function(1, 2)
# my_function(1, 2, 3)
# my_function(1,2,3,4)
my_function(
    1,
    2,
    d=4,
)
# error because there are no c
