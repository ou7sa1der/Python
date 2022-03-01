bottles_of_soap = int(input())

sum_dishes = 0
sum_pots = 0
quantity_soap = bottles_of_soap * 750
counter = 0

command = input()
while command != "End":
    counter += 1
    if counter == 1:
        dishes_ready = int(command)
        sum_dishes += dishes_ready
        dishes_loaded = dishes_ready * 5
        total_soap_left = quantity_soap - dishes_loaded
    elif counter != 1 and counter % 3 != 0:
        dishes_ready = int(command)
        sum_dishes += dishes_ready
        dishes_loaded = dishes_ready * 5
        total_soap_left -= dishes_loaded
    elif counter % 3 == 0:
        pots_ready = int(command)
        sum_pots += pots_ready
        pots_loaded = pots_ready * 15
        total_soap_left -= pots_loaded
    if total_soap_left <= 0:
        break
    command = input()
if command == "End":
    print("Detergent was enough!")
    print(f"{sum_dishes} dishes and {sum_pots} pots were washed.")
    print(f"Leftover detergent {total_soap_left} ml.")
else:
    print(f"Not enough detergent, {abs(total_soap_left)} ml. more necessary!")