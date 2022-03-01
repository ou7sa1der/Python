def is_number_valid(number):
    if number > 0 and number <= 100 and number % 10 != 0:
        is_number_valid = True
#checking is number valid

def loading_bar(number):
    loading_bar_list = []

    counter = number // 10
    #if counter is below zero to append '.' else to append n times from the number
    for x in range(1, 10 + 1):
        counter -= x
        if counter >= 0:
            loading_bar_list.append('%')
        else:
            loading_bar_list.append('.')
        counter = number // 10
    return ''.join(loading_bar_list)


number = int(input())


if is_number_valid(number):
    exit()
elif number == 100:
    print(f'{number}% Complete!')
    print(f'[{loading_bar(number)}]')
else:
    print(f'{number}% [{loading_bar(number)}]')
    print('Still loading...')