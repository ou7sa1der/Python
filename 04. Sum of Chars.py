number_of_lines = int(input())
total_sum = 0
for character in range(1, number_of_lines + 1):
    letters = input()
    total_sum += ord(letters)
print(f'The sum equals: {total_sum}')