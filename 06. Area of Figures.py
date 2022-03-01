from math import pi

figure = (input())

#kvadrat S = a * a
if figure == "square":
    a = float(input())
    S = a * a
    print(f'{S:.3f}')
#pravougulnik S = a * b
elif figure == "rectangle":
    a = float(input())
    b = float(input())
    S = a * b
    print(f'{S:.3f}')
#krug S = pi * r * r
elif figure == "circle":
    r = float(input())
    S = pi * r * r
    print(f'{S:.3f}')
#triugulnik S = a * b / 2
elif figure == "triangle":
    a = float(input())
    b = float(input())
    S = a * b / 2
    print(f'{S:.3f}')
