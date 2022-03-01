import sys
number_count = int(input())

max_number = -sys.maxsize
min_number = sys.maxsize
total_sum = 0
even_number = 0

for number_count in range(1, number_count + 1):
    number = int(input())
    total_sum = total_sum + number
    if number > max_number:
        max_number = number
    if number < min_number:
        min_number = number

if max_number == total_sum - max_number:
    print("Yes")
    print(f"Sum = {max_number}")
else:
    print("No")
    difference = max_number - abs(max_number - total_sum)
    print(f"Diff = {abs(difference)}")