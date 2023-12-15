from collections import deque

player_1_2_names = deque(input().split(", "))
players_dict = {f"{player_1_2_names[0]}": [501, 0], f"{player_1_2_names[1]}": [501, 0]}

matrix_1 = [[x for x in input().split()] for y in range(7)]

while True:
    command = input().strip("()").split(", ")
    x = int(command[0])
    y = int(command[1])
    players_dict[player_1_2_names[0]][1] += 1

    if x < 0 or x >= 7 or y < 0 or y >= 7:
        player_1_2_names.rotate()
        continue

    if matrix_1[x][y].isdigit():
        players_dict[player_1_2_names[0]][0] -= int(matrix_1[x][y])
    elif matrix_1[x][y] == "D":
        players_dict[player_1_2_names[0]][0] -= 2 * (int(matrix_1[x][0]) + int(matrix_1[x][6]) + int(matrix_1[0][y]) +
                                                     int(matrix_1[6][y]))
    elif matrix_1[x][y] == "T":
        players_dict[player_1_2_names[0]][0] -= 3 * (int(matrix_1[x][0]) + int(matrix_1[x][6]) + int(matrix_1[0][y]) +
                                                     int(matrix_1[6][y]))
    elif matrix_1[x][y] == "B":
        break

    if players_dict[player_1_2_names[0]][0] <= 0:
        break

    player_1_2_names.rotate()

name = player_1_2_names.popleft()
print(f"{name} won the game with {players_dict[name][1]} throws!")
