product = input()
day = input()
quantity = float(input())


if day == 'Monday' or day == 'Tuesday' or day == 'Wednesday' or day == 'Thursday' or day == 'Friday':
    if product == 'banana':
        sum = quantity * 2.5
        print(f'{sum:.2f}')
    elif product == 'apple':
        sum = quantity * 1.2
        print(f'{sum:.2f}')
    elif product == 'orange':
        sum = quantity * 0.85
        print(f'{sum:.2f}')
    elif product == 'grapefruit':
        sum = quantity * 1.45
        print(f'{sum:.2f}')
    elif product == 'kiwi':
        sum = quantity * 2.7
        print(f'{sum:.2f}')
    elif product == 'pineapple':
        sum = quantity * 5.5
        print(f'{sum:.2f}')
    elif product == 'grapes':
        sum = quantity * 3.85
        print(f'{sum:.2f}')
    else:
        print('error')
elif day == 'Saturday' or day == 'Sunday':
    if product == 'banana':
        sum = quantity * 2.7
        print(f'{sum:.2f}')
    elif product == 'apple':
        sum = quantity * 1.25
        print(f'{sum:.2f}')
    elif product == 'orange':
        sum = quantity * 0.90
        print(f'{sum:.2f}')
    elif product == 'grapefruit':
        sum = quantity * 1.6
        print(f'{sum:.2f}')
    elif product == 'kiwi':
        sum = quantity * 3
        print(f'{sum:.2f}')
    elif product == 'pineapple':
        sum = quantity * 5.6
        print(f'{sum:.2f}')
    elif product == 'grapes':
        sum = quantity * 4.2
        print(f'{sum:.2f}')
    else:
        print('error')
else:
    print('error')

