import sys

def read_three_numbers():
    """
    Đọc 3 số nguyên từ stdin nếu có (ví dụ khi dùng redirect file).
    Nếu không đủ token trong stdin, sẽ hỏi tương tác bằng input().
    """
    data = sys.stdin.read().strip().split()
    if len(data) >= 3:
        try:
            a, b, c = int(data[0]), int(data[1]), int(data[2])
            return a, b, c
        except ValueError:
            raise ValueError("Input file contains non-integer tokens.")
    # fallback interactive
    a = int(input("Nhap canh a: "))
    b = int(input("Nhap canh b: "))
    c = int(input("Nhap canh c: "))
    return a, b, c

def main():
    try:
        a, b, c = read_three_numbers()
    except Exception as e:
        print("Loi input:", e)
        return

    # sắp xếp để kiểm tra dễ: a <= b <= c
    a_s, b_s, c_s = sorted([a, b, c])

    if a_s + b_s > c_s:
        result = "Day la tam giac."
    else:
        result = "Khong phai tam giac."

    # In output rõ ràng
    print(f"Voi ba canh ({a_s}, {b_s}, {c_s}) -> {result}")

if __name__ == "__main__":
    main()


