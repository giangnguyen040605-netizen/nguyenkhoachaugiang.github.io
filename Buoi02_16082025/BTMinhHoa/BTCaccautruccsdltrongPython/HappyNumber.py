def is_happy(n: int) -> bool:
    seen = set()
    while n != 1 and n not in seen:
        seen.add(n)
        n = sum(int(digit) ** 2 for digit in str(n))
    return n == 1

if __name__ == "__main__":
    # Đọc input từ file
    with open("HappyNumber.inp", "r", encoding="utf-8") as f:
        n = int(f.readline().strip())
    
    result = is_happy(n)

    # Ghi output ra file
    with open("HappyNumber.out", "w", encoding="utf-8") as f:
        f.write(str(result) + "\n")

