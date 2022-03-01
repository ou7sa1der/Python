number_of_electrons = int(input())

filled_shells = []
for n in range(1, number_of_electrons + 1):
    max_number_electrons = 2 * pow(n,2)
    if number_of_electrons <= 0:
        break
    if max_number_electrons > number_of_electrons:
        filled_shells.append(number_of_electrons)
        break
    filled_shells.append(max_number_electrons)
    number_of_electrons -= max_number_electrons

print(filled_shells)