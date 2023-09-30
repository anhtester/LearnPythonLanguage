print("\n===break in for===")
for i in range(1, 11):
    if (i > 5):
        break
    print(i)

print("\n===break in while===")
n = 0
while (n < 10):
    print(n)
    n += 1
    if (n > 5):
        break

print("\n===continue in while===")
n = 0
while (n < 10):
    if (n < 5):
        n += 1
        continue
    print(n)
    n += 1
"""
- Ý nghĩa của continue là nó sẽ không thực hiện phần dưới
mà sẽ nhảy ngược lên trên chạy lại
"""
