# Nhập số n
n = int(input())

# (a) Số chữ số
num_digits = len(str(n))

# (b) Tổng các chữ số
digits = [int(d) for d in str(n)]
sum_digits = sum(digits)

# (c) Chữ số cuối
last_digit = n % 10

# (d) Chữ số đầu
first_digit = int(str(n)[0])

# Xuất kết quả
print(f"{n} has {num_digits} digits.")
print(" + ".join(str(d) for d in digits) + f" = {sum_digits}.")
print(f"Last digit is {last_digit}.")
print(f"Fist digit is {first_digit}.")
