from collections import deque

elves = deque(int(x) for x in input().split())
materials = deque(int(x) for x in input().split())
elves_energy_total_cost = 0
suc_made_toys = 0
iteration = 0

while elves and materials:
    elf = elves.popleft()

    if elf < 5:
        continue

    iteration += 1
    mat = materials.pop()

    if mat > elf:
        elf *= 2
        elves.append(elf)
        materials.append(mat)
        continue

    if iteration % 5 == 0 and iteration % 3 == 0:
        if elf >= 2 * mat:
            elf -= (2 * mat)
            elves_energy_total_cost += (2 * mat)
            elves.append(elf)
        else:
            elf *= 2
            elves.append(elf)
            materials.append(mat)
    elif iteration % 3 == 0:
        if elf >= 2 * mat:
            elf -= 2 * mat
            elf += 1
            elves_energy_total_cost += (2 * mat)
            elves.append(elf)
            suc_made_toys += 2
        else:
            elf *= 2
            elves.append(elf)
            materials.append(mat)
    elif iteration % 5 == 0:
        elf -= mat
        elves_energy_total_cost += mat
        elves.append(elf)
    else:
        elf -= mat
        elves_energy_total_cost += mat
        elf += 1
        elves.append(elf)
        suc_made_toys += 1

print(f"Toys: {suc_made_toys}")
print(f"Energy: {elves_energy_total_cost}")
print(f"Elves left: {', '.join([str(x) for x in elves])}") if elves else None
print(f"Boxes left: {', '.join([str(x) for x in materials])}") if materials else None

# 10 16 13 25
# 12 11 8

# 10 14 22 4 5
# 11 16 17 11 1 8

# 5 6 7
# 2 1 5 7 5 3