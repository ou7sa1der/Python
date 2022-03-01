numbers_received = list(map(int,input().split(', ')))

positive = []
negative = []
even = []
odd = []

for number in numbers_received:
    if number >= 0:
        positive.append(number)
    if number < 0:
        negative.append(number)
    if number % 2 == 0:
        even.append(number)
    if number % 2 != 0:
        odd.append(number)

positive = ', '.join(map(str,positive))
negative = ', '.join(map(str,negative))
even = ', '.join(map(str,even))
odd = ', '.join(map(str,odd))
print(f'Positive: {positive}')
print(f'Negative: {negative}')
print(f'Even: {even}')
print(f'Odd: {odd}')