money_amount = float(input())
money_amount_in_coins = int(money_amount * 100)
coins_counter = 0
coins_counter += money_amount_in_coins // 200
money_amount_in_coins %= 200
coins_counter += money_amount_in_coins // 100
money_amount_in_coins %= 100
coins_counter += money_amount_in_coins // 50
money_amount_in_coins %= 50
coins_counter += money_amount_in_coins // 20
money_amount_in_coins %= 20
coins_counter += money_amount_in_coins // 10
money_amount_in_coins %= 10
coins_counter += money_amount_in_coins // 5
money_amount_in_coins %= 5
coins_counter += money_amount_in_coins // 2
money_amount_in_coins %= 2
if money_amount_in_coins == 1:
    coins_counter += 1
print(coins_counter)