# Đọc kích thước ma trận
n = int(input())

# Đọc ma trận
A = []
for _ in range(n):
    row = list(map(int, input().split()))
    A.append(row)

# Lấy các phần tử trên chéo chính
cheo_chinh = [A[i][i] for i in range(n)]

# Lấy các phần tử trên chéo phụ
cheo_phu = [A[i][n - 1 - i] for i in range(n)]

# Xuất kết quả
print("Cac phan tu tren cheo chinh:", " ".join(map(str, cheo_chinh)))
print("Cac phan tu tren cheo phu:", " ".join(map(str, cheo_phu)))