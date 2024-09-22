a = 10
print((lambda x: x + 10)(a))
add_ten = lambda x: x + 10
print(add_ten(5))


def my_func(n):
    return lambda x: x * n


double = my_func(2)
print(double(5))
triple = my_func(3)
print(triple(5))
