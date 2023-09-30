a = 5
b = 2

print(a + b)
print(a - b)
print(a * b)
print(a / b)  # a chia b lấy đúng số thập phân luôn
print(a // b)  # a chia b lấy phần nguyên
print(a ** b)  # a mũ b
print(a % b)  # lấy phần dư của a chia b

# Toán tử so sánh
print(a > b)
print(a < b)
print(a == b)
print(a != b)
print(a >= b)
print(a <= b)

print("{0} < {1} là {2}".format(a, b, a < b))

# Toán tử Logic
"""
- Phép VÀ dùng chữ and
- Phép HOẶC dùng chữ or
- Phủ định dùng chữ not
"""
c = 10
print(a > b and a < c)
print(a > b and a > c)
print(a > b or a > c)
print(not (a > b))  # Phủ định của a > b

# Toán tử gán
# Giống với cú pháp của Java
a = 10
b = 5
a += 2
b /= 2
print(a)
print(b)
