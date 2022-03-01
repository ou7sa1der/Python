floating_number = float(input())

#ako e 0
#positive
#negative
#or "large" if it exceeds 1 000 000.
#Add "small" - less than 1

first_word = ""
second_word = ""

if floating_number == 0:
    print("zero")

while floating_number > 0 or floating_number < 0:
    if floating_number > 0:
        second_word = "positive"
        if floating_number < 1 and floating_number > -1:
            first_word = "small"
            print(f"{first_word} {second_word}")
            break
        elif abs(floating_number) > 1000000:
            first_word = "large"
            print(f"{first_word} {second_word}")
            break
        else:
            print(second_word)
            break
    elif floating_number < 0:
        second_word = "negative"
        if floating_number < 1 and floating_number > -1:
            first_word = "small"
            print(f"{first_word} {second_word}")
            break
        elif abs(floating_number) > 1000000:
            first_word = "large"
            print(f"{first_word} {second_word}")
            break
        else:
            print(second_word)
            break