import math

a = float(input("Nhập vào a: "))
b = float(input("Nhập vào b: "))
c = float(input("Nhập vào c: "))

# Giải phương trình tìm nghiệm
if (a != 0):
    # Tính Delta b^2 - 4*a*c
    delta = delta = b ** 2 - 4 * a * c
    if (delta < 0):
        print("Phương trình vô nghiệm")
    elif (delta == 0):
        x = -b / (2 * a)
        print("Có nghiệm kép x1=x2=: ", x)
    else:
        x1 = (-b - math.sqrt(delta)) / (2 * a)
        x2 = (-b + math.sqrt(delta)) / (2 * a)
        print("Phương trình có nghiệm là: ")
        print("X1 =", x1)
        print("X2 =", x2)
else:
    print("Không phải phương trình bậc 2")
