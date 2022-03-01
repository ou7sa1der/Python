array = input().split(", ")
array = [int(x) for x in array]
array.sort(key=lambda n:n==0)
print(array)
