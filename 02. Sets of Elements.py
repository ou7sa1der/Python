first_set,second_set = input().split(' ')

first_set_lenght = int(first_set)
second_set_lenght = int(second_set)
count_number = 0
first_set_data = set()
second_set_data = set()

while first_set_lenght + second_set_lenght > count_number:
    element = int(input())
    count_number += 1
    if count_number <= first_set_lenght:
        first_set_data.add(element)
    else:
        second_set_data.add(element)

for el in first_set_data.intersection(second_set_data):
    print(el)
