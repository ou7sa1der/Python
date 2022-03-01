from math import floor,ceil
magnolias_count = int(input())
ziumbiuls_count = int(input())
roses_count = int(input())
cactus_count = int(input())
gift_price = float(input())

total_sum = (magnolias_count * 3.25) + (ziumbiuls_count * 4) + (roses_count * 3.5) + (cactus_count * 8)
sum_with_taxes = total_sum - (total_sum * 0.05)

if gift_price > sum_with_taxes:
    money_left = gift_price - sum_with_taxes
    print(f"She will have to borrow {ceil(money_left)} leva.")
else:
    money_needed = sum_with_taxes - gift_price
    print(f"She is left with {floor(money_needed)} leva.")