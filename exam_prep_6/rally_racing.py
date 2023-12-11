size = int(input())
racing_num = input()
tracked_car_x_y = [0, 0]
nultimatrix = []
sides = {"up": [-1, 0], "down": [1, 0], "left": [0, -1], "right": [0, 1]}
total_km = 0
tunnels_coords = []
flag = False

for i in range(size):
    line = input().split()
    nultimatrix.append(line)
    if "T" in line:
        tunnels_coords.append(i)
        tunnels_coords.append(line.index("T"))

while True:
    command = input()

    if command == "End":
        break

    new_x = tracked_car_x_y[0] + sides[command][0]
    new_y = tracked_car_x_y[1] + sides[command][1]
    total_km += 10

    if nultimatrix[new_x][new_y] == ".":
        tracked_car_x_y = [new_x, new_y]
    elif nultimatrix[new_x][new_y] == "T":
        total_km += 20
        if new_x == tunnels_coords[0] and new_y == tunnels_coords[1]:
            tracked_car_x_y = [tunnels_coords[2], tunnels_coords[3]]
        elif new_x == tunnels_coords[2] and new_y == tunnels_coords[3]:
            tracked_car_x_y = [tunnels_coords[0], tunnels_coords[1]]
        nultimatrix[tunnels_coords[0]][tunnels_coords[1]] = "."
        nultimatrix[tunnels_coords[2]][tunnels_coords[3]] = "."
    elif nultimatrix[new_x][new_y] == "F":
        tracked_car_x_y = [new_x, new_y]
        nultimatrix[new_x][new_y] = "C"
        flag = True
        break

if flag:
    print(f"Racing car {racing_num} finished the stage!")
else:
    nultimatrix[tracked_car_x_y[0]][tracked_car_x_y[1]] = "C"
    print(f"Racing car {racing_num} DNF.")

print(f"Distance covered {total_km} km.")
for i in nultimatrix:
    print("".join(i))
