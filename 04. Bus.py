#Също така, на всеки нечетен брой спирки се качват по двама проверяващи и слизат на четните спирки.
passgengers = int(input())
stops = int(input())
count_passengers = 0
checkers = 2

for stops_count in range(1, stops + 1):
    passengers_out = int(input())
    passengers_in = int(input())
    if stops_count == 1:
            if passengers_out > passengers_in:
                count_passengers = passgengers - (passengers_out - passengers_in) + checkers
            elif passengers_in >= passengers_out:
                count_passengers = passgengers + (passengers_in - passengers_out) + checkers
    elif stops_count > 1:
        if stops_count % 2 == 0:
            if passengers_out > passengers_in:
                count_passengers = count_passengers - (passengers_out - passengers_in) - checkers
            elif passengers_in >= passengers_out:
                count_passengers = count_passengers + (passengers_in - passengers_out) - checkers
        elif stops_count % 2 != 0:
            if passengers_out > passengers_in:
                count_passengers = count_passengers - (passengers_out - passengers_in) + checkers
            elif passengers_in >= passengers_out:
                count_passengers = count_passengers + (passengers_in - passengers_out) + checkers

print(f"The final number of passengers is : {count_passengers}")