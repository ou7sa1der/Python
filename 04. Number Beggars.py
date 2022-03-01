taken_list = input().split(', ')
beggars = int(input())

sums_of_each_beggar = []
start_index = 0

for beggar in range(1, beggars + 1):
    current_sum = 0
    for sum in range(start_index, len(taken_list), beggars):
        current_sum += int(taken_list[sum])
    sums_of_each_beggar.append(current_sum)
    start_index += 1
print(sums_of_each_beggar)
