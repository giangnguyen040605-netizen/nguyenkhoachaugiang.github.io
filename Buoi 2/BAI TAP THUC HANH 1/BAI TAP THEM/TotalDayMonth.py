import sys

def is_leap_year(year):
    return (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0)

def main():
    m, y = map(int, sys.stdin.read().strip().split())
    if m < 1 or m > 12:
        print("Thang khong hop le")
        return
    if m in [1, 3, 5, 7, 8, 10, 12]:
        days = 31
    elif m in [4, 6, 9, 11]:
        days = 30
    else:
        days = 29 if is_leap_year(y) else 28
    print(days)

if __name__ == "__main__":
    main()
