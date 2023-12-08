from collections import deque


def sq_loc(line):
    if "s" in line:
        sq_location.append(i)
        sq_location.append(line.index("s"))


def chek_index(x, y):
    global flag
    if 0 > x or x == size or 0 > y or y == size:
        flag = True
        return print("The squirrel is out of the field.")


size = int(input())
moves = deque(input().split(", "))
nutrix = []
sq_location = []
sides = {"up": [-1, 0], "down": [1, 0], "left": [0, -1], "right": [0, 1]}
flag = False
hazzelnuts = 0

for i in range(size):
    line = list(input())
    nutrix.append(line)
    sq_loc(line)

nutrix[sq_location[0]][sq_location[1]] = "*"

while moves:
    if flag:
        break

    current_move = moves.popleft()

    new_x = sq_location[0] + sides[current_move][0]
    new_y = sq_location[1] + sides[current_move][1]
    chek_index(new_x, new_y)

    sq_location = [new_x, new_y]
    if flag:
        break

    if nutrix[new_x][new_y] == "t":
        print("Unfortunately, the squirrel stepped on a trap...")
        flag = True
    elif nutrix[new_x][new_y] == "h":
        nutrix[new_x][new_y] = "*"
        hazzelnuts += 1
        if hazzelnuts == 3:
            print("Good job! You have collected all hazelnuts!")
            flag = True

if hazzelnuts < 3 and not flag:
    print("There are more hazelnuts to collect.")
print(f"Hazelnuts collected: {hazzelnuts}")
