single_string = input().split(' ')
searched_items = input().split(' ')


products = {}


for index in range(0,len(single_string),2):
    key = single_string[index]
    value = int(single_string[index + 1])
    products[key] = value

for searched_word in searched_items:
    if not searched_word in products:
        print(f"Sorry, we don't have {searched_word}")
    else:
        print(f"We have {products[searched_word]} of {searched_word} left")