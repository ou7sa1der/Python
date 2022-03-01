countries = input().split(', ')
capitals = input().split(', ')

dict_to_print = dict(zip(countries,capitals))

for country in dict_to_print:
    print(f'{country} -> {dict_to_print[country]}')