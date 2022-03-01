sequence_of_targets = list(map(int, input().split(' ')))

while True:
    command = input().split(' ')
    if 'End' in command:
        print('|'.join(map(str, sequence_of_targets)))
        break


    elif 'Shoot' in command:
        index = int(command[1])
        power = int(command[2])
        if 0 <= index < len(sequence_of_targets):
            sequence_of_targets[index] -= power
            if sequence_of_targets[index] <= 0:  # note if not 100points/ if navutre
                sequence_of_targets.pop(index)



    elif 'Add' in command:
        index = int(command[1])
        value = int(command[2])
        if 0 <= index < len(sequence_of_targets):
            sequence_of_targets.insert(index, value)
        else:
            print("Invalid placement!")


    elif "Strike" in command:
        index = int(command[1])
        radius = int(command[2])

        start = index - radius
        end = index + radius

        if start >= 0 and end < len(sequence_of_targets):
            del sequence_of_targets[start: end + 1]
        else:
            print("Strike missed!")
