command = input()


products = {}


while command != 'statistics':
    kvp = command.split(': ')
    key = kvp[0]
    value = int(kvp[1])
    if key in products:
        products[key] += value
    else:
        products[key] = value
    command = input()

print("Products in stock:")
for product in products:
    print(f"- {product}: {products[product]}")
print(f'Total Products: {len(products)}')
print(f'Total Quantity: {sum(products.values())}')