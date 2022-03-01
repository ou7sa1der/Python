def sum_numbers(number_one:int,number_two:int):
    result_first_two = number_one + number_two
    return result_first_two


def subtract(number_one:int,number_two:int,number_three:int):
    final_result = sum_numbers(number_one,number_two) - number_three
    return final_result


number_one = int(input())
number_two = int(input())
number_three = int(input())

print(subtract(number_one,number_two,number_three))