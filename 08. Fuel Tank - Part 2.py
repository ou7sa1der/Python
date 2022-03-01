fuel_type = input()
amount_of_fuel = float(input())
club_card_holder = input()

gas_price = 0.93
diesel_price = 2.33
gasoline_price = 2.22

if fuel_type == "Gas":
    if club_card_holder == "Yes":
        discount_price_for_liter = gas_price - 0.08
        price = amount_of_fuel * discount_price_for_liter
        if amount_of_fuel > 20 and amount_of_fuel <= 25:
            discount_price = price - (price * 0.08)
            print(f"{discount_price:.2f} lv.")
        elif amount_of_fuel > 25:
            discount_price_two = price - (price * 0.1)
            print(f"{discount_price_two:.2f} lv.")
        else:
            print(f"{price:.2f} lv.")
    elif club_card_holder == "No":
        price = amount_of_fuel * gas_price
        if amount_of_fuel > 20 and amount_of_fuel <= 25:
            discount_price = price - (price * 0.08)
            print(f"{discount_price:.2f} lv.")
        elif amount_of_fuel > 25:
            discount_price_two = price - (price * 0.1)
            print(f"{discount_price_two:.2f} lv.")
        else:
            print(f"{price:.2f} lv.")
elif fuel_type == "Gasoline":
    if club_card_holder == "Yes":
        discount_price_for_liter = gasoline_price - 0.18
        price = amount_of_fuel * discount_price_for_liter
        if amount_of_fuel > 20 and amount_of_fuel <= 25:
            discount_price = price - (price * 0.08)
            print(f"{discount_price:.2f} lv.")
        elif amount_of_fuel > 25:
            discount_price_two = price - (price * 0.1)
            print(f"{discount_price_two:.2f} lv.")
        else:
            print(f"{price:.2f} lv.")
    elif club_card_holder == "No":
        price = amount_of_fuel * gasoline_price
        if amount_of_fuel > 20 and amount_of_fuel <= 25:
            discount_price = price - (price * 0.08)
            print(f"{discount_price:.2f} lv.")
        elif amount_of_fuel > 25:
            discount_price_two = price - (price * 0.1)
            print(f"{discount_price_two:.2f} lv.")
        else:
            print(f"{price:.2f} lv.")
elif fuel_type == "Diesel":
    if club_card_holder == "Yes":
        discount_price_for_liter = diesel_price - 0.12
        price = amount_of_fuel * discount_price_for_liter
        if amount_of_fuel > 20 and amount_of_fuel <= 25:
            discount_price = price - (price * 0.08)
            print(f"{discount_price:.2f} lv.")
        elif amount_of_fuel > 25:
            discount_price_two = price - (price * 0.1)
            print(f"{discount_price_two:.2f} lv.")
        else:
            print(f"{price:.2f} lv.")
    elif club_card_holder == "No":
        price = amount_of_fuel * diesel_price
        if amount_of_fuel > 20 and amount_of_fuel <= 25:
            discount_price = price - (price * 0.08)
            print(f"{discount_price:.2f} lv.")
        elif amount_of_fuel > 25:
            discount_price_two = price - (price * 0.1)
            print(f"{discount_price_two:.2f} lv.")
        else:
            print(f"{price:.2f} lv.")