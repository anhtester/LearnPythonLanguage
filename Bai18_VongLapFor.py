n = int(input("Nhập vào N: "))
tong = 0

# Vòng lặp tự tăng 1 đơn vị
for i in range(n + 1):
    tong += i

print("Tổng là: ", tong)

print("==================")
# Vòng lặp tăng đơn vị tuỳ ý
for j in range(0, 10, 2):
    print(j)

print("==================")
# Duyệt List phần tử
colors = ["Red", "Yellow", "Blue", "Green"]

# Giống for đơn giản trong Java
for i in range(len(colors)):
    print(colors[i])

print("==================")
# Giống for cải tiến trong Java
for color in colors:
    print(color)