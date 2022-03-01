season = input()
km_a_month = float(input())

if km_a_month <= 5000:
    if season == "Autumn" or season == "Spring":
        price_for_km = 0.75
        sum_for_km = km_a_month * price_for_km
        wage_sum1 = (sum_for_km * 4)
        wage_sum2 = wage_sum1 - (wage_sum1 * 0.10)
    elif season == "Summer":
        price_for_km = 0.90
        sum_for_km = km_a_month * price_for_km
        wage_sum1 = (sum_for_km * 4)
        wage_sum2 = wage_sum1 - (wage_sum1 * 0.10)
    else:
        price_for_km = 1.05
        sum_for_km = km_a_month * price_for_km
        wage_sum1 = (sum_for_km * 4)
        wage_sum2 = wage_sum1 - (wage_sum1 * 0.10)
elif km_a_month > 5000 and km_a_month <= 10000:
    if season == "Autumn" or season == "Spring":
        price_for_km = 0.95
        sum_for_km = km_a_month * price_for_km
        wage_sum1 = (sum_for_km * 4)
        wage_sum2 = wage_sum1 - (wage_sum1 * 0.10)
    elif season == "Summer":
        price_for_km = 1.10
        sum_for_km = km_a_month * price_for_km
        wage_sum1 = (sum_for_km * 4)
        wage_sum2 = wage_sum1 - (wage_sum1 * 0.10)
    else:
        price_for_km = 1.25
        sum_for_km = km_a_month * price_for_km
        wage_sum1 = (sum_for_km * 4)
        wage_sum2 = wage_sum1 - (wage_sum1 * 0.10)
elif km_a_month > 10000 and km_a_month <= 20000:
        price_for_km = 1.45
        sum_for_km = km_a_month * price_for_km
        wage_sum1 = (sum_for_km * 4)
        wage_sum2 = wage_sum1 - (wage_sum1 * 0.10)

print(f"{wage_sum2:.2f}")