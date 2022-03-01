number = int(input())
word = input()
unfiltered_list = []
filtered_list = []
for x in range(1, number + 1):
    random_strings = input()
    unfiltered_list.append(random_strings)
    if word in random_strings:
        filtered_list.append(random_strings)
print(unfiltered_list)
print(filtered_list)