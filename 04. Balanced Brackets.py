lines_received = int(input())

# • Opening bracket – “(“,
# • Closing bracket – “)”
last_string = ''
open_count = 0
close_count = 0

for lines in range(1, lines_received + 1):
    string = input()
    if string == '(' and last_string == '(':
        # print('UNBALANCED')
        break
    if string == '(':
        open_count += 1
    if string == ')':
        close_count += 1
    last_string = string

if open_count == close_count:
    print('BALANCED')
else:
    print('UNBALANCED')