operations = input()
total_sum = 0

while operations != "NoMoreMoney":
    operations_to_number = float(operations)
    if operations_to_number >= 0:
        total_sum += operations_to_number
        print(f"Increase: {operations_to_number:.2f}")
        operations = input()
    elif operations_to_number < 0:
        print("Invalid operation!")
        break
print(f"Total: {total_sum:.2f}")