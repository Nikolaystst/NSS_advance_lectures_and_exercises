size = int(input())

nss = []
alice_loc = []

tea_bags = 0

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}

for i in range(size):
    nss.append(input().split())

    if 'A' in nss[i]:
        alice_loc = [i, nss[i].index('A')]
        nss[i][alice_loc[1]] = '*'

while tea_bags < 10:
    direction = input()

    row = alice_loc[0] + directions[direction][0]
    col = alice_loc[1] + directions[direction][1]

    if not (0 <= row < size and 0 <= row < size):
        break

    alice_loc = [row, col]
    symbol = nss[row][col]
    nss[row][col] = '*'

    if symbol == 'R':
        break

    if symbol.isdigit():
        tea_bags += int(symbol)


if tea_bags < 10:
    print("Alice didn't make it to the tea party.")
else:
    print("She did it! She went to the party.")

print(*[' '.join(row) for row in nss], sep='\n')
