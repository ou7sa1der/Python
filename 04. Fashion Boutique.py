sequence_of_integers = input().split()
capacity_of_a_rack = int(input())
current_rack = 0
racks_used = 0

while sequence_of_integers:
    clothes = int(sequence_of_integers.pop())
    current_rack += clothes
    if current_rack == capacity_of_a_rack:
        racks_used += 1
        current_rack = 0
    elif current_rack > capacity_of_a_rack:
        sequence_of_integers.append(str(clothes))
        racks_used += 1
        current_rack = 0

if current_rack > 0:
    print(racks_used + 1)
else:
    print(racks_used)