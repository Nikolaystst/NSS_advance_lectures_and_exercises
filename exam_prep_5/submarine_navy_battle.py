sides = {"up": [-1, 0], "down": [1, 0], "left": [0, -1], "right": [0, 1]}
rows = int(input())
submarine_coords = []
nultimatrix = []
count_c = 3
mines_counter = 0

for i in range(rows):
    line = list(input())
    if "S" in line:
        submarine_coords.append(i)
        submarine_coords.append(line.index("S"))
    # if "C" in line:
    #     count_c += line.count("C")
    nultimatrix.append(line)

nultimatrix[submarine_coords[0]][submarine_coords[1]] = "-"

while True:
    where_to_go = input()

    nex = submarine_coords[0] + sides[where_to_go][0]
    ney = submarine_coords[1] + sides[where_to_go][1]

    if nultimatrix[nex][ney] == "-":
        submarine_coords = [nex, ney]
    elif nultimatrix[nex][ney] == "*":
        submarine_coords = [nex, ney]
        nultimatrix[nex][ney] = "-"
        mines_counter += 1
        if mines_counter == 3:
            print(f"Mission failed, U-9 disappeared! Last known coordinates [{nex}, {ney}]!")
            break
    elif nultimatrix[nex][ney] == "C":
        submarine_coords = [nex, ney]
        nultimatrix[nex][ney] = "-"
        count_c -= 1
        if count_c == 0:
            print("Mission accomplished, U-9 has destroyed all battle cruisers of the enemy!")
            break
nultimatrix[submarine_coords[0]][submarine_coords[1]] = "S"
for i in nultimatrix:
    print("".join(i))
