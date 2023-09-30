# Ghép chuỗi
s1 = "Anh Tester"
s2 = "Automation Testing"

s3 = s1 + s2
print(s3)
s3 = s1 + " " + s2
print(s3)

#In ra chuỗi nhiều dòng
s4 = """
Dòng 1
Dòng 2
"""
print(s4)

#\n dùng để xuống dòng và dùng dấu NHÂN để tăng chuỗi
s5 = "Python for Tester\n"
s5_10 = s5*10
print(s5_10)

#Kiểm tra chuỗi 1 chứa chuỗi 2
print("\n===Kiểm tra chuỗi 1 chứa chuỗi 2===")
s1 = "Xin chào Anh Tester"
s2 = "Tester"

if s2 in s1:
    print("Chuỗi s2 CÓ trong chuỗi s1")
else:
    print("Chuỗi s2 KHÔNG CÓ trong chuỗi s1")

print("\n===Chuyển chuỗi hoa thường===")
print(s1.lower())
print(s1.upper())

print("\n===Viết hoa chữ cái đầu===")
print(s1.capitalize())
s1 = str.capitalize(s1)
print(s1)

print("\n===Tìm kiếm chuỗi===")
s1 = "Lập trình Python đang là xu hướng hiện nay, chúng ta nên học Python."
#Trả về -1 nếu không tìm thấy, ngược lại trả về vị trí đầu tiên của chuỗi con đó
#Vị trí bắt đầu là 0 và tính luôn khoảng trắng
print(s1.find("trình"))
print(s1.find("Python"))
print(s1.find("123"))

print("\n===Đếm số lượng chuỗi con===")
print(s1.count("Python"))

print("\n===Tách chuỗi===")
print(s1.split(" "))

print("\n===Thay thế giá trị trong chuỗi===")
print(s1.replace(" ", "-"))
print(s1.replace(" ", "-", 4))

print("\n===Lấy ra chuỗi con theo vị trí===")
print(s1[0:9])