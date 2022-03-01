numbers = int(input())

average_number = 0

for numbers in range(1, numbers +1):
    x_amount_numbers = int(input())
    average_number += x_amount_numbers

average_sum = average_number / numbers
print(f"{average_sum:.2f}")