toan = int(input())
ly = int(input())
hoa = int(input())

dtb = (toan*2 + ly*3 + hoa) / 6

if 8 <= dtb <= 10:
    rating = "Good"
elif 6.5 <= dtb < 8:
    rating = "Pretty"
elif 5 <= dtb < 6.5:
    rating = "Average"
else:
    rating = "Weak"

print(f"Average point = {dtb:.2f}, rating {rating}.")
