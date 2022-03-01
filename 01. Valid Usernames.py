usernames = input().split(', ')

result = ''

for user in usernames:
    if 3 <= len(user) <= 16:
        for char in user:
            if char.isalpha() \
            or char.isdigit() \
            or '-' in char \
            or '_' in char:
                result += char
            else:
                continue

        if user == result:
            print(user)
        result = ''