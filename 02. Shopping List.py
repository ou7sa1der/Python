grocery_list = input().split('!')

while True:
    command = input().split(' ')
    if 'Go' in command or 'Shopping!' in command:
        break
    elif 'Urgent' in command:
        if command[1] in grocery_list:
            continue
        else:
            grocery_list.insert(0,command[1])
    elif 'Unnecessary' in command:
        if command[1] in grocery_list:
            grocery_list.remove(command[1])
    elif 'Correct' in command:
        if command[1] in grocery_list:
            index = grocery_list.index(command[1])
            grocery_list.insert(index, command[2])
            grocery_list.remove(command[1])
        else:
            continue
    elif 'Rearrange' in command:
        if command[1] in grocery_list:
            grocery_list.remove(command[1])
            grocery_list.append(command[1])

print(', '.join(grocery_list))