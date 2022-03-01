number = int(input())
total_sum = 0
typed_number = int(input())
while total_sum < number:
    total_sum += typed_number
    if total_sum >= number:
        print(total_sum)
        break
    typed_number = int(input())
else:
    print(total_sum)