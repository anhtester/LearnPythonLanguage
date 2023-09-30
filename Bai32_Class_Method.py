
"""
ĐẶC ĐIỂM CỦA THAM SỐ SELF
- self là tham số bắt buộc chứ self không phải là từ khoá nên chúng ta đặt tên gì cũng được, bắt buộc đặt tham số đó ở đầu tiên.
- self thuộc về đối tượng của lớp chứ không thuộc về lớp, nên khi lấy đối tượng lớp để gọi thì buộc có self.
, nếu hàm không có self thì báo lỗi. (getAddress)
- self cũng được sử dụng để tham chiếu đến một trường biến trong lớp.


SỰ KHÁC BIỆT GIỮA HÀM STATIC VÀ NON_STATIC TRONG PYTHON
- Hàm static thuộc về lớp chứ không thuộc về đối tượng lớp.
- Gọi hàm static thông qua tên class hoặc đối tượng class (giống Java).
- Gọi hàm non-static buộc dùng đối tượng class (giống Java)
VD hàm showInfo non-static => Nếu dùng Tên class chấm gọi sẽ báo lỗi
- Hàm static có thể không cần dùng tham số self.

"""

#Khác file buộc import để gọi class trong file mới được
import Bai31_Class_Method

class ThongTin:

    # Gọi thông qua đối tượng class
    print("\n===Gọi thông đối tượng class===")
    student = Bai31_Class_Method.Student("An", 27)
    student.getName()
    student.showInfo()
    student.getAddress()

    #Gọi thông qua tên class
    print("\n===Gọi thông qua tên class===")
    Bai31_Class_Method.Student("Bối Bối", 2).showInfo()
    Bai31_Class_Method.Student.showThongTin("Duyên", 30)

    # Gọi sai cách
    print("\n===Gọi sai cách===")
    #Student.showInfo() #hàm này non-static gọi thông qua đối tượng class mới được
    #Student.getAddress("O Mon") #Hàm này không gọi được dù cả thông qua tên class và đối tượng class
