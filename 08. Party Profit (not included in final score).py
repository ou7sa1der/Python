party_size = int(input())
days = int(input())
coins = 0
total_coin = 0

for days in range(1, days + 1):
    coins += 50
    if days % 10 == 0:
        party_size -= 2
    if days % 15 == 0:
        party_size += 5
    if days == 1:
        spend_coins_for_food = coins - (2 * party_size)
        left_coins_after = spend_coins_for_food
    else:
        left_coins_after = 50 + total_coin - (2 * party_size)
    if days % 3 == 0:
        left_coins_after -= (party_size * 3)
    if days % 5 == 0:
        left_coins_after += (party_size * 20)
        if days % 3 == 0:
            left_coins_after -= (party_size * 2)
    total_coin = left_coins_after
coins_received_per_person = left_coins_after / party_size
print(f"{party_size} companions received {int(coins_received_per_person)} coins each.")