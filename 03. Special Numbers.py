number = int(input())
action_with_numbers = 0

for number in range(1, number + 1):
    string_number = str(number)
    for index in string_number:
        action_with_numbers += int(index)
    if action_with_numbers == 5 or action_with_numbers == 7 or action_with_numbers == 11:
        print(f'{number} -> True')
        action_with_numbers = 0
    else:
        print(f'{number} -> False')
        action_with_numbers = 0
