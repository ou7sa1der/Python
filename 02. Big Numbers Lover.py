from functools import cmp_to_key

# initializing the list
numbers = input().split(" ")

def get_key(first, second):
   if str(first) + str(second) > str(second) + str(first):
      return -1
   return 1

# getting the result
result = sorted(numbers, key=cmp_to_key(get_key))

# joining the result
result = "".join(str(integer) for integer in result)

# printing the result
print(int(result))