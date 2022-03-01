from collections import deque

number_of_petrol_pumps = int(input())
current_petrol = 0
gas_stations = deque()
starting_station = ""
flag = False

for x in range(number_of_petrol_pumps):
    amount_of_petrol_and_distance = input()
    gas_stations.append(amount_of_petrol_and_distance)

for station in range(number_of_petrol_pumps):
    liters_and_distance = gas_stations[0].split()
    liters = int(liters_and_distance[0])
    distance = int(liters_and_distance[1])
    if liters >= distance and not flag:
        current_petrol += liters - distance
        gas_stations.rotate(-1)
        starting_station = station
        flag = True
        continue
    elif current_petrol > 0 and flag:
        current_petrol += liters
        if current_petrol >= distance:
            current_petrol -= distance
    gas_stations.rotate(-1)

print(starting_station)
