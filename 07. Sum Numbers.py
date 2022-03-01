numbers_count = int(input())

numbers_sum = 0

for numbers_count in range(1, numbers_count + 1):
    number = int(input())
    numbers_sum += number
print(numbers_sum)