"""
- Dùng từ khoá def để khai báo tên hàm
"""


def getName():
    print("An")


getName()

# Hàm có tham số cố định
print("\n===Hàm có tham số cố định===")


def tinhTong(a, b):
    print(a + b)


tinhTong(2, 5)

# Hàm nhiều tham số không xác định
print("\n===Hàm nhiều tham số không xác định===")


def thoiKhoaBieu(*monHoc):
    print("Mon 1: " + monHoc[0])
    print("Mon 2: " + monHoc[1])


thoiKhoaBieu("Toan", "Ly")

# Hàm nhiều tham số xác định thông qua tên key
print("\n===Hàm nhiều tham số xác định thông qua tên key===")


def xinChao(**hoTen):
    print("First Name: " + hoTen["ho"])
    print("Last Name: " + hoTen["ten"])


xinChao(ho="Vo", ten="Thai An")

# Hàm trả về kết quả - return
print("\n===Hàm trả về kết quả - return===")


def tinhTong(*giaTri):
    tong = 0
    for i in giaTri:
        tong += i
    return tong


print(tinhTong(2, 5, 7))
tong1 = tinhTong(1, 2, 3)
tong2 = tinhTong(4, 5, 6)
print(tong1 + tong2)
