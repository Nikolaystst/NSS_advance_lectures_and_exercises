from collections import deque

players = deque(input().split(", "))
nultimatrix = []
rotations = 0
rotations_to_miss = deque()

for i in range(6):
    nultimatrix.append(input().split())

while True:
    rotations += 1
    coords = input().strip("()").split(", ")
    x = int(coords[0])
    y = int(coords[1])

    if rotations_to_miss:
        if rotations == rotations_to_miss[0]:
            rotations_to_miss.popleft()
            players.rotate()
            continue

    if nultimatrix[x][y] == "E":
        print(f"{players.popleft()} found the Exit and wins the game!")
        break
    elif nultimatrix[x][y] == "T":
        print(f"{players.popleft()} is out of the game! The winner is {players.pop()}.")
        break
    elif nultimatrix[x][y] == ".":
        players.rotate()
    elif nultimatrix[x][y] == "W":
        print(f"{players[0]} hits a wall and needs to rest.")
        players.rotate()
        rotations_to_miss.append(rotations + 2)
