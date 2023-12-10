def chek_play(x, lst):
    if "B" in lst:
        p_loc.append(x)
        p_loc.append(lst.index("B"))


rows, cols = [int(x) for x in input().split()]

nultilist_1 = []
p_loc = []
count_moves = 0
count_touched = 0
sides = {"up": [-1, 0], "down": [1, 0], "left": [0, -1], "right": [0, 1]}

for i in range(rows):
    line = input().split()
    chek_play(i, line)
    nultilist_1.append(line)

nultilist_1[p_loc[0]][p_loc[1]] = "-"

while True:
    command = input()

    if command == "Finish":
        break

    new_x = p_loc[0] + sides[command][0]
    new_y = p_loc[1] + sides[command][1]

    if new_x < 0 or new_x == rows:
        continue
    elif new_y < 0 or new_y == cols:
        continue
    elif nultilist_1[new_x][new_y] == "O":
        continue
    elif nultilist_1[new_x][new_y] == "-":
        count_moves += 1
        p_loc = [new_x, new_y]
    elif nultilist_1[new_x][new_y] == "P":
        count_moves += 1
        count_touched += 1
        nultilist_1[new_x][new_y] = "-"
        p_loc = [new_x, new_y]
        if count_touched == 3:
            break

print("Game over!")
print(f"Touched opponents: {count_touched} Moves made: {count_moves}")
