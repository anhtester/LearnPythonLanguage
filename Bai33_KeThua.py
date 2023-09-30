class BaseTest:

    driver = None
    url = "https://anhtester.com"

    def getDriver(self):
        if self.driver is None:
            print("Biến driver có giá trị null. (None)")
        else:
            print("Giá trị biến driver là: ", self.driver)

        return self.driver

    def getUrl(self):
        return self.url

baseTest = BaseTest()
baseTest.getDriver()
print(baseTest.getUrl())


#Kế thừa từ class BaseTest
class LoginTest(BaseTest):

    def loginTest(self):
        #Dùng từ khoá super() để gọi hàm trực tiếp từ class Cha
        print(super().getDriver())
        print(super().getUrl())

loginTest = LoginTest()
loginTest.loginTest()

#Gọi hàm ở class Cha thông qua đối tượng class con
print("\n===Gọi hàm ở class Cha thông qua đối tượng class con===")
print(loginTest.getUrl())

#Đa kế thừa

class Action:
    def __init__(self, driver):
        self.driver = driver

    def clickElement(self):
        print(self.driver, "Click Element")

#Sử dụng đa kế thừa
class CustomerTest(BaseTest, Action):
    def __init__(self):
        BaseTest.__init__(self)
        Action.__init__(self,"chromedriver")


#Gọi hàm từ 2 class Cha
print("\n===Gọi hàm từ 2 class Cha===")
customer = CustomerTest()
print(customer.getDriver())
customer.clickElement()