list_of_integers_str = input().split()
numbers_to_remove = int(input())

list_of_integers = [int(x) for x in list_of_integers_str]

for i in range(1, numbers_to_remove + 1):
    list_of_integers.remove(min(list_of_integers))

print(f', '.join ([str(x) for x in list_of_integers]))