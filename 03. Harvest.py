from math import floor,ceil

square_meters_field = int(input())
grape_for_sq_m = float(input())
needed_liters_wine = int(input())
workers_count = int(input())

square_meters = square_meters_field * grape_for_sq_m
harvest_for_wine = square_meters * 0.40 / 2.5

if harvest_for_wine >= needed_liters_wine:
    liters_over = harvest_for_wine - needed_liters_wine
    liters_per_person = liters_over / workers_count
    print(f"Good harvest this year! Total wine: {floor(harvest_for_wine)} liters.")
    print(f"{ceil(liters_over)} liters left -> {ceil(liters_per_person)} liters per person.")
else:
    liters_needed = needed_liters_wine - harvest_for_wine
    print(f"It will be a tough winter! More {floor(liters_needed)} liters wine needed.")