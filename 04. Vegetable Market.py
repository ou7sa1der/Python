vegetables_kg_price = float(input())
fruits_kg_price = float(input())
vegetables_kg = float(input())
fruits_kg = float(input())

one_euro = 1.94

vegetable_sum = vegetables_kg_price * vegetables_kg
fruits_sum = fruits_kg_price * fruits_kg

total = (vegetable_sum + fruits_sum) / one_euro

print(f'{total:.2f}')


