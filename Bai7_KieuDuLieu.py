#Python thuộc loại ngôn ngữ Thông dịch
#Nên chạy chương trình không cần biên dịch
#Java là ngôn ngữ cần biên dịch (compile trước khi chạy)

#Kiểu dữ liệu trong Python không bắt buộc khai báo kiểu của biến
#Mà gán giá trị cho nó, nó sẽ tự hiểu kiểu tương ứng

x = 5 #int
y = 10.5 #float
name = 'Anh Tester' #str
headless = True #True/False - boolean
z = None #NoneType - Ra giá trị null

print(x)
print(y)
print(name)
print(headless)
print(z)

#ƯU ĐIỂM
"""
- Viết mã nhanh hơn
- Mã ít hơn
"""
#NHƯỢC ĐIỂM
"""
- Thời gian chạy lâu hơn
- Khi xảy ra lỗi khó gỡ lỗi (chậm hơn)
vì cần tìm ra kiểu dữ liệu của các biến
"""
#VÍ DỤ
n = 5
print(type(n))
n = 2.345
print(type(n))
n = 'Python'
print(type(n))
n = True
print(type(n))