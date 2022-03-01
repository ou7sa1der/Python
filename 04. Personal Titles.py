age = float(input())
gender = input()

#    • Mr." – мъж (пол 'm') на 16 или повече години
#    • "Master" – момче (пол 'm') под 16 години

#    • "Ms." – жена (пол 'f') на 16 или повече години
#    • "Miss" – момиче (пол 'f') под 16 години

if gender == "m":
    if age >= 16:
        print("Mr.")
    else:
        print("Master")
elif gender == "f":
    if age >= 16:
        print("Ms.")
    else:
        print("Miss")