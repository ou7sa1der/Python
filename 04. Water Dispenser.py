from collections import deque
liters = int(input())
command = input()


def creating_deque(command):
    people_waiting_for_water = deque()

    while not command == "Start":
        name = command
        people_waiting_for_water.append(name)
        command = input()

    return people_waiting_for_water


people_waiting_for_water = creating_deque(command)

command = input()
while not command == 'End' and people_waiting_for_water:

    if 'refill' in command:
        split_command = command.split(' ')
        refilling_liters = int(split_command[1])
        liters += refilling_liters
    else:
        person_in_line = people_waiting_for_water.popleft()
        needed_liters = int(command)
        liters -= needed_liters
        if liters < 0:
            liters += needed_liters
            print(f"{person_in_line} must wait")
        else:
            print(f"{person_in_line} got water")
    command = input()
print(f"{liters} liters left")
