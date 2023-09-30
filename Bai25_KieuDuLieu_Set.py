"""
- Set giống trong Java
- Set không có thứ tự và giá trị không được trùng nhau
nếu trùng sẽ hiểu chỉ 1 giá trị
- Set khai báo bằng dấu {}
"""

drivers = {"123", "456", "789"}
print(drivers)

browsers = {"chrome", "chrome"}
print(browsers)

print("\n====Duyệt Set====")
for i in drivers:
    print(i)

print("\n====Thêm 1 phần tử vào Set====")
browsers.add("edge")
print(browsers)

print("\n====Thêm nhiều phần tử vào Set====")
browsers_add = {"firefox", "safari"}
browsers.update(browsers_add)
print(browsers)

print("\n====Thêm List vào Set====")
# Nó bỏ qua các giá trị trùng từ List
listMode = {"true", "false", "true"}
browsers.update(listMode)
print(browsers)

print("\n====Xoá giá trị trong Set====")
browsers.remove("chrome")
print(browsers)
# remove nếu không có thì báo lỗi, discard nếu không có thì thôi
# Nên dùng discard
browsers.discard("chrome")
print(browsers)
