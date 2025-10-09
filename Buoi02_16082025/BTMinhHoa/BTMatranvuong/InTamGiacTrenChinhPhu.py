# Đọc kích thước ma trận
n = int(input())

# Đọc ma trận vuông
A = []
for _ in range(n):
    row = list(map(float, input().split()))
    A.append(row)

# Tam giác trên chéo chính (j > i)
tam_giac_chinh = []
for i in range(n):
    for j in range(i + 1, n):
        tam_giac_chinh.append(A[i][j])

# Tam giác trên chéo phụ (i + j < n - 1)
tam_giac_phu = []
for i in range(n):
    for j in range(n):
        if i + j < n - 1:
            tam_giac_phu.append(A[i][j])

# Xuất kết quả
print("Tam giac tren cheo chinh:", " ".join(map(str, map(int, tam_giac_chinh))))
print("Tam giac tren cheo phu:", " ".join(map(str, map(int, tam_giac_phu))))