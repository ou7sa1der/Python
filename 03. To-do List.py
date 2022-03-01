received_string_two = input().split('-')
empty_string = [0] * 10

while True:
    if 'End' in received_string_two:
        break
    priority_level = int(received_string_two[0])
    note = received_string_two[1]
    empty_string.pop(priority_level)
    empty_string.insert(priority_level, note)
    received_string_two = input().split('-')
result = [element for element in empty_string if element != 0]
print(result)