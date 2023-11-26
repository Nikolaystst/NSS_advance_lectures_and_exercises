from _collections import deque

petrol_stations = int(input())
gas_in_tank = 0
counter_gas_stations = 0
nss_deque = deque()
flag = True

for i in range(petrol_stations):
    nss_deque.append([int(x) for x in input().split()])

while flag:

    for gas_distance in nss_deque:
        gas_in_tank += gas_distance[0]
        if gas_in_tank >= gas_distance[1]:
            gas_in_tank -= gas_distance[1]
            continue
        else:
            nss_deque.rotate(-1)
            gas_in_tank = 0
            counter_gas_stations += 1
            break

    else:
        flag = False
print(counter_gas_stations)
