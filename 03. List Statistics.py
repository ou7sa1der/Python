number = int(input())
positive_list = []
negative_list = []
sum_negatives = 0
for x in range(1, number + 1):
    numbers = int(input())
    if numbers >= 0:
        positive_list.append(numbers)
    else:
        negative_list.append(numbers)
        sum_negatives += numbers
print(positive_list)
print(negative_list)
print(f"Count of positives: {len(positive_list)}. Sum of negatives: {sum_negatives}")