rent_for_hall = int(input())

price_for_cake = rent_for_hall * 0.2
price_for_drinks = price_for_cake - (price_for_cake * 0.45)
price_for_animation_service = rent_for_hall / 3

needed_money = rent_for_hall + price_for_cake + price_for_drinks + price_for_animation_service

print(needed_money)
