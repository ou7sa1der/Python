import sys
divisor = int(input())
bound = int(input())

#N is divisible by divisor
#N is less than or equal to bound
#N is greater than 0.
n = 0
n_largest = -sys.maxsize

while divisor and bound >= 0 and n <= bound:
    if n == 0:
        n = divisor + 1
    if n % divisor == 0 and n <= bound and n > 0:
        n_largest = n
        if n > n_largest:
            break
    n += 1
print(n_largest)