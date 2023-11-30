nss_matrix = [[int(x) for x in input().split(", ")] for y in range(int(input().split(", ")[0]))]
sum_1 = sum(sum(x) for x in nss_matrix)

print(sum_1)
print(nss_matrix)
