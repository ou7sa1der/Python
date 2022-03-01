type_flower = input()
count_flower = int(input())
budget = int(input())
total_price = 0

#"Roses", "Dahlias", "Tulips", "Narcissus" или "Gladiolus";

if type_flower == "Roses":
    if count_flower > 80:
        total_price = (count_flower * 5) * 0.9
    else:
        total_price = count_flower * 5
elif type_flower == "Dahlias":
    if count_flower > 90:
        total_price = (count_flower * 3.8) * 0.85
    else:
        total_price = count_flower * 3.8
elif type_flower == "Tulips":
    if count_flower > 80:
        total_price = (count_flower * 2.8) * 0.85
    else:
        total_price = count_flower * 2.8
elif type_flower == "Narcissus":
    if count_flower < 120:
        total_price = (count_flower * 3) + (count_flower * 3) * 0.15
    else:
        total_price = count_flower * 3
elif type_flower == "Gladiolus":
    if count_flower < 80:
        total_price = (count_flower * 2.5) + (count_flower * 2.5) * 0.2
    else:
        total_price = count_flower * 2.5

money_left = budget - total_price
money_needed = total_price - budget

if budget >= total_price:
    print(f"Hey, you have a great garden with {count_flower} {type_flower} and {money_left:.2f} leva left.")
else:
    print(f"Not enough money, you need {money_needed:.2f} leva more.")