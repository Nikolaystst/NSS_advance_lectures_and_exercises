def find_player(row, col, multilist):
    for x in range(row):
        for y in range(col):
            if multilist[x][y] == "P":
                multilist[x][y] = "."
                return (x, y)


#                 func за проверка на коорд на играча


def valid_index(row, col, player=False):
    global win_or_loose

    if 0 <= row < rows and 0 <= col < cols:
        return True
    if player:
        win_or_loose = True


#         func за проверка на валидни индекси плюс дали играча излиза и побеждава


def find_bunnies(row, col, multilist):
    bunny_pos = []
    for x in range(row):
        for y in range(col):
            if multilist[x][y] == "B":
                bunny_pos.append((x, y))
    return bunny_pos
    # func за намиране локация на зайчетата


def bunny_growth(multilist):
    for x, y in multilist:
        for bun_mov in matrix_moves.values():
            new_x, new_y = x + bun_mov[0], y + bun_mov[1]

            if valid_index(new_x, new_y):
                matrix[new_x][new_y] = "B"


#           func за разпространение на заичетата


def am_i_alive(row, col):
    global end

    if matrix[row][col] == "B":
        end = "dead"


#   func дали не съм попаднал на зайче


rows, cols = [int(x) for x in input().split()]

win_or_loose = False
# flag за край на програмата при True обвързан с фунцкцията valid_index на 10 ред
end = "won"
# flag за край при смърт и status за принт накрая обвързан с функцията am_i_alive ред 40
matrix = [[x for x in input()] for y in range(rows)]
moves_to_do = list(input())

matrix_moves = {
    "L": (0, -1),
    "R": (0, 1),
    "U": (-1, 0),
    "D": (1, 0)
}
# dict за ходовета на местене на дъската

player_row, player_col = find_player(rows, cols, matrix)
# namiram lokaciqta na playera и го махам от дъската


for move in moves_to_do:
    player_next_row, player_next_col = player_row + matrix_moves[move][0], player_col + matrix_moves[move][1]
    # pravq dvijenieto na playera

    if valid_index(player_next_row, player_next_col, player=True):
        player_row, player_col = player_next_row, player_next_col
    #   proverqvam dali moga da ida na tam i dali ne pe4elq igrata

    bunny_growth(find_bunnies(rows, cols, matrix))
    # mestq zaichetata

    if win_or_loose:
        [print(*f, sep='') for f in matrix]
        print(f"{end}: {player_row} {player_col}")
        exit()

    am_i_alive(player_row, player_col)
    if end == "dead":
        [print(*f, sep='') for f in matrix]
        print(f"{end}: {player_row} {player_col}")
        exit()
