wagons = int(input())
command = input().split(' ')

list_wagons = [0] * wagons

while 'End' not in command:
    if command[0] == 'add':
        list_wagons[-1] += int(command[1])
    elif command[0] == 'insert':
        list_wagons[int(command[1])] += int(command[2])
    elif command[0] == 'leave':
        list_wagons[int(command[1])] -= int(command[2])
    command = input().split(' ')
print(list_wagons)

