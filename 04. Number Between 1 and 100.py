input_number = float(input())

while True:
    if input_number >= 1 and input_number <= 100:
        print(f"The number {input_number} is between 1 and 100")
        break
    else:
        input_number = float(input())