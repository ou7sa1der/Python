from collections import deque
kids_playing = deque(input().split(' '))
n_th_toss = int(input())

while not len(kids_playing) == 1:
    kids_playing.rotate(-1)
    print(f'Removed {kids_playing.pop()}')
        
print(f"Last is {kids_playing.pop()}")
