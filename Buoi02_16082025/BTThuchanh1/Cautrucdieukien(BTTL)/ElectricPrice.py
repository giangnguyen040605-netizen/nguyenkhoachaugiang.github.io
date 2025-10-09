# Tính tiền điện hộ gia đình theo bậc thang + VAT 10%

def calc_electric_price(old_kwh, new_kwh):
    kwh = new_kwh - old_kwh

    if kwh <= 100:
        cost = kwh * 1242
    elif kwh <= 150:
        cost = 100 * 1242 + (kwh - 100) * 1304
    elif kwh <= 200:
        cost = 100 * 1242 + 50 * 1304 + (kwh - 150) * 1651
    elif kwh <= 300:
        cost = 100 * 1242 + 50 * 1304 + 50 * 1651 + (kwh - 200) * 1788
    elif kwh <= 400:
        cost = 100 * 1242 + 50 * 1304 + 50 * 1651 + 100 * 1788 + (kwh - 300) * 1912
    else:
        cost = (100 * 1242 + 50 * 1304 + 50 * 1651 +
                100 * 1788 + 100 * 1912 + (kwh - 400) * 1962)

    total = int(round(cost * 1.1))  # cộng VAT 10%
    return kwh, total

if __name__ == "__main__":
    old_kwh = int(input())
    new_kwh = int(input())
    kwh, total = calc_electric_price(old_kwh, new_kwh)
    print(f"The amount to pay for {kwh} kWh consumed in the month is {total:,} VND.")
