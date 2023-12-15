sides = {"up": [-1, 0], "down": [1, 0], "left": [0, -1], "right": [0, 1]}
rows, cols = input().split(",")
rows = int(rows)
cols = int(cols)

matrix_nss = []
mouse_coords = []
count_cheese = 0
eaten_cheese = 0

for i in range(rows):
    line = list(input())
    if "M" in line:
        mouse_coords.append(i)
        mouse_coords.append(line.index("M"))
    matrix_nss.append(line)
    if "C" in line:
        count_cheese += line.count("C")

matrix_nss[mouse_coords[0]][mouse_coords[1]] = "*"

while True:
    command = input()

    if command == "danger":
        print("Mouse will come back later!")
        matrix_nss[mouse_coords[0]][mouse_coords[1]] = "M"
        break

    new_x = mouse_coords[0] + sides[command][0]
    new_y = mouse_coords[1] + sides[command][1]

    if new_x not in range(0, rows) or new_y not in range(0, cols):
        matrix_nss[mouse_coords[0]][mouse_coords[1]] = "M"
        print("No more cheese for tonight!")
        break

    if matrix_nss[new_x][new_y] == "C":
        mouse_coords = [new_x, new_y]
        matrix_nss[new_x][new_y] = "*"
        eaten_cheese += 1
        if eaten_cheese == count_cheese:
            matrix_nss[new_x][new_y] = "M"
            print("Happy mouse! All the cheese is eaten, good night!")
            break

    elif matrix_nss[new_x][new_y] == "T":
        matrix_nss[new_x][new_y] = "M"
        print("Mouse is trapped!")
        break

    elif matrix_nss[new_x][new_y] == "@":
        continue

    else:
        mouse_coords = [new_x, new_y]

for i in matrix_nss:
    print("".join(i))
