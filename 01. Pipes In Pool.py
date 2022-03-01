V = int(input())
P1 = int(input())
P2 = int(input())
H = float(input())

#До колко се е запълнил басейна и коя тръба с колко процента е допринесла.
#Aко басейнът се е препълнил – с колко литра е прелял за даденото време.

pipe_one_lt = H * P1
pipe_two_lt = H * P2
both_pipes = pipe_one_lt + pipe_two_lt
both_pipes_percent = (both_pipes / V) * 100
pipe_one_litres = (pipe_one_lt / both_pipes) * 100
pipe_two_litres = (pipe_two_lt / both_pipes) * 100

if both_pipes > V:
    liters_over = both_pipes - V
    print(f"For {H:.2f} hours the pool overflows with {liters_over:.2f} liters.")
else:
    print(f"The pool is {both_pipes_percent:.2f}% full. Pipe 1: {pipe_one_litres:.2f}%. Pipe 2: {pipe_two_litres:.2f}%.")