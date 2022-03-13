number_of_lines = int(input())

count_rows = 0
set_even = set()
set_odd = set()

while number_of_lines:
    number_of_lines -= 1
    count_rows += 1
    name = list(input())
    sum_name = 0
    for char in name:
        sum_name += ord(char)
    result = sum_name // count_rows
    if result % 2 == 0:
        set_even.add(result)
    else:
        set_odd.add(result)

if sum(set_even) == sum(set_odd):
    set_union = set_odd.union(set_even)
    set_union_str = [str(el) for el in set_union]
    print(', '.join(set_union_str))
elif sum(set_odd) > sum(set_even):
    set_difference = set_odd.difference(set_even)
    set_difference_str = [str(el) for el in set_difference]
    print(', '.join(set_difference_str))
else:
    set_symmetric_diff = set_odd.symmetric_difference(set_even)
    set_symmetric_diff_str = [str(el) for el in set_symmetric_diff]
    print(', '.join(set_symmetric_diff_str))
