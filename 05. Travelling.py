destination = input()

total_sum_for_trip = 0
money_typed = 0

while destination != "End":
    budget = float(input())
    while total_sum_for_trip <= budget:
        money_saved = float(input())
        total_sum_for_trip += money_saved
        if total_sum_for_trip >= budget:
            print(f"Going to {destination}!")
            break
    total_sum_for_trip = 0
    destination = input()