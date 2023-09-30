# Bảng cửu chương
for i in range(1, 11):
    print("2 x {0} = {1}".format(i, 2 * i))

# Vòng lặp lồng nhau
for i in range(2, 10):
    print("===Bảng cửu chương {0}===".format(i))
    for j in range(1, 11):
        print("{0} x {1} = {2}".format(i, j, (i * j)))
