kind = input()
import math
if kind == 'square':
    a = float(input())
    S = a * a
    print(f'{S:.3f}')
elif kind == 'rectangle':
    a = float(input())
    b = float(input())
    S = a * b
    print(f'{S:.3f}')
elif kind == 'circle':
    a = float(input())
    S = math.pi * (a*a)
    print(f'{S:.3f}')
elif kind == 'triangle':
    a = float(input())
    h = float(input())
    S = a * h / 2
    print(f'{S:.3f}')