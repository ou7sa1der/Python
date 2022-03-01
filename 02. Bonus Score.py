number = int(input())

#ako e do 100 vkliuchitelno
if number <= 100:
    bonus = 5
    if number % 2 == 0:
        bonus += 1
    elif number % 10 == 5:
        bonus += 2
    number_with_bonus = number + bonus
    print(f'{bonus}')
    print(f'{number_with_bonus}')
#ako e po golqmo ot 100
if number > 100 and number <= 1000:
    bonus = number * 0.2
    if number % 2 == 0:
        bonus += 1
    elif number % 10 == 5:
        bonus += 2
    number_with_bonus = number + bonus
    print(f'{bonus}')
    print(f'{number_with_bonus}')
#ako e po golqmo ot 1000
if number > 1000:
    bonus = number * 0.1
    if number % 2 == 0:
        bonus += 1
    elif number % 10 == 5:
        bonus += 2
    number_with_bonus = number + bonus
    print(f'{bonus}')
    print(f'{number_with_bonus}')
