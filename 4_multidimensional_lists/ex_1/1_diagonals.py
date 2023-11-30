n = int(input())

nss_matrix = [[int(x) for x in input().split(", ")] for y in range(n)]

diagonal = [nss_matrix[i][i] for i in range(n)]
diagonal_2 = [nss_matrix[i][n - 1 - i] for i in range(n)]

print(f"Primary diagonal: {', '.join([str(x) for x in diagonal])}. Sum: {sum(diagonal)} ")
print(f"Secondary diagonal: {', '.join([str(x) for x in diagonal_2])}. Sum: {sum(diagonal_2)} ")
