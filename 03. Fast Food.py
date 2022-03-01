from collections import deque

quantity_of_food = int(input())
first_sequence = input().split()
sequence_orders = deque(first_sequence)
completed_orders = []

while sequence_orders:
    order = sequence_orders[0]
    if quantity_of_food >= int(order):
        quantity_of_food -= int(order)
        completed_orders.append(int(order))
        sequence_orders.popleft()
    else:
        quantity_of_food -= int(order)
        break

for x in range(len(first_sequence)):
    first_sequence[x] = int(first_sequence[x])
print(max(first_sequence))

if quantity_of_food >= 0:
    print("Orders complete")
else:
    print(f"Orders left: {' '.join(sequence_orders)}")