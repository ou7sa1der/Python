numbers_count = int(input())

number_in_range_one = 0
number_in_range_two = 0
number_in_range_three = 0



for numbers_count in range(1, numbers_count + 1):
    number = int(input())
    if number % 2 == 0:
        number_in_range_one += 1
    if number % 3 == 0:
        number_in_range_two += 1
    if number % 4 == 0:
        number_in_range_three += 1

p1 = number_in_range_one / numbers_count * 100
p2 = number_in_range_two / numbers_count * 100
p3 = number_in_range_three / numbers_count * 100


print(f"{p1:.2f}%")
print(f"{p2:.2f}%")
print(f"{p3:.2f}%")