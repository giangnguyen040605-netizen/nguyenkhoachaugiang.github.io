# Nhập số dòng và số cột
n, m = map(int, input().split())

# Nhập ma trận
A = []
for i in range(n):
    row = list(map(int, input().split()))
    A.append(row)

# Xuất ma trận
print("Array A:")
for row in A:
    print(" ".join(map(str, row)))