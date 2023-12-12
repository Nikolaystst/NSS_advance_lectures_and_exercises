SIZE = 6

nultimix = []
sides = {"up": [-1, 0], "down": [1, 0], "left": [0, -1], "right": [0, 1]}

for i in range(SIZE):
    nultimix.append(input().split())

starting_x_y = [int(x) for x in input().strip("()").split(", ")]

while True:
    command = input().split(", ")

    if command[0] == "Stop":
        break

    nex = starting_x_y[0] + sides[command[1]][0]
    ney = starting_x_y[1] + sides[command[1]][1]

    starting_x_y = [nex, ney]

    if command[0] == "Create":
        if nultimix[nex][ney] == ".":
            nultimix[nex][ney] = command[2]
    elif command[0] == "Update":
        if nultimix[nex][ney].isdigit() or nultimix[nex][ney].isalpha():
            nultimix[nex][ney] = command[2]
    elif command[0] == "Delete":
        if nultimix[nex][ney].isdigit() or nultimix[nex][ney].isalpha():
            nultimix[nex][ney] = "."
    elif command[0] == "Read":
        if nultimix[nex][ney].isdigit() or nultimix[nex][ney].isalpha():
            print(nultimix[nex][ney])

for i in nultimix:
    print(" ".join(i))
