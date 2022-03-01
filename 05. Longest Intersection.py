number_of_intersections = int(input())

first_set_of_el = set()
second_set_of_el = set()
longest_range = set()

while number_of_intersections:
    elements = input().split('-')
    first_range = elements[0]
    second_range = elements[1]

    splited_first_range = first_range.split(',')
    from_ = int(splited_first_range[0])
    to_ = int(splited_first_range[1])

    splited_second_range = second_range.split(',')
    second_from_ = int(splited_second_range[0])
    second_to_ = int(splited_second_range[1])

    for x in range(from_,to_ + 1):
        first_set_of_el.add(x)

    for y in range(second_from_,second_to_ + 1):
        second_set_of_el.add(y)

    cross_over = first_set_of_el.intersection(second_set_of_el)
    first_set_of_el = set()
    second_set_of_el = set()

    if len(longest_range) < len(cross_over):
        longest_range = cross_over

    number_of_intersections -= 1

print(f"Longest intersection is {list(longest_range)} with length {len(longest_range)}")

