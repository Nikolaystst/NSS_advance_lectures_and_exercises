num = int(input())
nultilist = []
bunny_loc = []
best = []
best_direction = None
max_collected_eggs = 0

func_map = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

for x in range(num):
    r = input().split()
    nultilist.append(r)
    if "B" in r:
        bunny_loc = [x, r.index("B")]

for directions, x_y in func_map.items():
    rout = []
    collected = 0
    row, col = [bunny_loc[0] + x_y[0], bunny_loc[1] + x_y[1]]

    while 0 <= row < num and 0 <= col < num:
        if nultilist[row][col] == "X":
            break

        collected += int(nultilist[row][col])
        rout.append([row, col])
        row += x_y[0]
        col += x_y[1]

    if collected > max_collected_eggs:
        max_collected_eggs = collected
        best_direction = directions
        best = rout

print(best_direction)
[print(x) for x in best]
print(max_collected_eggs)
