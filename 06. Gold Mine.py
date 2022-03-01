locations_chosen = int(input())

total_gold_digged = 0

for count_locations in range(1, locations_chosen + 1):
    expected_gold_digging = float(input())
    days_on_locations = int(input())
    total_gold_digged = 0
    for days_count in range(1, days_on_locations + 1):
        amount_digged = float(input())
        total_gold_digged += amount_digged

    average_gold_digged = total_gold_digged / days_on_locations
    if average_gold_digged >= expected_gold_digging:
        print(f"Good job! Average gold per day: {average_gold_digged:.2f}.")
    else: #average_gold_digged < expected_gold_digging:
        gold_needed = expected_gold_digging - average_gold_digged
        print(f"You need {gold_needed:.2f} gold.")