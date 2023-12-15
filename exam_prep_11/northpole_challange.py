row, cols = [int(x) for x in input().split(", ")]
sides = {"up": [-1, 0], "down": [1, 0], "left": [0, -1], "right": [0, 1]}
santas_pos = []
counter = 0
cristmas_dec = 0
gifts = 0
cookies = 0
matrix_1 = []
flag = False

for i in range(row):
    line = input().split()
    if "Y" in line:
        santas_pos.append(i)
        santas_pos.append(line.index("Y"))
    if "D" in line:
        counter += line.count("D")
    if "G" in line:
        counter += line.count("G")
    if "C" in line:
        counter += line.count("C")
    matrix_1.append(line)

matrix_1[santas_pos[0]][santas_pos[1]] = "x"


def valid_side(x, y):
    if x < 0:
        x = row - 1
    elif x == row:
        x = 0
    if y < 0:
        y = cols - 1
    elif y == cols:
        y = 0
    return [x, y]


while True:
    command = input().split("-")

    if command[0] == "End":
        break

    side = command[0]
    range_1 = int(command[1])

    for i in range(range_1):
        new_x = santas_pos[0] + sides[side][0]
        new_y = santas_pos[1] + sides[side][1]
        santas_pos = valid_side(new_x, new_y)

        if matrix_1[santas_pos[0]][santas_pos[1]] == "D":
            cristmas_dec += 1
        elif matrix_1[santas_pos[0]][santas_pos[1]] == "G":
            gifts += 1
        elif matrix_1[santas_pos[0]][santas_pos[1]] == "C":
            cookies += 1

        if counter == cristmas_dec + gifts + cookies:
            flag = True
            break
        else:
            matrix_1[santas_pos[0]][santas_pos[1]] = "x"

    if flag:
        break

matrix_1[santas_pos[0]][santas_pos[1]] = "Y"

print("Merry Christmas!") if flag else None
print("You've collected:")
print(f"- {cristmas_dec} Christmas decorations")
print(f"- {gifts} Gifts")
print(f"- {cookies} Cookies")
for line in matrix_1:
    print(" ".join(line))
