# Nhập dữ liệu
a = float(input())
b = float(input())
op = input().strip()   # phép toán (+, -, *, /)

# Xử lý theo phép toán
if op == "+":
    kq = a + b
    print(f"{a} + {b} = {kq}")
elif op == "-":
    kq = a - b
    print(f"{a} - {b} = {kq}")
elif op == "*":
    kq = a * b
    print(f"{a} * {b} = {kq}")
elif op == "/":
    if b == 0:
        print("Khong chia duoc cho 0")
    else:
        kq = a / b
        print(f"{a} / {b} = {kq}")
else:
    print("Phep toan khong hop le")
