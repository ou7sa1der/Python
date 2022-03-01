def int_func(first_line_input,number_or_string):
    return int(number_or_string) * 2


def real_func(first_line_input,number_or_string):
    result = float(number_or_string) * 1.5
    return f'{result:.2f}'


def string_func(first_line_input,number_or_string):
    number_or_string = number_or_string.split(' ')
    number_or_string.insert(0,'$')
    number_or_string.append('$')
    return ''.join(number_or_string)

first_line_input = input()
number_or_string = input()

if first_line_input == 'int':
    print(int_func(first_line_input,number_or_string))


elif first_line_input == 'real':
    print(real_func(first_line_input,number_or_string))


elif first_line_input == 'string':
    print(string_func(first_line_input,number_or_string))