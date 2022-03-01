friends_list = list(map(str, input().split(', ')))


black_list = []
lost_names = []
while True:
    command = input().split(' ')
    if 'Report' in command:
        break
    if 'Blacklist' == command[0]:
        action = command[0]
        name = command[1]
        if not name in friends_list:
            print(f'{name} was not found.')
        else:
            index = friends_list.index(name)
            print(f'{name} was blacklisted.')
            friends_list[index] = 'Blacklisted'
            black_list.append(name)

    if 'Error' == command[0]:
        index = int(command[1])
        name = friends_list[index]
        valid = 0 <= index < len(friends_list)
        if valid and name != 'Blacklisted' and name != 'Lost':
            lost_names.append(friends_list[index])
            print(f'{friends_list[index]} was lost due to an error.')
            friends_list[index] = 'Lost'

    if 'Change' == command[0]:
        index = int(command[1])
        name = command[2]
        valid = 0 <= index < len(friends_list)
        if valid:
            print(f'{friends_list[index]} changed his username to {name}.')
            friends_list[index] = name

print(f'Blacklisted names: {len(black_list)}')
print(f'Lost names: {len(lost_names)}')
print(" ".join(map(str, friends_list)))