# Tập hợp nguyên âm (cả hoa và thường)
nguyen_am = set("aeiouAEIOU")

# Đọc n, m
n, m = map(int, input().split())

max_count = -1
dong_max = -1

for i in range(1, n + 1):
    row = input().split()
    count = sum(1 for ch in row if ch in nguyen_am)
    if count > max_count:
        max_count = count
        dong_max = i

print(f"Dong {dong_max} co nhieu nguyen am nhat voi so luong nguyen am la {max_count}.")