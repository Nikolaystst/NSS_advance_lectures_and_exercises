def chek_coord(x_1, y_1):
    if x_1 in range(0, 8) and y_1 in range(0, 8):
        return True
    else:
        return False


sides = {"up": [-1, 0], "down": [1, 0], "left": [0, -1], "right": [0, 1], "up-right": [-1, 1], "up-left": [-1, -1],
         "down-right": [1, 1], "down-left": [1, -1]}

king_location = []
nultimatrix = []
final_queens = []
counter = 0

for i in range(8):
    line = input().split()
    if "K" in line:
        king_location = [i, line.index("K")]
    nultimatrix.append(line)

for key in sides.keys():
    counter = 0
    while True:
        flag = False
        counter += 1
        new_x = king_location[0] + (sides[key][0] * counter)
        new_y = king_location[1] + (sides[key][1] * counter)
        to_do = chek_coord(new_x, new_y)
        if to_do:
            if nultimatrix[new_x][new_y] == "Q":
                final_queens.append([new_x, new_y])
                flag = True
                break
        elif not to_do:
            break

    if flag:
        continue

if final_queens:
    for i in final_queens:
        print(i)
else:
    print("The king is safe!")