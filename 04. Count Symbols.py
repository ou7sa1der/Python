received_text = ''.join(input())

elements_dict = {}

for el in received_text:
    if el not in elements_dict:
        elements_dict[el] = 1
    else:
        elements_dict[el] += 1

sorted_elements_dict = sorted(elements_dict.items(),key=lambda x:x[0])

for el,value in sorted_elements_dict:
    print(f'{el}: {value} time/s')