string_even_int = list(map(int,input().split('@')))
love_flag = False
houses_done = 0
cupid_last_position = 0
command = input().split(' ')
zero_flag = []
while command != 'Love!':
    cupid = int(command[1]) + cupid_last_position
    if cupid >= len(string_even_int):
        cupid = 0
    string_even_int[cupid] = string_even_int[cupid] - 2
    if string_even_int[cupid] <= 0:
        string_even_int[cupid] = 0
        if cupid in zero_flag:
            print(f"Place {cupid} already had Valentine's day.")
        else:
            houses_done += 1
            print(f"Place {cupid} has Valentine's day.")
            zero_flag.append(cupid)
    cupid_last_position = cupid
    command = input().split(' ')
    if 'Love!' in command:
        love_flag = True
        break
print(f"Cupid's last position was {cupid_last_position}.")
if love_flag:
    print(f"Cupid has failed {len(string_even_int) - houses_done} places.")
else:
    print("Mission was successful.")