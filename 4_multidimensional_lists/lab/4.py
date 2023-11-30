row, cols = (int(x) for x in input().split(", "))

nss_matrix = [[int(y) for y in input().split()] for x in range(row)]

# 1 nachin
# x = [sum(i) for i in zip(*nss_matrix)]
# print("\n".join((str(d) for d in x)))

# 2 nachin
# sum = 0
# for y in range(cols):
#     sum = 0
#     for x in range(row):
#         sum += nss_matrix[x][y]
#     print(sum)

# 3 nachin
for y in range(cols):
    sum_1 = sum(nss_matrix[i][y] for i in range(row))
    print(sum_1)

# 3, 6
# 7 1 3 3 2 1
# 1 3 9 8 5 6
# 4 6 7 9 1 0

# 3, 3
# 1 2 3
# 4 5 6
# 7 8 9