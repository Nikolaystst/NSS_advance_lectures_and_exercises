rows, cols = [int(x) for x in input().split()]
nss_matrix = [[y for y in input().split()] for x in range(rows)]
counter = 0

for x in range(rows - 1):
    for y in range(cols - 1):
        if nss_matrix[x][y] == nss_matrix[x][y + 1] and \
                nss_matrix[x][y] == nss_matrix[x + 1][y] and \
                nss_matrix[x][y] == nss_matrix[x + 1][y + 1]:
            counter += 1
        # current = nss_matrix[x][y]
        # current_right = nss_matrix[x][y + 1]
        # current_down = nss_matrix[x + 1][y]
        # current_right_down = nss_matrix[x + 1][y + 1]
        #
        # counter += 1 if current == current_right and current == current_down and current == current_right_down else 0

print(counter)
