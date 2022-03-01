def product_calculation(product:str,quantity:float):
    if product == 'coffee':
        return quantity * 1.50
    elif product == 'coke':
        return quantity * 1.40
    elif product == 'water':
        return quantity * 1
    elif product == 'snacks':
        return quantity * 2


product = input()
quantity = float(input())


print(f'{product_calculation(product,quantity):.2f}')