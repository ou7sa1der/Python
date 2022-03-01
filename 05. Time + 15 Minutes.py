hours = int(input())
minutes = int(input())
minutes += 15
#chasovete vinagi sa mejdu 0 i 23
#minutite vinagi sa mejdu 0 i 59
hours += minutes // 60
minutes = minutes % 60
if hours > 23:
    hours -= 24
if minutes <= 9:
    print(f'{hours}:0{minutes}')
else:
    print(f'{hours}:{minutes}')