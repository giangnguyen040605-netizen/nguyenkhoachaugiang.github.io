old_index = int(input())
new_index = int(input())

# Tính số m3 tiêu thụ
used = new_index - old_index

# Định mức 4 m3 đầu tiên: 4.400 đ/m3
if used <= 4:
    cost = used * 4400
elif used <= 6:
    cost = 4 * 4400 + (used - 4) * 8300
else:
    cost = 4 * 4400 + 2 * 8300 + (used - 6) * 10500

# Xuất kết quả
print(f"Payment for {used} m^3 in month is {cost:,} VND.")

