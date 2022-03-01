days_count = int(input())
confectioner_count = int(input())
cakes_count = int(input())
waffles_count = int(input())
pancakes_count = int(input())

cake_price = 45
waffles_price = 5.80
pancakes_price = 3.20

cakes_day_money = cakes_count * cake_price
waffles_day_money = waffles_count * waffles_price
pancakes_day_money = pancakes_count * pancakes_price

total_money_for_one_confectioner_for_a_day = (cakes_day_money + waffles_day_money + pancakes_day_money) * confectioner_count
total_sum = total_money_for_one_confectioner_for_a_day * days_count
final_sum_after_expences = total_sum - (total_sum / 8)

print(final_sum_after_expences)