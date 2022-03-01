from collections import deque

command = input()
back_of_the_line = deque()

while not command == 'End':
    if not command == 'Paid':
        back_of_the_line.append(command)
    else:
        while back_of_the_line:
            print(back_of_the_line.popleft())

    command = input()

print(f"{len(back_of_the_line)} people remaining.")