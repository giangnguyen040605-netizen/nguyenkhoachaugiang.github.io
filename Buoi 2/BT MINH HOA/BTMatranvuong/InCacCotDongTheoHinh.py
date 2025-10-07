import sys

def in_cac_dong_cot(matrix, n):
    # Các dòng zig-zag
    dong = []
    for i in range(n):
        if i % 2 == 0:  # chẵn -> trái sang phải
            dong.append(matrix[i])
        else:  # lẻ -> phải sang trái
            dong.append(matrix[i][::-1])

    # Các cột zig-zag
    cot = []
    for j in range(n):
        col = [matrix[i][j] for i in range(n)]
        if j % 2 == 0:  # chẵn -> trên xuống
            cot.append(col)
        else:  # lẻ -> dưới lên
            cot.append(col[::-1])

    return dong, cot


if __name__ == "__main__":
    data = sys.stdin.read().strip().split()
    n = int(data[0])
    a = []
    idx = 1
    for i in range(n):
        row = list(map(int, data[idx:idx+n]))
        a.append(row)
        idx += n

    dong, cot = in_cac_dong_cot(a, n)

    print("Cac dong:", end=" ")
    for d in dong:
        print(d, end="")
    print()

    print("Cac cot:", end=" ")
    for c in cot:
        print(c, end="")
    print()