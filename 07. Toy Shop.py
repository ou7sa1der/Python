trip_price = float(input())
puzzles_count = int(input())
talking_dolls_count = int(input())
bears_count = int(input())
minions_count = int(input())
trucks_count = int(input())


#    • Пъзел - 2.60 лв.
 #   • Говореща кукла - 3 лв.
 #   • Плюшено мече - 4.10 лв.
 #   • Миньон - 8.20 лв.
 #   • Камионче - 2 лв.


whole_toys_sum = puzzles_count * 2.6 + talking_dolls_count * 3 + bears_count * 4.1 + minions_count * 8.2 + trucks_count * 2
all_toys_count = puzzles_count + talking_dolls_count + bears_count + minions_count + trucks_count

#ako igrachkite sa 50 ili poveche ima 25% otstupka
if all_toys_count >= 50:
    discount = whole_toys_sum * 0.25
    final_price = whole_toys_sum - discount
    rent = final_price * 0.10
    profit = final_price - rent
    if profit >= trip_price:
        money_left = profit - trip_price
        print(f"Yes! {money_left:.2f} lv left.")
    else:
        money_needed = trip_price - profit
        print(f"Not enough money! {money_needed:.2f} lv needed.")
#ako ne samo 10% naem
elif all_toys_count < 50:
    rent = whole_toys_sum * 0.1
    profit = whole_toys_sum - rent
    if profit >= trip_price:
        money_left = profit - trip_price
        print(f"Yes! {money_left:.2f} lv left.")
    else:
        money_needed = trip_price - profit
        print(f"Not enough money! {money_needed:.2f} lv needed.")