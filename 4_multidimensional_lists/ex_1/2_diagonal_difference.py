size_1 = int(input())
nss_matrix = [[int(y) for y in input().split()] for x in range(size_1)]

sum_1 = sum([nss_matrix[x][x] for x in range(size_1)])
sum_2 = sum([nss_matrix[x][size_1 - 1 - x] for x in range(size_1)])
print(abs(sum_1 - sum_2))
