pairs = int(input())

sum_numbers = 0
count_numbers = 0
pair_sum = 0
pair_count = 0
x_pair_sum = 0
y_pair_sum = 0
number_one = 0
number_two = 0


for numbers in range(1, pairs * 2):
    if count_numbers % 2 == 0:
        numbers = int(input())
        count_numbers += 1
        number_two = numbers
        pair_count += 1
        if pair_count <= 1:
            pair_sum_one = sum_numbers
        elif pair_count == pairs:
            y_pair_sum = number_one + number_two
        else:
            x_pair_sum = number_one + number_two
    else:
        pass
    numbers = int(input())
    sum_numbers += numbers
    count_numbers += 1
    number_one = numbers

if pair_sum_one != x_pair_sum: or y_pair_sum != x_pair_sum:

    print(f"No, maxdiff = {Difference}")