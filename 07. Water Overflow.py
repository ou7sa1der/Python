# number_of_liters_poured = int(input())
# tank_liters = 255
# total_poured_water = 0
# line_count = 0
# for number_of_liters_poured in range(1, number_of_liters_poured + 1):
#     liters_water = int(input())
#     total_poured_water += liters_water
#     if total_poured_water > tank_liters and line_count == 0:
#         line_count = liters_water
#
#
# if line_count > 0:
#     final_liters = total_poured_water - line_count
#     print("Insufficient capacity!")
#     print(final_liters)
# else:
#     print(total_poured_water)

times_pouring_water = int(input())
water_tank_capacity = 255
poured_water = 0
actual_water_in_tank = 0
overflow_counter = 0
for amount_of_water in range(1, times_pouring_water + 1):
    liters_pouring = int(input())
    if poured_water == 0:
        actual_water_in_tank = liters_pouring
    poured_water += liters_pouring
    if poured_water > water_tank_capacity and overflow_counter == 0:
        print("Insufficient capacity!")
        overflow_counter += 1
        overflow_liters = liters_pouring

if actual_water_in_tank != 0 and overflow_counter == 0:
    print(poured_water)
elif overflow_counter > 0 and actual_water_in_tank != 0:
    actual_water_in_tank = poured_water - overflow_liters
    print(actual_water_in_tank)
elif actual_water_in_tank != 0:
    if water_tank_capacity > actual_water_in_tank:
        print(actual_water_in_tank)
    else:
        print(0)
else:
    print(poured_water)