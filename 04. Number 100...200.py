number = int(input())

#ako e pod 100
if number < 100:
    print("Less than 100")
#ako e mejdu 100 i 200
elif number >= 100 and number <= 200:
    print("Between 100 and 200")
#ako e nad 200
else:
    print("Greater than 200")