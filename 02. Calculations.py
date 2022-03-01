def operation_for_the_numbers(operation:str,number_one:int,number_two:int):
    if operation == 'multiply':
        return number_one * number_two
    elif operation == 'divide':
        return number_one // number_two
    elif operation == 'add':
        return number_one + number_two
    elif operation == 'subtract':
        return number_one - number_two





operation = input()
number_one = int(input())
number_two = int(input())

print(operation_for_the_numbers(operation,number_one,number_two))