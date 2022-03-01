needed_experience = float(input())
count_of_battles = int(input())
collected_experience = 0
counter_for_battles = 0
for battles in range(1, count_of_battles + 1):
    if collected_experience >= needed_experience:
        print(f'Player successfully collected his needed experience for {counter_for_battles} battles.')
        exit()
    experience_earn_per_battle = float(input())
    counter_for_battles += 1
    if counter_for_battles % 3 == 0:
        collected_experience += experience_earn_per_battle + (experience_earn_per_battle * 0.15)
    elif counter_for_battles % 5 == 0:
        collected_experience += experience_earn_per_battle - (experience_earn_per_battle * 0.10)
    elif counter_for_battles % 15 == 0:
        collected_experience += experience_earn_per_battle + (experience_earn_per_battle * 0.05)
    else:
        collected_experience += experience_earn_per_battle

if collected_experience >= needed_experience:
    print(f'Player successfully collected his needed experience for {counter_for_battles} battles.')
else:
    print(f'Player was not able to collect the needed experience, {needed_experience - collected_experience:.2f} more needed.')