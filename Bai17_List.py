# Kiểu dữ liệu List trong Python

# Tạo List rỗng
emptyList1 = []
print(emptyList1)

# Tạo một đối tượng List
emptyList2 = list()
print(emptyList2)

# Tạo list có dữ liệu
colorsList = ["Red", "Green", "Blue"]
print(colorsList)

studentList = list()
# Chèn phần tử vào list
studentList.insert(1, "An")
studentList.insert(2, "Duyên")
studentList.insert(3, "Bối")
# Thêm phần tử vào cuối
studentList.append("Uyên")
print(studentList)

# Truy xuất phần tử từ List
# List bắt đầu từ 0
print(colorsList[2])  # Blue
print(studentList[1])  # Duyên

# Duyệt List
print(studentList[0:4])  # In ra từ 0 đến nhỏ hơn 2 (0,1,2,3)
print(colorsList[0:2])  # (0,1)

# Length của List
print("Độ dài colorsList:", len(colorsList))
print("Độ dài studentList:", len(studentList))
# Đếm số lượng phần tử theo giá trị trong List
studentList.insert(4, "An")
print("Số bạn tên An:", studentList.count("An"))

# Xoá phần tử trong List theo giá trị
print(studentList)
studentList.remove("An")
print(studentList)
studentList.remove("An")
print(studentList)
# Xoá phần tử trong List theo vị trí
studentList.pop(1)
print(studentList)

# Kiểm tra phần tử trong List
if "Duyên" in studentList:
    print("Có bạn Duyên")
else:
    print("Không có bạn Duyên")

numberList = [1, 2, 5, 10, 8, 9]
print(numberList)
# Đảo ngược giá trị trong List
numberList.reverse()
print(numberList)
# Sắp xếp giá trị trong List
numberList.sort()
print(numberList)

numberList.sort(reverse=True)
print(numberList)

#List trong Python có thể lưu nhiều kiểu dữ liệu
exampleList = ["Java", "Python", 9, 10]
print(exampleList)
