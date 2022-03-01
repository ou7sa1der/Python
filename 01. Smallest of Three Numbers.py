import sys
def smallest_of_them_all(num1:int,num2:int,num3:int):
    list_of_numbers = [num1,num2,num3]
    smallest = sys.maxsize
    for num in list_of_numbers:
        if num < smallest:
            smallest = num
    return smallest


number_one = int(input())
number_two = int(input())
number_three = int(input())

print(smallest_of_them_all(number_one,number_two,number_three))