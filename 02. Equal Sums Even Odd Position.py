number_one = int(input())
number_two = int(input())

equal_sum = 0
odd_sum = 0

#moeto reshenie
for digits in range(number_one, number_two):
    digits = str(digits)
    odd_sum = int(digits[0]) + int(digits[2]) + int(digits[4])
    equal_sum = int(digits[1]) + int(digits[3]) + int(digits[5])
    if odd_sum == equal_sum:
        print(int(digits), end=" ")
    else:
        odd_sum = 0
        equal_sum = 0

#ot exercise
#number_one = int(input())
#number_two = int(input())
#for number in range(number_one,number_two):
#    number_to_str = str(number)
#    even_sum = 0
#    odd_sum = 0
#    for index, digit in enumerate(number_to_str):
#        if index % 2 == 0:
#            even_sum += int(digit)
#        else:
#            odd_sum += int(digit)
#    if even_sum == odd_sum:
#        print(number, end=" ")