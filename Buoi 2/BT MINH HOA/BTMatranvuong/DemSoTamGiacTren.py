def main():
    import sys
    data = sys.stdin.read().strip().split()
    n = int(data[0])
    nums = list(map(float, data[1:]))
    A = [nums[i*n:(i+1)*n] for i in range(n)]

    so_am = so_duong = so_khong = 0

    # chỉ đếm tam giác trên (j > i)
    for i in range(n):
        for j in range(i+1, n):
            v = A[i][j]
            if abs(v) < 1e-9:
                so_khong += 1
            elif v > 0:
                so_duong += 1
            else:
                so_am += 1

    print("Trong nua tam giac tren cheo chinh:")
    print("+ {} so am".format(so_am))
    print("+ {} so duong".format(so_duong))
    print("+ {} so khong".format(so_khong))

if __name__ == "__main__":
    main()
