def calculations_and_creating_dictionary(products_received):

    products_dictionary = {}

    while products_received != 'buy':
        products = products_received.split(' ')
        product = products[0]
        price = float(products[1])
        quantity = int(products[2])
        if product in products_dictionary:
            products_dictionary[product][1] += quantity
            if price != products_dictionary[product][0]:
                products_dictionary[product][0] = price

        else:
            products_dictionary[product] = [price,quantity]
        products_received = input()

    for key in products_dictionary:
        products_dictionary[key] = products_dictionary[key][0] * products_dictionary[key][1]

    return products_dictionary

products_received = input()

products_dictionary = calculations_and_creating_dictionary(products_received)
for key,value in products_dictionary.items():
    print(f'{key} -> {value:.2f}')