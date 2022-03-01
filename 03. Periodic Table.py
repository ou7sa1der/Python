count_lines = int(input())
counter_of_lines = 0
unique_set_of_chemical_el = set()

while count_lines > counter_of_lines:
    chemical_el = input().split()
    counter_of_lines += 1
    for el in chemical_el:
        unique_set_of_chemical_el.add(el)

for unique_el in unique_set_of_chemical_el:
    print(unique_el)