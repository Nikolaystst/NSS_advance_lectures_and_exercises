n = int(input())

nss_matrix = [[int(y) for y in input().split()] for x in range(n)]
sum_one = sum(nss_matrix[i][i] for i in range(n))

print(sum_one)
