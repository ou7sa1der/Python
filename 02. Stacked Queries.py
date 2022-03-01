# •	'1 {number}' – push the number (integer) into the stack
# •	'2' – delete the number at the top of the stack
# •	'3' – print the maximum number in the stack
# •	'4' – print the minimum number in the stack


def stack_for_print_func(stack):
    stack_for_print = []

    for num in range(len(stack)):
        num_for_pop = str(stack.pop())
        stack_for_print.append(num_for_pop)

    return ", ".join(stack_for_print)


number_lines = int(input())
stack = []

checked_lines = 0
while number_lines > checked_lines:
    query = input().split()
    command = query[0]
    if command == '1':
        number = int(query[1])
        stack.append(number)
    elif command == '2' and stack:
        number_to_pop = stack.pop()
    elif command == '3' and stack:
        print(max(stack))
    elif command == '4' and stack:
        print(min(stack))
    checked_lines += 1

print(stack_for_print_func(stack))
