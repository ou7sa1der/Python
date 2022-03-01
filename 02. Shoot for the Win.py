sequence_integers = list(map(int,input().split(' ')))

shot_targets = 0
while True:
    command = input()
    if command == 'End':
        break
    index_of_target = int(command)
    if index_of_target >= len(sequence_integers):
        continue
    old_value = sequence_integers[index_of_target]
    if sequence_integers[index_of_target] != -1:
        sequence_integers[index_of_target] = -1
        for index in range (0,len(sequence_integers)):
            if sequence_integers[index] == -1:
                continue
            if sequence_integers[index] > old_value:
                sequence_integers[index] -= old_value
            else:
                sequence_integers[index] += old_value
for index in sequence_integers:
    if index == -1:
        shot_targets += 1

print(f'Shot targets: {shot_targets} -> {" ".join(map(str,sequence_integers))}')