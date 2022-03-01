from math import ceil,floor
days_count = int(input())
left_food_kg = int(input())
dog_food_kg = float(input())
cat_food_kg = float(input())
turtle_grams = float(input())

needed_dog_food = days_count * dog_food_kg
needed_cat_food = days_count * cat_food_kg
needed_turtle_food_kg = (days_count * turtle_grams) / 1000
total_food = needed_dog_food + needed_cat_food + needed_turtle_food_kg

#Ако оставената храна Е достатъчна:
if left_food_kg >= total_food:
    left_over_food = left_food_kg - total_food
    print(f"{floor(left_over_food)} kilos of food left.")
#Ако оставената храна НЕ Е достатъчна
else:
    needed_food = total_food - left_food_kg
    print(f"{ceil(needed_food)} more kilos of food are needed.")