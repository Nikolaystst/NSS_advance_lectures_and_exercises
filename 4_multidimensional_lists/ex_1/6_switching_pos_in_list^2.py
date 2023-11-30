row, col = [int(x) for x in input().split()]

nss_matrix = [[x for x in input().split()] for y in range(row)]

while True:
    command = input()
    if command == "END":
        break
    command = command.split()

    if command[0] != "swap" or len(command) != 5:
        print("Invalid input!")
        continue
    elif command[0] == "swap":
        x1 = int(command[1])
        y1 = int(command[2])
        x2 = int(command[3])
        y2 = int(command[4])
        if x1 >= row or x2 >= row or y1 >= col or y2 >= col:
            print("Invalid input!")
            continue
        else:
            nss_matrix[x1][y1], nss_matrix[x2][y2] = nss_matrix[x2][y2], nss_matrix[x1][y1]
            for i in range(row):
                print(*nss_matrix[i])
