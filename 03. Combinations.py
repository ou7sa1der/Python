number = int(input())
valid_action = 0

for x1 in range (number+1):
    for x2 in range(number + 1):
        for x3 in range(number + 1):
            combination = x1 + x2 + x3
            if combination == number:
                valid_action += 1
print(valid_action)