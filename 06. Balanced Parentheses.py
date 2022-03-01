# three types of parentheses: (), {}, and []
from collections import deque

def going_through_closing_el(string_brackets):
    closing_brackets = deque()

    for bracket in range(len(string_brackets)):
        if string_brackets[bracket] == ')':
            closing_brackets.append(string_brackets[bracket])

        elif string_brackets[bracket] == '}':
            closing_brackets.append(string_brackets[bracket])

        elif string_brackets[bracket] == ']':
            closing_brackets.append(string_brackets[bracket])

    return closing_brackets


def going_through_opening_el(string_brackets):
    search_brackets = []

    for bracket in range(len(string_brackets)):
        if string_brackets[bracket] == '(':
            search_brackets.append(string_brackets[bracket])

        elif string_brackets[bracket] == '{':
            search_brackets.append(string_brackets[bracket])

        elif string_brackets[bracket] == '[':
            search_brackets.append(string_brackets[bracket])
    return search_brackets


def turning_into_list(string_brackets):
    string_brackets_list = []
    for el in range(len(string_brackets)):
        string_brackets_list.append(string_brackets[el])
    return string_brackets_list


# matching_brackets = ['(', ')', '{', '}', '[', ']']
string_brackets = input()
opening_brackets = going_through_opening_el(string_brackets)
closing_brackets = going_through_closing_el(string_brackets)
string_brackets_list = turning_into_list(string_brackets)
flag = False
if len(opening_brackets) != len(closing_brackets):
    print('NO')
    exit()

match_brackets = []
for el in opening_brackets:
    if el == '{':

        if '}' == closing_brackets[-1]:
            match_brackets.append('{')
            match_brackets.append('}')
            closing_brackets.pop()
            flag = True
        elif '}' == closing_brackets[0] and not flag:
            match_brackets.append('{')
            match_brackets.append('}')
            closing_brackets.popleft()
        else:
            break
    elif el == '[':

        if ']' == closing_brackets[-1]:
            match_brackets.append('[')
            match_brackets.append(']')
            closing_brackets.pop()
            flag = True
        elif ']' == closing_brackets[0]  and not flag:
            match_brackets.append('[')
            match_brackets.append(']')
            closing_brackets.popleft()
        else:
            break

    elif el == '(':

        if ')' == closing_brackets[-1]:
            match_brackets.append('(')
            match_brackets.append(')')
            closing_brackets.pop()
            flag = True
        elif ')' == closing_brackets[0] and not flag:
            match_brackets.append('(')
            match_brackets.append(')')
            closing_brackets.popleft()
        else:
            break

if len(string_brackets_list) == len(match_brackets):
    print('YES')
else:
    print('NO')
