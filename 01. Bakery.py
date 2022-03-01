single_string = input().split(' ')

keys = []
values = []


def keys_values_func(single_string,keys,values):

    keys = []
    values = []

    for key in range(0, len(single_string), 2):
        keys.append(single_string[key])

    for value in range(0,len(single_string)):
        if single_string[value] not in keys:
            values.append(int(single_string[value]))


    return print(dict(zip(keys,values)))


keys_values_func(single_string,keys,values)