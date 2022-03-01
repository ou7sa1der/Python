hour = int(input())
day = input()

#office_working_time = 10 do 18 chasa
#ot ponedelnik do subota vkliuchitelno

if day == 'Monday' or day == 'Tuesday' or day == 'Wednesday' or day == 'Thursday' or day == 'Friday' or day == 'Saturday':
    if hour >= 10 and hour <= 18:
        print('open')
    else:
        print('closed')
else:
    print('closed')