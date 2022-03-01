sequence_of_integers  = list(map(int, input().split(' ')))
greater_than_average_list = []

greater_than_average_list = []
average_number = sum(sequence_of_integers) // len(sequence_of_integers)

greater_than_average_list = [number for number in sequence_of_integers if number > average_number]
greater_than_average_list.sort(reverse=True)

if len(greater_than_average_list) == 0:
    print('No')
else:
    print(" ".join(map(str,greater_than_average_list[0:5])))