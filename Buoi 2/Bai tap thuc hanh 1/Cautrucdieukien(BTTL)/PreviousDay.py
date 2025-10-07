# Hàm kiểm tra năm nhuận
def is_leap(year):
    return (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0)

# Hàm lấy số ngày trong tháng
def days_in_month(month, year):
    if month in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif month in [4, 6, 9, 11]:
        return 30
    elif month == 2:
        return 29 if is_leap(year) else 28
    else:
        return 0  # Trường hợp lỗi

# Hàm tính ngày trước đó
def previous_day(d, m, y):
    if d == 1 and m == 1:  # Ngày đầu năm
        return 31, 12, y - 1
    elif d == 1:  # Ngày đầu tháng
        m_prev = m - 1
        d_prev = days_in_month(m_prev, y)
        return d_prev, m_prev, y
    else:  # Các ngày còn lại
        return d - 1, m, y

# ===== Main program =====
d = int(input())
m = int(input())
y = int(input())

d_prev, m_prev, y_prev = previous_day(d, m, y)
print("Previous day of %d/%d/%d is %d/%d/%d." % (d, m, y, d_prev, m_prev, y_prev))
