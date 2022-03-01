command = input().split(' ')

result = ''

for word in command:
    times_repeated = len(word)
    result += word * times_repeated

print(result)