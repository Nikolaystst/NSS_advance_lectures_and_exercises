from collections import deque


def chek_rover(line):
    if "E" in line:
        rover_coord.append(i)
        rover_coord.append(line.index("E"))
        matrix[rover_coord[0]][rover_coord[1]] = "-"


def chek_new_coord(rover_coord, side_tuple):
    coord_x = rover_coord[0] + side_tuple[0]
    coord_y = rover_coord[1] + side_tuple[1]

    if coord_x == -1:
        coord_x = 5
    elif coord_x == 6:
        coord_x = 0

    if coord_y == -1:
        coord_y = 5
    elif coord_y == 6:
        coord_y = 0

    return [coord_x, coord_y]


def chek_for_water(rover_coords):
    global water
    if matrix[rover_coords[0]][rover_coord[1]] == "W":
        matrix[rover_coords[0]][rover_coord[1]] = "-"
        print(f"Water deposit found at ({rover_coords[0]}, {rover_coords[1]})")
        water += 1


def chek_for_metal(rover_coords):
    global metal
    if matrix[rover_coords[0]][rover_coord[1]] == "M":
        matrix[rover_coords[0]][rover_coord[1]] = "-"
        print(f"Metal deposit found at ({rover_coords[0]}, {rover_coords[1]})")
        metal += 1


def chek_for_concrete(rover_coords):
    global concrete
    if matrix[rover_coords[0]][rover_coord[1]] == "C":
        matrix[rover_coords[0]][rover_coord[1]] = "-"
        print(f"Concrete deposit found at ({rover_coords[0]}, {rover_coords[1]})")
        concrete += 1


def chek_for_broken(rover_coords):
    global flag
    if matrix[rover_coords[0]][rover_coord[1]] == "R":
        print(f"Rover got broken at ({rover_coords[0]}, {rover_coords[1]})")
        flag = True


field = 6

water = 0
metal = 0
concrete = 0
matrix = []
rover_coord = []
flag = False
sides = {"up": (-1, 0), "down": (1, 0), "left": (0, -1), "right": (0, 1)}

for i in range(field):
    line = input().split()
    matrix.append(line)

    chek_rover(line)

commands_to_do = deque(input().split(", "))

while commands_to_do:
    to_do = commands_to_do.popleft()

    rover_coord = chek_new_coord(rover_coord, sides[to_do])
    chek_for_water(rover_coord)
    chek_for_metal(rover_coord)
    chek_for_concrete(rover_coord)
    chek_for_broken(rover_coord)
    if flag:
        break

if water > 0 and metal > 0 and concrete > 0:
    print("Area suitable to start the colony.")
else:
    print("Area not suitable to start the colony.")
