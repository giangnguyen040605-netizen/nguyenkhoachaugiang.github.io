import sys

def in_cac_duong_cheo(matrix, n):
    # Các đường song song chéo chính
    duong_cheo_chinh = []
    for k in range(2*n - 1):
        duong = []
        for i in range(n):
            j = k - i
            if 0 <= j < n:
                duong.append(matrix[i][j])
        if duong:
            duong_cheo_chinh.append(duong)

    # Các đường song song chéo phụ
    duong_cheo_phu = []
    for k in range(2*n - 1):
        duong = []
        for i in range(n):
            j = k - (n - 1 - i)
            if 0 <= j < n:
                duong.append(matrix[i][j])
        if duong:
            duong_cheo_phu.append(duong)

    return duong_cheo_chinh, duong_cheo_phu


if __name__ == "__main__":
    data = sys.stdin.read().strip().split()
    n = int(data[0])
    a = []
    idx = 1
    for i in range(n):
        row = list(map(int, data[idx:idx+n]))
        a.append(row)
        idx += n

    chinh, phu = in_cac_duong_cheo(a, n)

    print("Cac duong song song cheo chinh:", end=" ")
    for d in chinh:
        print(d, end="")
    print()

    print("Cac duong song song cheo phu:", end=" ")
    for d in phu:
        print(d, end="")
    print()