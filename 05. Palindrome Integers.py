def palindrome_or_not(list_of_numbers):
    for number in list_of_numbers:
        if int(number) == int(number[::-1]):
            print('True')
        else:
            print('False')


list_of_numbers = list(map(str, input().split(', ')))
palindrome_or_not(list_of_numbers)