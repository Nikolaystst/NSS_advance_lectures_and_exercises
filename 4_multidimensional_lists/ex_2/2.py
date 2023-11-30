rows = int(input())
nss_multilist = [[int(x) for x in input().split()] for y in range(rows)]


def valid_index(x, y):
    if 0 <= x < rows and 0 <= y < rows:
        return True


def list_moving(yes_no, x, y, val, multilist):
    if yes_no == "Add":
        multilist[x][y] += val
    else:
        multilist[x][y] -= val
    return multilist


while True:
    command = input().split()

    if command[0] == "END":
        break

    to_do = command[0]
    row = int(command[1])
    col = int(command[2])
    val = int(command[3])

    if not valid_index(row, col):
        print("Invalid coordinates")
        continue

    list_moving(to_do, row, col, val, nss_multilist)

[print(*x) for x in nss_multilist]

# 3
# 1 2 3
# 4 5 6
# 7 8 9
# Add 0 0 5
# Subtract 1 1 2
# END

# 4
# 1 2 3 4
# 5 6 7 8
# 8 7 6 5
# 4 3 2 1
# Add 4 4 100
# Add 3 3 100
# Subtract -1 -1 42
# Subtract 0 0 42
# END
