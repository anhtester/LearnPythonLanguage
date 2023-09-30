#Giống với Java - dùng lặp với số lần không biết trước

n = 0
while(n<10):
    print(n)
    n+=1

#Dùng else sẽ chạy ngược lại khi while false
print("\n===Dùng else sẽ chạy ngược lại khi while false")
n = 0
while(n<5):
    print(n)
    n+=1
else:
    print("Ngoài vòng lặp")

#Dùng break để thoát khỏi vòng lặp
print("\n===Dùng break để thoát khỏi vòng lặp")
n = 0
while(n<10):
    print(n)
    n+=1
    if(n>5):
        break
else:
    print("Ngoài vòng lặp")