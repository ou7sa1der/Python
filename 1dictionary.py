input_string = input()

count_dict = {}

for chr in input_string:
    if chr == ' ':
        continue
    elif chr in count_dict:
        count_dict[chr] += 1
    else:
        count_dict[chr] = 1

for key in count_dict:
    print(f"{key} -> {count_dict[key]}")