w = int(input("輸入體重: "))
h = float(input("輸入身高: "))
bmi = w / (h * h)
print(bmi)
if bmi > 20.7:
    print("high")
elif 14.8 < bmi < 20.7:
    print("usual")
elif bmi < 14.8:
    print("low")

a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))

if a + b > c and a + c > b and b + c > a:
    print(f"周長:{(a + b + c)}")


    p = ( a + b + c) / 2
    area = (p * (p - a ) * )