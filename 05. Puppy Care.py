food_bought_kg = int(input())

food_bought_grams = food_bought_kg * 1000
total_food = 0
command = input()

while command != "Adopted":
    total_food += int(command)
    command = input()

if total_food <= food_bought_grams:
    food_left = food_bought_grams - total_food
    print(f"Food is enough! Leftovers: {food_left} grams.")
elif total_food > food_bought_grams:
    food_needed = total_food - food_bought_grams
    print(f"Food is not enough. You need {food_needed} grams more.")