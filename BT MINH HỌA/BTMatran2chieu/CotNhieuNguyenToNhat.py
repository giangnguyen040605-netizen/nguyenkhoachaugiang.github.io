def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return False
    return True

# Đọc n, m
n, m = map(int, input().split())

# Đọc ma trận
A = []
for _ in range(n):
    row = list(map(int, input().split()))
    A.append(row)

# Đếm số nguyên tố theo cột
prime_counts = [0] * m
for j in range(m):
    for i in range(n):
        if is_prime(A[i][j]):
            prime_counts[j] += 1

# Tìm số lượng nguyên tố nhiều nhất
max_count = max(prime_counts)

# Lấy các cột có nhiều nguyên tố nhất
result = [str(j) for j in range(m) if prime_counts[j] == max_count]

print("Cac cot nhieu nguyen to nhat:", " ".join(result))