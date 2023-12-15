from math import floor

row_cols = int(input())
players_loc = []
players_loc_2 = []
matrix_1 = []
sides = {"up": [-1, 0], "down": [1, 0], "left": [0, -1], "right": [0, 1]}
coins = 0
flag = False
flag_2 = False

for i in range(row_cols):
    line = input().split()
    if "P" in line:
        players_loc.append(i)
        players_loc.append(line.index("P"))
    matrix_1.append(line)

matrix_1[players_loc[0]][players_loc[1]] = "."
players_loc_2.append(players_loc[0])
players_loc_2.append(players_loc[1])

while True:
    command = input()

    if command not in sides.keys():
        continue

    new_x = players_loc[0] + sides[command][0]
    new_y = players_loc[1] + sides[command][1]

    if new_x < 0:
        new_x = row_cols - 1
    elif new_x == row_cols:
        new_x = 0
    if new_y < 0:
        new_y = row_cols - 1
    elif new_y == row_cols:
        new_y = 0

    if matrix_1[new_x][new_y].isdigit():
        coins += int(matrix_1[new_x][new_y])
        matrix_1[new_x][new_y] = "."
        players_loc = [new_x, new_y]
        players_loc_2.append(new_x)
        players_loc_2.append(new_y)
        if coins >= 100:
            flag = True
            break
    elif matrix_1[new_x][new_y] == "X":
        players_loc_2.append(new_x)
        players_loc_2.append(new_y)
        flag_2 = True
        coins = floor(coins / 2)
        break
    else:
        players_loc = [new_x, new_y]
        players_loc_2.append(new_x)
        players_loc_2.append(new_y)

if flag:
    print(f"You won! You've collected {coins} coins.")
if flag_2:
    print(f"Game over! You've collected {coins} coins.")
print("Your path:")
for i in range(0, len(players_loc_2), 2):
    print(f"[{players_loc_2[i]}, {players_loc_2[i + 1]}]")
