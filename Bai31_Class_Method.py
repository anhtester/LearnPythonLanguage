class Student:

    # Thuộc tính
    address = "Can Tho"

    # Contructor
    def __init__(self, name, age):
        print("Hàm xây dựng có tham số.")
        self.name = name
        self.age = age

    # def __init__(self):
    #     print("Hàm xây dựng không tham số.")

    def getName(self):
        return self.name

    #Not use self
    #Not use static
    #Hàm này không gọi được dù cả thông qua tên class và đối tượng class
    def getAddress(address):
        print(address)

    def getAddress(self):
        print(self.address)

    def showInfo(self):
        print(self.name)
        print(self.address) #self cũng được sử dụng để tham chiếu đến một trường biến trong lớp

    @staticmethod
    def showThongTin(name, age):
        print(name)
        print(age)

#Khác class nhưng cùng file nên không cần import file
class ThongTin:
    # Gọi thông qua đối tượng class
    print("\n===Gọi thông qua đối tượng class===")
    student = Student("An", 27)
    student.getName()
    student.showInfo()
    student.getAddress()

    #Gọi hàm xây dựng không tham số
    # student2 = Student()
    # student2.getAddress()

    #Gọi thông qua tên class
    print("\n===Gọi thông qua tên class===")
    Student("Bối Bối", 2).showInfo()
    Student.showThongTin("Duyên", 30)

    # Gọi sai cách
    print("\n===Gọi sai cách===")
    #Student.showInfo() #hàm này non-static gọi thông qua đối tượng class mới được
    #Student.getAddress("O Mon") #Hàm này không gọi được dù cả thông qua tên class và đối tượng class