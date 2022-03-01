money_needed_for_trip = float(input())
money_on_hand = float(input())

spend_count = 0
days_spend = 5

money_saved_spend = 0
days_count = 0
action = input()
sum_saved_or_spend = float(input())

while money_saved_spend < money_needed_for_trip:
    days_count += 1
    if action == "save":
        spend_count = 0
        if days_count == 1:
            money_saved_spend = money_on_hand + sum_saved_or_spend
        if days_count != 1:
            money_saved_spend += sum_saved_or_spend
        if money_saved_spend >= money_needed_for_trip:
            print(f"You saved the money for {days_count} days.")
            break
    if action == "spend":
        spend_count += 1
        if days_count == 1 or sum_saved_or_spend < money_on_hand:
            money_saved_spend = money_on_hand - sum_saved_or_spend
        if days_count != 1:
            money_saved_spend -= sum_saved_or_spend
        if sum_saved_or_spend > money_on_hand or sum_saved_or_spend > money_saved_spend:
            money_saved_spend = 0
        if days_count == spend_count == days_spend:
            print("You can't save the money.")
            print(f"{days_spend}")
            break
    action = input()
    sum_saved_or_spend = float(input())