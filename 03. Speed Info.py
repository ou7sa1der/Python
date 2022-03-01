speed = float(input())

#ako e do 10 - otpechatvame slow
if speed <= 10:
    print("slow")
#ako e nad 10 i do 50 - average
elif speed > 10 and speed <= 50:
    print("average")
#ako e nad 50 i do 150 - fast
elif speed > 50 and speed <= 150:
    print("fast")
#ako e nad 150 i do 1000 - ultra fast
elif speed > 150 and speed <= 1000:
    print("ultra fast")
#ako e nad 1000 - extremely fast
else:
    print("extremely fast")