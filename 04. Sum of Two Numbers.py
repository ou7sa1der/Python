start_number = int(input())
end_number = int(input())
magic_number = int(input())
combination_count = 0
magic_number_count = 0
start_number_count = start_number
end_number_count = end_number
action_found = False

for start_number in range(start_number, end_number + 1):
    for end_number in range(start_number_count, end_number + 1):
        action = start_number + end_number
        combination_count += 1
        if action == magic_number:
            magic_number_count = combination_count
            print(f"Combination N:{magic_number_count} ({start_number} + {end_number} = {magic_number})")
            action_found = True
            break
    if action == magic_number:
        magic_number_count = combination_count
        break
if not action_found:
    print(f"{combination_count} combinations - neither equals {magic_number}")