import re

str = input()
#search using regex
while str:
    number = re.findall('[0-9]+', str)
    if number == []:
        pass
    else:
        print(*number, end=' ')
    str = input()