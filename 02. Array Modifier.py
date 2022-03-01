array_with_integers = list(map(int, input().split(' ')))

new_list = []

while True:
    commands = input().split(' ')

    if commands[0] == 'end':
        break
    elif commands [0] == 'swap':
        index_one = int(commands[1])
        index_two = int(commands[2])
        array_with_integers[index_one],array_with_integers[index_two] = array_with_integers[index_two],array_with_integers[index_one]
    elif commands [0] == 'multiply':
        index_one = int(commands[1])
        index_two = int(commands[2])
        array_with_integers[index_one] = array_with_integers[index_one] * array_with_integers[index_two]
    elif commands [0] == 'decrease':
        new_list = [element - 1 for element in array_with_integers]
        array_with_integers = new_list
print(', '.join(map(str, array_with_integers)))