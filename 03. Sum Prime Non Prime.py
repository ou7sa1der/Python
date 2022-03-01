import sys
number = input()

prime_numbers_count = 0
non_prime_numbers_count = 0

while True:
    if number == "stop":
        break
    if int(number) < 0:
        print("Number is negative.")
        number = input()
    i = 2
    while True:
        if number == "stop":
            break
        if int(number) < 0:
            print("Number is negative.")
            number = input()
            i += 1
            continue
        if int(number) % i == 0 or int(number) == 2 or int(number) == 4:
            non_prime_numbers_count += int(number)
            number = input()
            i += 1
            continue
        else:
            prime_numbers_count += int(number)
        number = input()
        i += 1
    break
print(f"Sum of all prime numbers is: {prime_numbers_count}")
print(f"Sum of all non prime numbers is: {non_prime_numbers_count}")
