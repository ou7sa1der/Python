city = input()
sales = float(input())


if sales >= 0 and sales <= 500:
    if city == 'Sofia':
        commision = sales * 0.05
        print(f'{commision:.2f}')
    elif city == 'Varna':
        commision = sales * 0.045
        print(f'{commision:.2f}')
    elif city == 'Plovdiv':
        commision = sales * 0.055
        print(f'{commision:.2f}')
    else:
        print('error')

elif sales > 500 and sales <= 1000:
    if city == 'Sofia':
        commision = sales * 0.07
        print(f'{commision:.2f}')
    elif city == 'Varna':
        commision = sales * 0.075
        print(f'{commision:.2f}')
    elif city == 'Plovdiv':
        commision = sales * 0.08
        print(f'{commision:.2f}')
    else:
        print('error')
elif sales > 1000 and sales <= 10000:
    if city == 'Sofia':
        commision = sales * 0.08
        print(f'{commision:.2f}')
    elif city == 'Varna':
        commision = sales * 0.10
        print(f'{commision:.2f}')
    elif city == 'Plovdiv':
        commision = sales * 0.12
        print(f'{commision:.2f}')
    else:
        print('error')
elif sales > 10000:
    if city == 'Sofia':
        commision = sales * 0.12
        print(f'{commision:.2f}')
    elif city == 'Varna':
        commision = sales * 0.13
        print(f'{commision:.2f}')
    elif city == 'Plovdiv':
        commision = sales * 0.145
        print(f'{commision:.2f}')
    else:
        print('error')
else:
    print('error')