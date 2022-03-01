text = input()

encrypted_text = ''

for char in text:
    sum_of_chars = ord(char) + 3
    encrypted_text += chr(sum_of_chars)

print(encrypted_text)