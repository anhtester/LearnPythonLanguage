"""
- Dictionary giống với Map trong Java
- Cấu trúc dạng key:value
- Key không được trùng tên, nhưng có thể trùng giá trị
- Từ Python 3.7 thì các Dictionary được sắp xếp theo thứ tự
- Dicctionary được khai báo bằng dấu ngoặc nhọn {}, phân cách dấu phẩy
"""

sinhVien = {
    "hoTen": "Anh Tester",
    "lop": "Auto Test",
    "ngonNgu": "Python"
}

print(sinhVien)

# Sử dụng get() để lấy giá trị thông qua key
print("\n===Sử dụng get() để lấy giá trị thông qua key===")
print(sinhVien["hoTen"])
print(sinhVien.get("lop"))

# Cập nhật giá trị của key
print("\n===Cập nhật giá trị===")
sinhVien["hoTen"] = "Duyên"
print(sinhVien)
sinhVien.update({"ngonNgu": "Vietnam", "diem": 10, "diaChi": "Can Tho"})
print(sinhVien)

# Xoá giá trị thông qua key
print("\n===Xoá giá trị thông qua key===")
sinhVien.pop("ngonNgu")
print(sinhVien)

# Xoá key:value cuối cùng
sinhVien.popitem()
print(sinhVien)

# Xoá với từ khoá del
del sinhVien["hoTen"]
print(sinhVien)

# Duyệt từng key thông qua for
print("\n===Duyệt thông qua for===")
for i in sinhVien:
    print(i)

# Duyệt từng key thông qua for với hàm keys()
print("\n===Duyệt thông qua for===")
for i in sinhVien.keys():
    print(i)

# Duyệt từng value thông qua for với hàm values()
print("\n===Duyệt thông qua for===")
for i in sinhVien.values():
    print(i)

# Duyệt từng key value thông qua for với hàm items()
print("\n===Duyệt thông qua for===")
for x, y in sinhVien.items():
    print(x, ":", y, sep="")
