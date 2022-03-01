age = int(input())
#Kids drink toddy, Teens drink coke, Young adults drink beer, Adults drink whisky.
#Rules:
#Kids under 14 years old.
#Teens under 18 years old.
#Young adults under 21 years old.
#Adults above 21.
#Note: All the values except the last one are inclusive!
if age <= 14:
    print("drink toddy")
elif age <= 18:
    print("drink coke")
elif age <= 21:
    print("drink beer")
else:
    print("drink whisky")