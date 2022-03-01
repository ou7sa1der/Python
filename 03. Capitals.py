country_names = input().split(', ')
capital_cities = input().split(', ')


final = zip(country_names,capital_cities)


for key,value in final:
    print(f"{key} -> {value}")