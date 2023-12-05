def coord_search(symbol, line):
    if symbol == "w":
        coords_white.append(row)
        coords_white.append(line.index(symbol))
    elif symbol == "b":
        coords_black.append(row)
        coords_black.append(line.index(symbol))


size = 8
chess = []
coords_white = []
coords_black = []

for row in range(size):
    line = input().split()
    chess.append(line)
    if "w" in line:
        coord_search("w", line)
    elif "b" in line:
        coord_search("b", line)

if abs(coords_white[1] - coords_black[1]) != 1:
    till_end_white = coords_white[0]
    till_end_black = size - coords_black[0] - 1
    if till_end_white <= till_end_black:
        print(f"Game over! White pawn is promoted to a queen at {chr(97 + coords_white[1])}8.")
    else:
        print(f"Game over! Black pawn is promoted to a queen at {chr(97 + coords_black[1])}1.")

else:
    pos = (coords_white[0] + coords_black[0]) // 2
    if (coords_white[0] - coords_black[0]) % 2 == 1:
        print(f"Game over! White win, capture on {chr(97 + coords_black[1])}{8 - pos}.")
    else:
        print(f"Game over! Black win, capture on {chr(97 + coords_white[1])}{8 - pos}.")
