jobs_to_do = input()
coffee_count = 0

action_to_upper = ['CODING', 'MOVIE', 'DOG', 'CAT']
action_to_lower = ['coding', 'movie', 'dog', 'cat']

while jobs_to_do != 'END':
    if jobs_to_do in action_to_lower:
        coffee_count += 1
    elif jobs_to_do in action_to_upper:
        coffee_count += 2
    jobs_to_do = input()
    if jobs_to_do == 'END':
        if coffee_count > 5:
            print('You need extra sleep')
        else:
            print(coffee_count)

# coding
# dog
# cat
# movie
# Other events can be present and it will be represent by arbitrary string, just ignore this one.
