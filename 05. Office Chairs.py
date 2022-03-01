number_of_rooms = int(input())
free_chairs = 0
needed_chairs_in_room = 0
flag = True
for room in range(1,number_of_rooms + 1):
    chairs_and_visitors = input().split(' ')
    chairs =  chairs_and_visitors[0]
    visitors = int(chairs_and_visitors[1])
    if len(chairs) > visitors:
        free_chairs += len(chairs) - visitors
    if visitors > len(chairs):
        needed_chairs_in_room += visitors - len(chairs)
        print(f"{needed_chairs_in_room} more chairs needed in room {room}")
        needed_chairs_in_room = 0
        flag = False

if flag:
    print(f"Game On, {free_chairs} free chairs left")