time_player1 = int(input())
time_player2 = int(input())
time_player3 = int(input())
import math

total_time = time_player1 + time_player2 + time_player3

minutes = total_time / 60
seconds = total_time % 60

minutes = math.floor(minutes)

if seconds < 10:
    print(f'{minutes}:0{seconds}')
else:
    print(f'{minutes}:{seconds}')


