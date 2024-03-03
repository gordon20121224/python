# sum = input("please enter a num:")
# print(sum)
# sum = int(sum)
# for i in range(1, sum):
#     if i % 3 == 0 or i % 7 == 0:
#         print(i)

n - int(input("enter num:"))

for i in range(n):
    print(i)
    print(" " * (n - 1 - i) + "* " * (i * 2 + 1))
for i in range(n):
    print(" " * (n - 1) + "*")
