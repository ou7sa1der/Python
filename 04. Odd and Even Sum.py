def sum_of_odd_digits(number):
    odd = []
    for i in number:
        if int(i) % 2 != 0:
            odd.append(i)
    odd = list(map(int,odd))
    return sum(odd)


def sum_of_even_digits(number):
    even = []
    for i in number:
        if int(i) % 2 == 0:
            even.append(i)
    even = list(map(int,even))
    return sum(even)


number = input()

print(f"Odd sum = {sum_of_odd_digits(number)}, Even sum = {sum_of_even_digits(number)}")