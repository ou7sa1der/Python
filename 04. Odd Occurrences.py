single_string = input().split(' ')


def dictionary_func(single_string,commands_count):
    for command in single_string:
        key = command.lower()
        if key in commands_count:
            commands_count[key] += 1
        else:
            commands_count[key] = 1
    return commands_count


def odd_func(commands_count,odd_commands):
    for key in commands_count:
        if commands_count[key] % 2 != 0:
            odd_commands.append(key)
    return ' '.join(odd_commands)


commands_count = {}
odd_commands = []

dictionary_func(single_string,commands_count)
print(odd_func(commands_count,odd_commands))