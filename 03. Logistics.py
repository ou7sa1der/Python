count_cargo = int(input())

cargo_sum = 0
van_sum = 0
truck_sum = 0
train_sum = 0

for cargo_in_tons in range(1, count_cargo + 1):
    cargo_in_tons = int(input())
    if cargo_in_tons <= 3:
        van_sum += cargo_in_tons
    elif cargo_in_tons >= 4 and cargo_in_tons <= 11:
        truck_sum += cargo_in_tons
    elif cargo_in_tons >= 12:
        train_sum += cargo_in_tons
    cargo_sum += cargo_in_tons

van_percantage = van_sum / cargo_sum * 100
truck_percantage = truck_sum / cargo_sum * 100
train_percantage = train_sum / cargo_sum * 100
average_per_ton = (van_sum * 200 + truck_sum * 175 + train_sum * 120) / cargo_sum
print(f"{average_per_ton:.2f}")
print(f"{van_percantage:.2f}%")
print(f"{truck_percantage:.2f}%")
print(f"{train_percantage:.2f}%")