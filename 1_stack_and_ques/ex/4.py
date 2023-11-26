nss_stack = [int(x) for x in input().split()]
capacity_of_rack = int(input())
starting_capacity = capacity_of_rack
racks = 1

for value_of_cloth in nss_stack:
    if value_of_cloth <= capacity_of_rack:
        capacity_of_rack -= value_of_cloth
    else:
        racks += 1
        capacity_of_rack = starting_capacity
        capacity_of_rack -= value_of_cloth

print(racks)
