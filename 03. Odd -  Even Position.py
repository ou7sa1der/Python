import sys
number_count = int(input())

odd_sum = 0
odd_min_number = sys.maxsize
odd_max_number = -sys.maxsize
even_sum = 0
even_min_number = sys.maxsize
even_max_number = -sys.maxsize

number_count_two = 0

for number_count in range(number_count):
    number_count_two += 1
    number = float(input())
    if number_count_two % 2 != 0:
        odd_sum += number
        if number > odd_max_number:
            odd_max_number = number
        if number < odd_min_number:
            odd_min_number = number
    elif number_count_two % 2 == 0:
        even_sum += number
        if number > even_max_number:
            even_max_number = number
        if number < even_min_number:
            even_min_number = number

if odd_sum == 0:
    print(f"OddSum={odd_sum:.2f},")
    print(f"OddMin=No,")
    print(f"OddMax=No,")
else:
    print(f"OddSum={odd_sum:.2f},")
    print(f"OddMin={odd_min_number:.2f},")
    print(f"OddMax={odd_max_number:.2f},")
if even_sum == 0:
    print(f"EvenSum={even_sum:.2f},")
    print(f"EvenMin=No,")
    print(f"EvenMax=No")
else:
    print(f"EvenSum={even_sum:.2f},")
    print(f"EvenMin={even_min_number:.2f},")
    print(f"EvenMax={even_max_number:.2f}")