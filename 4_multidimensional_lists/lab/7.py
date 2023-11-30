rows, cols = [int(x) for x in input().split(", ")]

nss_matrix = [[int(x) for x in input().split(", ")] for y in range(rows)]
final_matrix = []

sum_1 = 0

for x in range(rows - 1):
    for y in range(cols - 1):
        top_left = nss_matrix[x][y]
        top_right = nss_matrix[x][y + 1]
        bottom_left = nss_matrix[x + 1][y]
        bottom_right = nss_matrix[x + 1][y + 1]

        if (top_left + top_right + bottom_left + bottom_right) > sum_1:
            sum_1 = top_left + top_right + bottom_left + bottom_right
            final_matrix = [[top_left, top_right], [bottom_left, bottom_right]]

print(final_matrix[0][0], final_matrix[0][1])
print(final_matrix[1][0], final_matrix[1][1])
print(sum_1)

# 3, 6
# 7, 1, 3, 3, 2, 1
# 1, 3, 9, 8, 5, 6
# 4, 6, 7, 9, 1, 0

# 2, 4
# 10, 11, 12, 13
# 14, 15, 16, 17
