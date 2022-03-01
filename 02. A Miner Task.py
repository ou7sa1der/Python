def turn_in_dict(command):

    resource_collected = {}

    while command != 'stop':
        quantity = int(input())
        key = command
        value = quantity

        if key in resource_collected:
            resource_collected[key] += value
        else:
            resource_collected[key] = value

        command = input()

    return resource_collected


command = input()


resource_collected = turn_in_dict(command)


for key in resource_collected:
    print(f'{key} -> {resource_collected[key]}')