def is_valid(password:str):
    password_digits = False
    password_lenght = False
    password_alnum = False
    count = 0
    if len(password) <= 10 and len(password) >= 6:
        password_lenght = True
    else:
        print("Password must be between 6 and 10 characters")


    if password.isalnum():
        password_alnum = True
    else:
        print("Password must consist only of letters and digits")


    for index in password:
        if index.isnumeric():
            count += 1
            if count == 2:
                password_digits = True
                break
    else:
        print("Password must have at least 2 digits")

    if password_digits == True and password_lenght == True and password_alnum == True:
        print("Password is valid")


password = input()
is_valid(password)