width = int(input())
lenght = int(input())

cake_size = width * lenght
pieces_count = 0
pieces_sum = 0

command = input()
while command != "STOP":
    pieces_sum += int(command)
    pieces_count += 1
    if pieces_sum > cake_size:
        needed_pieces = pieces_sum - cake_size
        print(f"No more cake left! You need {needed_pieces} pieces more.")
        break
    command = input()
if command == "STOP":
    left_pieces = cake_size - pieces_sum
    print(f"{left_pieces} pieces are left.")