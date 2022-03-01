numbers_count = int(input())

number_in_range_one = 0
number_in_range_two = 0
number_in_range_three = 0
number_in_range_four = 0
number_in_range_five = 0


for numbers_count in range(1, numbers_count + 1):
    number = int(input())
    if number < 200:
        number_in_range_one += 1
    elif number < 400:
        number_in_range_two += 1
    elif number < 600:
        number_in_range_three += 1
    elif number < 800:
        number_in_range_four += 1
    else:
        number_in_range_five += 1

p1 = number_in_range_one / numbers_count * 100
p2 = number_in_range_two / numbers_count * 100
p3 = number_in_range_three / numbers_count * 100
p4 = number_in_range_four / numbers_count * 100
p5 = number_in_range_five / numbers_count * 100

print(f"{p1:.2f}%")
print(f"{p2:.2f}%")
print(f"{p3:.2f}%")
print(f"{p4:.2f}%")
print(f"{p5:.2f}%")