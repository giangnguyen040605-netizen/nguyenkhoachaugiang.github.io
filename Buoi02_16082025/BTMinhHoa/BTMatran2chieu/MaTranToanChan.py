# Đọc số dòng và số cột
n, m = map(int, input().split())

# Khởi tạo biến kiểm tra
toan_chan = True

# Nhập ma trận và kiểm tra từng phần tử
for i in range(n):
    row = list(map(int, input().split()))
    for num in row:
        if num % 2 != 0:   # nếu gặp số lẻ
            toan_chan = False

# Xuất kết quả
if toan_chan:
    print("Mang A toan chan!")
else:
    print("Mang A khong toan chan!")