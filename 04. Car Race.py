list_of_integers = input().split()
list_of_integers = [int(x) for x in list_of_integers]

middle = len(list_of_integers) // 2
sum_right = 0
sum_left = 0

left_side = list_of_integers[0:middle]
right_side = list_of_integers[middle:]
right_side.remove(right_side[0])
for x in range(1, 1 + 1):
    for x in left_side:
        sum_left += x
        if x == 0:
            sum_left *= 0.80
    for i in right_side[::-1]:
        sum_right += i
        if i == 0:
            sum_right *= 0.80

if sum_left < sum_right:
    print(f"The winner is left with total time: {sum_left:.1f}")
else:
    print(f"The winner is right with total time: {sum_right:.1f}")