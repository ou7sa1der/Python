budget = float(input())
extras = int(input())
price_for_extras_dress = float(input())

decor_price = budget * 0.1
dress_price = extras * price_for_extras_dress

if extras > 150:
    dress_price_discount = dress_price - (dress_price * 0.1)
    total_movie_price = decor_price + dress_price_discount
    if total_movie_price <= budget:
        total_sum = budget - total_movie_price
        print("Action!")
        print(f"Wingard starts filming with {total_sum:.2f} leva left.")
    # Ако  парите за декора и дрехите са повече от бюджета:
    elif total_movie_price > budget:
        total_sum = total_movie_price - budget
        print("Not enough money!")
        print(f"Wingard needs {total_sum:.2f} leva more.")
elif extras <= 150:
    dress_price = extras * price_for_extras_dress
    total_movie_price = decor_price + dress_price
#Ако парите за декора и дрехите са по малко или равни на бюджета:
    if total_movie_price <= budget:
        total_sum = budget - total_movie_price
        print("Action!")
        print(f"Wingard starts filming with {total_sum:.2f} leva left.")
# Ако  парите за декора и дрехите са повече от бюджета:
    elif total_movie_price > budget:
        total_sum = total_movie_price - budget
        print("Not enough money!")
        print(f"Wingard needs {total_sum:.2f} leva more.")