text = input()
count_sum = 0

for sum_in_text in text:
    if sum_in_text == "a":
        count_sum += 1
    if sum_in_text == "e":
        count_sum += 2
    if sum_in_text == "i":
        count_sum += 3
    if sum_in_text == "o":
        count_sum += 4
    if sum_in_text == "u":
        count_sum += 5
print(count_sum)