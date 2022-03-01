command = input()

dict_to_print = {}

while command != 'stop':
    resource = command
    quantity = int(input())
    if resource in dict_to_print:
        dict_to_print[resource] += quantity
    else:
        dict_to_print[resource] = quantity
    command = input()

for x in dict_to_print:
    print(f'{x} -> {dict_to_print[x]}')