list_of_strings = list(map(int, input().split(', ')))
indice = 0
even_indices = []

for number in list_of_strings:
    if number % 2 == 0:
        even_indices.append(indice)
    indice += 1
print(even_indices)


even_indices = [number for number in list_of_strings if number % 2 == 0]


# even_indices = [number for number in list_of_strings if number % 2 == 0]
# print(even_indices)