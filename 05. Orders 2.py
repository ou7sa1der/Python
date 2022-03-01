def action_with_quantity(name,price,quantity,dict_to_print):

    if not name in dict_to_print:
        dict_to_print[name] = [price,quantity]
    else:
        dict_to_print[name][1] += quantity
        if price != dict_to_print[name][0]:
            dict_to_print[name][0] = price

    return dict_to_print




command = input()

dict_to_print = {}

#{name} {price} {quantity}
while command != 'buy':
    command = command.split(' ')
    name = command[0]
    price = float(command[1])
    quantity = int(command[2])


    action_with_quantity(name,price,quantity,dict_to_print)


    command = input()

for product in dict_to_print:
    dict_to_print[product] = dict_to_print[product][0] * dict_to_print[product][1]

for product in dict_to_print:
    print(f"{product} -> {dict_to_print[product]:.2f}")