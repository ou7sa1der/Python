days_count_for_campaign = int(input())
candy_man_count = int(input())
cakes_count = int(input())
waffels_count = int(input())
pancakes_count = int(input())

cake = 45
waffel = 5.80
pancake = 3.20

# 1/8 ot krainata suma shte bude polzvana za pokrivane na razhodite

cakes_made = cakes_count * cake
waffel_made = waffels_count * waffel
pancake_made = pancakes_count * pancake

money_count_for_day = (cakes_made + waffel_made + pancake_made) * candy_man_count

money_count = money_count_for_day * days_count_for_campaign
money_count_after_payout = money_count - money_count / 8

print(money_count_after_payout)

