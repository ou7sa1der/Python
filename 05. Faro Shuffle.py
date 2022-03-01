list_for_shuffle = input().split()
times_shuffling = int(input())

half_list = len(list_for_shuffle) // 2

for x in range(times_shuffling):
    left_side = list_for_shuffle[0:half_list]
    right_side = list_for_shuffle[half_list:]

    faro_cards = []

    for i in range(len(left_side)):
        faro_cards.append(left_side[i])
        faro_cards.append(right_side[i])

    list_for_shuffle = faro_cards
print(list_for_shuffle)