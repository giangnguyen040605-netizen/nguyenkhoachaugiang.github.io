def next_day(day, month, year):
    # Kiểm tra năm nhuận
    def is_leap(y):
        return (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0)
    
    # Số ngày mỗi tháng
    month_days = [31, 29 if is_leap(year) else 28, 31, 30, 31, 30,
                  31, 31, 30, 31, 30, 31]
    
    day += 1  # tăng 1 ngày
    
    if day > month_days[month-1]:
        day = 1
        month += 1
        if month > 12:
            month = 1
            year += 1
            
    return day, month, year

# Nhập dữ liệu
day = int(input())
month = int(input())
year = int(input())

# Tính ngày tiếp theo
d, m, y = next_day(day, month, year)

# Xuất kết quả
print(f"{d}/{m}/{y}")
