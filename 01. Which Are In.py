first_strings = input().split(', ')
second_strings = input().split(', ')

substings_list = []

for x in first_strings:
    for y in second_strings:
        if x in y:
            substings_list.append(x)

substings_list_two = []
for unique_item in substings_list:
    if unique_item not in substings_list_two:
        substings_list_two.append(unique_item)
print(substings_list_two)