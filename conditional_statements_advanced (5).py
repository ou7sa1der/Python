product = input()

city = input()

quantity = float(input())

if city == 'Sofia':
    if product == 'coffee':
        money = quantity * 0.5
        print(money)
    elif product == 'water':
        money = quantity * 0.8
        print(money)
    elif product == 'beer':
        money = quantity * 1.20
        print(money)
    elif product == 'sweets':
        money = quantity * 1.45
        print(money)
    elif product == 'peanuts':
        money = quantity * 1.60
        print(money)

elif city == 'Plovdiv':
    if product == 'coffee':
        money = quantity * 0.4
        print(money)
    elif product == 'water':
        money = quantity * 0.7
        print(money)
    elif product == 'beer':
        money = quantity * 1.15
        print(money)
    elif product == 'sweets':
        money = quantity * 1.3
        print(money)
    elif product == 'peanuts':
        money = quantity * 1.5
        print(money)

elif city == 'Varna':
    if product == 'coffee':
        money = quantity * 0.45
        print(money)
    elif product == 'water':
        money = quantity * 0.7
        print(money)
    elif product == 'beer':
        money = quantity * 1.1
        print(money)
    elif product == 'sweets':
        money = quantity * 1.35
        print(money)
    elif product == 'peanuts':
        money = quantity * 1.55
        print(money)
