def pump_the_queens(row, lst):
    many = lst.count("Q")
    for i in range(many):
        queen_locations.append(row)
        queen_locations.append(lst.index("Q"))
        lst[queen_locations[-1]] = "."


def chek_index(x, y, counter, side):
    def chek_coord(x_1, y_1):
        if x_1 in range(0, 8) and y_1 in range(0, 8):
            return True
        else:
            return False

    new_x = x + (sides[side][0] * counter)
    new_y = y + (sides[side][1] * counter)
    to_contunie = chek_coord(new_x, new_y)
    if to_contunie:
        if nultimatrix[new_x][new_y] == "K":
            return "King"
        elif nultimatrix[new_x][new_y] == "Q":
            return "Queen"
        else:
            return "goon"
    elif not to_contunie:
        return "None"


sides = {"up": [-1, 0], "down": [1, 0], "left": [0, -1], "right": [0, 1], "up-right": [-1, 1], "up-left": [-1, -1],
         "down-right": [1, 1], "down-left": [1, -1]}

queen_locations = []
king_location = []
nultimatrix = []
final_queens = []

for i in range(8):
    line = input().split()
    if "K" in line:
        king_location = [i, line.index("K")]
    if "Q" in line:
        pump_the_queens(i, line)
    nultimatrix.append(line)

for i in range(0, len(queen_locations), 2):
    nultimatrix[queen_locations[i]][queen_locations[i + 1]] = "Q"

for i in range(0, len(queen_locations), 2):
    x = queen_locations[i]
    y = queen_locations[i + 1]
    for key in sides.keys():
        count = 0
        while True:
            flag = False
            count += 1
            to_do = chek_index(x, y, count, key)
            if to_do == "King":
                final_queens.append([x, y])
                flag = True
                break
            elif to_do == "Queen":
                break
            elif to_do == "None":
                break

        if flag:
            break

print(king_location)
print(final_queens)
for i in nultimatrix:
    print(i)
