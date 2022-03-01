times_typed_numbers = int(input())
even_list = []
odd_list = []
positive_list = []
negative_list = []
for x in range(1, times_typed_numbers + 1):
    numbers = int(input())
    if int(numbers) % 2 == 0:
        even_list.append(numbers)
    if numbers % 2 != 0:
        odd_list.append(numbers)
    if numbers >= 0:
        positive_list.append(numbers)
    if numbers < 0:
        negative_list.append(numbers)
command = input()
if command == 'positive':
    print(positive_list)
if command == 'negative':
    print(negative_list)
if command == 'odd':
    print(odd_list)
if command == 'even':
    print(even_list)