def majority_element(nums):
    count = {}
    for num in nums:
        count[num] = count.get(num, 0) + 1
    
    n = len(nums)
    for num, freq in count.items():
        if freq > n // 2:   # strictly lớn hơn n/2
            return num
    return None  # nếu không tồn tại

# Đọc input
with open("MajorityElement.inp", "r", encoding="utf-8") as f:
    n = int(f.readline().strip())
    nums = list(map(int, f.readline().split()))

# Ghi output
result = majority_element(nums)
with open("MajorityElement.out", "w", encoding="utf-8") as f:
    f.write(str(result))


