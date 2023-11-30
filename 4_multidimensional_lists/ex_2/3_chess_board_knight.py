def knight_locs_func(nultilist):
    for x in range(board):
        for y in range(board):
            if nultilist[x][y] == "K":
                knight_locs.append([x, y])


def valid_index(x, y):
    for move in moves.values():
        new_x = x + move[0]
        new_y = y + move[1]
        if 0 <= new_x < board and 0 <= new_y < board:
            posible_moves.append([new_x, new_y])


board = int(input())
nultilist = [list(input()) for y in range(board)]
knight_locs = []
knight_locs_func(nultilist)
knigts_removed = 0

moves = {
    "up_left": (-2, -1),
    "up_right": (-2, 1),
    "right_up": (-1, 2),
    "right_down": (1, 2),
    "down_right": (2, 1),
    "down_left": (2, -1),
    "left_down": (1, -2),
    "left_up": (-1, -2)
}

while True:
    max_atacks = 0
    top_atacker_coord = []

    for x, y in knight_locs:
        posible_moves = []
        current_atack = 0

        valid_index(x, y)

        for atack in posible_moves:
            if nultilist[atack[0]][atack[1]] == "K":
                current_atack += 1

        if current_atack > max_atacks:
            max_atacks = current_atack
            top_atacker_coord = [x, y]

    knight_locs = []

    if not max_atacks:
        break

    nultilist[top_atacker_coord[0]][top_atacker_coord[1]] = "0"
    knigts_removed += 1
    knight_locs_func(nultilist)

print(knigts_removed)

# 5
# 0K0K0
# K000K
# 00K00
# K000K
# 0K0K0

# 8
# 0K0KKK00
# 0K00KKKK
# 00K0000K
# KKKKKK0K
# K0K0000K
# KK00000K
# 00K0K000
# 000K00KK