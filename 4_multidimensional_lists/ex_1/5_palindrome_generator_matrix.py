row, col = [int(x) for x in input().split()]
ascii_a = 97

nss_matrix = [[chr(ascii_a + x) + chr(ascii_a + x + y) + chr(ascii_a + x) for y in range(col)] for x in range(row)]

for x in range(row):
    print(*nss_matrix[x])
