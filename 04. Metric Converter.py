number = float(input())
unit = input()
unit_to = input()

if unit == "mm":
    # ot mm vuv cm
    if unit_to == "cm":
        number_to = number / 10
        print(f'{number_to:.3f}')
#ot mm vuv m
    elif unit_to == "m":
        number_to = number / 1000
        print(f'{number_to:.3f}')
elif unit == "cm":
    # ot cm vuv mm
    if unit_to == "mm":
        number_to = number * 10
        print(f'{number_to:.3f}')
#ot cm vuv m
    elif unit_to == "m":
        number_to = number / 100
        print(f'{number_to:.3f}')
elif unit == "m":
    # ot m vuv mm
    if unit_to == "mm":
        number_to = number / 0.001
        print(f'{number_to:.3f}')
#ot m vuv cm
    elif unit_to == "cm":
        number_to = number / 0.01
        print(f'{number_to:.3f}')