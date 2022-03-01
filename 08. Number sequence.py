import sys
numbers_count = int(input())

max_number = -sys.maxsize
min_number = sys.maxsize

for numbers_count in range(1, numbers_count + 1):
    number = int(input())
    if number < min_number:
        min_number = number
    else:
        number = number
    if number > max_number:
        max_number = number
    else:
        number = number
print(f"Max number: {max_number}")
print(f"Min number: {min_number}")