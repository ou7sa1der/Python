budget = float(input())
season = input()
fisherman_count = int(input())

#    • Цената за наем на кораба през пролетта е  3000 лв.;
#    • Цената за наем на кораба през лятото и есента е  4200 лв.;
#    • Цената за наем на кораба през зимата е  2600 лв.

#    В зависимост от броя на групата има различна отстъпка:
#    • Ако групата е до 6 човека включително  –  отстъпка от 10%;
#    • Ако групата е от 7 до 11 човека включително  –  отстъпка от 15%;
#    • Ако групата е от 12 нагоре  –  отстъпка от 25%.

total_price = 0
#money_left = budget - total_price
#money_needed = total_price - budget

if season == "Summer":
    total_price = 4200
    if fisherman_count <= 6:
        total_price = total_price - (total_price * 0.10)
        if budget >= total_price:
            money_left = budget - total_price
            if fisherman_count % 2 == 0:
                total_price = total_price - (total_price * 0.05)
                money_left = budget - total_price
                print(f"Yes! You have {money_left:.2f} leva left.")
            else:
                print(f"Yes! You have {money_left:.2f} leva left.")
        else:
            money_needed = total_price - budget
            print(f"Not enough money! You need {money_needed:.2f} leva.")
    elif fisherman_count > 7 and fisherman_count <= 11:
        total_price = total_price - (total_price * 0.15)
        if budget >= total_price:
            money_left = budget - total_price
            if fisherman_count % 2 == 0:
                total_price = total_price - (total_price * 0.05)
                money_left = budget - total_price
                print(f"Yes! You have {money_left:.2f} leva left.")
            else:
                print(f"Yes! You have {money_left:.2f} leva left.")
        else:
            money_needed = total_price - budget
            print(f"Not enough money! You need {money_needed:.2f} leva.")
    elif fisherman_count >= 12:
        total_price = total_price - (total_price * 0.25)
        if budget >= total_price:
            money_left = budget - total_price
            if fisherman_count % 2 == 0:
                total_price = total_price - (total_price * 0.05)
                money_left = budget - total_price
                print(f"Yes! You have {money_left:.2f} leva left.")
            else:
                print(f"Yes! You have {money_left:.2f} leva left.")
        else:
            money_needed = total_price - budget
            print(f"Not enough money! You need {money_needed:.2f} leva.")
elif season == "Autumn":
    total_price = 4200
    if fisherman_count <= 6:
        total_price = total_price - (total_price * 0.10)
        if budget >= total_price:
            money_left = budget - total_price
            print(f"Yes! You have {money_left:.2f} leva left.")
        else:
            money_needed = total_price - budget
            print(f"Not enough money! You need {money_needed:.2f} leva.")
    elif fisherman_count > 7 and fisherman_count <= 11:
        total_price = total_price - (total_price * 0.15)
        if budget >= total_price:
            money_left = budget - total_price
            print(f"Yes! You have {money_left:.2f} leva left.")
        else:
            money_needed = total_price - budget
            print(f"Not enough money! You need {money_needed:.2f} leva.")
    elif fisherman_count >= 12:
        total_price = total_price - (total_price * 0.25)
        if budget >= total_price:
            money_left = budget - total_price
            print(f"Yes! You have {money_left:.2f} leva left.")
        else:
            money_needed = total_price - budget
            print(f"Not enough money! You need {money_needed:.2f} leva.")
elif season == "Spring":
    total_price = 3000
    if fisherman_count <= 6:
        total_price = total_price - (total_price * 0.10)
        if budget >= total_price:
            money_left = budget - total_price
            if fisherman_count % 2 == 0:
                total_price = total_price - (total_price * 0.05)
                money_left = budget - total_price
                print(f"Yes! You have {money_left:.2f} leva left.")
            else:
                print(f"Yes! You have {money_left:.2f} leva left.")
        else:
            money_needed = total_price - budget
            print(f"Not enough money! You need {money_needed:.2f} leva.")
    elif fisherman_count > 7 and fisherman_count <= 11:
        total_price = total_price - (total_price * 0.15)
        if budget >= total_price:
            money_left = budget - total_price
            if fisherman_count % 2 == 0:
                total_price = total_price - (total_price * 0.05)
                money_left = budget - total_price
                print(f"Yes! You have {money_left:.2f} leva left.")
            else:
                print(f"Yes! You have {money_left:.2f} leva left.")
        else:
            money_needed = total_price - budget
            print(f"Not enough money! You need {money_needed:.2f} leva.")
    elif fisherman_count >= 12:
        total_price = total_price - (total_price * 0.25)
        if budget >= total_price:
            money_left = budget - total_price
            if fisherman_count % 2 == 0:
                total_price = total_price - (total_price * 0.05)
                money_left = budget - total_price
                print(f"Yes! You have {money_left:.2f} leva left.")
            else:
                print(f"Yes! You have {money_left:.2f} leva left.")
        else:
            money_needed = total_price - budget
            print(f"Not enough money! You need {money_needed:.2f} leva.")
elif season == "Winter":
    total_price = 2600
    if fisherman_count <= 6:
        total_price = total_price - (total_price * 0.10)
        if budget >= total_price:
            money_left = budget - total_price
            if fisherman_count % 2 == 0:
                total_price = total_price - (total_price * 0.05)
                money_left = budget - total_price
                print(f"Yes! You have {money_left:.2f} leva left.")
            else:
                print(f"Yes! You have {money_left:.2f} leva left.")
        else:
            money_needed = total_price - budget
            print(f"Not enough money! You need {money_needed:.2f} leva.")
    elif fisherman_count > 7 and fisherman_count <= 11:
        total_price = total_price - (total_price * 0.15)
        if budget >= total_price:
            money_left = budget - total_price
            if fisherman_count % 2 == 0:
                total_price = total_price - (total_price * 0.05)
                money_left = budget - total_price
                print(f"Yes! You have {money_left:.2f} leva left.")
            else:
                print(f"Yes! You have {money_left:.2f} leva left.")
        else:
            money_needed = total_price - budget
            print(f"Not enough money! You need {money_needed:.2f} leva.")
    elif fisherman_count >= 12:
        total_price = total_price - (total_price * 0.25)
        if budget >= total_price:
            money_left = budget - total_price
            if fisherman_count % 2 == 0:
                total_price = total_price - (total_price * 0.05)
                money_left = budget - total_price
                print(f"Yes! You have {money_left:.2f} leva left.")
            else:
                print(f"Yes! You have {money_left:.2f} leva left.")
        else:
            money_needed = total_price - budget
            print(f"Not enough money! You need {money_needed:.2f} leva.")