username = input()
password = input()

typed_password = input()
while typed_password != password:
    typed_password = input()
print(f"Welcome {username}!")