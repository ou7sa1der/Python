num_rows = int(input())
k = 1
a = 1
for i in range(0, num_rows):
    for j in range(0, k):
        print("*", end='')
    k = k + 1
    print()
for i in range (num_rows, 0, -1):
    for j in range(0, i -1):
        print("*", end='')
    a = a - 1
    print()