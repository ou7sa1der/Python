budget = float(input())
category = input()
people_in_the_group = int(input())

#    • От 1 до 4 – 75% от бюджета.
#    • От 5 до 9 – 60% от бюджета.
#    • От 10 до 24 – 50% от бюджета.
#    • От 25 до 49 – 40% от бюджета.
#    • 50 или повече – 25% от бюджета


if category == "VIP":
    ticket_price = 499.99 * people_in_the_group
    if people_in_the_group <= 4:
        transport_price = budget * 0.75
        money_left = budget - transport_price
        if ticket_price >= money_left:
            ticket = ticket_price - money_left
            print(f"Not enough money! You need {ticket:.2f} leva.")
        else:
            ticket = money_left - ticket_price
            print(f"Yes! You have {ticket:.2f} leva left.")
    elif people_in_the_group >= 5 and people_in_the_group <= 9:
        transport_price = budget * 0.60
        money_left = budget - transport_price
        if ticket_price >= money_left:
            ticket = ticket_price - money_left
            print(f"Not enough money! You need {ticket:.2f} leva.")
        else:
            ticket = money_left - ticket_price
            print(f"Yes! You have {ticket:.2f} leva left.")
    elif people_in_the_group >= 10 and people_in_the_group <= 24:
        transport_price = budget * 0.50
        money_left = budget - transport_price
        if ticket_price >= money_left:
            ticket = ticket_price - money_left
            print(f"Not enough money! You need {ticket:.2f} leva.")
        else:
            ticket = money_left - ticket_price
            print(f"Yes! You have {ticket:.2f} leva left.")
    elif people_in_the_group >= 25 and people_in_the_group <= 49:
        transport_price = budget * 0.40
        money_left = budget - transport_price
        if ticket_price >= money_left:
            ticket = ticket_price - money_left
            print(f"Not enough money! You need {ticket:.2f} leva.")
        else:
            ticket = money_left - ticket_price
            print(f"Yes! You have {ticket:.2f} leva left.")
    elif people_in_the_group > 50:
        transport_price = budget * 0.25
        money_left = budget - transport_price
        if ticket_price >= money_left:
            ticket = ticket_price - money_left
            print(f"Not enough money! You need {ticket:.2f} leva.")
        else:
            ticket = money_left - ticket_price
            print(f"Yes! You have {ticket:.2f} leva left.")
elif category == "Normal":
    ticket_price = 249.99 * people_in_the_group
    if people_in_the_group <= 4:
        transport_price = budget * 0.75
        money_left = budget - transport_price
        if ticket_price >= money_left:
            ticket = ticket_price - money_left
            print(f"Not enough money! You need {ticket:.2f} leva.")
        else:
            ticket = money_left - ticket_price
            print(f"Yes! You have {ticket:.2f} leva left.")
    elif people_in_the_group >= 5 and people_in_the_group <= 9:
        transport_price = budget * 0.60
        money_left = budget - transport_price
        if ticket_price >= money_left:
            ticket = ticket_price - money_left
            print(f"Not enough money! You need {ticket:.2f} leva.")
        else:
            ticket = money_left - ticket_price
            print(f"Yes! You have {ticket:.2f} leva left.")
    elif people_in_the_group >= 10 and people_in_the_group <= 24:
        transport_price = budget * 0.50
        money_left = budget - transport_price
        if ticket_price >= money_left:
            ticket = ticket_price - money_left
            print(f"Not enough money! You need {ticket:.2f} leva.")
        else:
            ticket = money_left - ticket_price
            print(f"Yes! You have {ticket:.2f} leva left.")
    elif people_in_the_group >= 25 and people_in_the_group <= 49:
        transport_price = budget * 0.40
        money_left = budget - transport_price
        if ticket_price >= money_left:
            ticket = ticket_price - money_left
            print(f"Not enough money! You need {ticket:.2f} leva.")
        else:
            ticket = money_left - ticket_price
            print(f"Yes! You have {ticket:.2f} leva left.")
    elif people_in_the_group > 50:
        transport_price = budget * 0.25
        money_left = budget - transport_price
        if ticket_price >= money_left:
            ticket = ticket_price - money_left
            print(f"Not enough money! You need {ticket:.2f} leva.")
        else:
            ticket = money_left - ticket_price
            print(f"Yes! You have {ticket:.2f} leva left.")