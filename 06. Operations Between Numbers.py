number_1 = int(input())
number_2 = int(input())
operator = input()

adding = number_1 + number_2
subtraction = number_1 - number_2
multiplication = number_1 * number_2


if operator == "+" or operator == "-" or operator == "*":
    if operator == "+":
        if abs(adding) % 2 == 0:
            print(f"{number_1} {operator} {number_2} = {abs(adding)} - even")
        else:
            print(f"{number_1} {operator} {number_2} = {abs(adding)} - odd")
    elif operator == "-":
        if abs(subtraction) % 2 == 0:
            print(f"{number_1} {operator} {number_2} = {abs(subtraction)} - even")
        else:
            print(f"{number_1} {operator} {number_2} = {abs(subtraction)} - odd")
    elif operator == "*":
        if abs(multiplication) % 2 == 0:
            print(f"{number_1} {operator} {number_2} = {abs(multiplication)} - even")
        else:
            print(f"{number_1} {operator} {number_2} = {abs(multiplication)} - odd")
elif operator == "/" and number_2 != 0:
    divison = number_1 / number_2
    print(f"{number_1} / {number_2} = {abs(divison):.2f}")
elif operator == "%" and number_2 != 0:
    modul_division = number_1 % number_2
    print(f"{number_1} % {number_2} = {abs(modul_division)}")
else:
    print(f"Cannot divide {number_1} by zero")