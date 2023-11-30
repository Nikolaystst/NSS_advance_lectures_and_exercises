row, col = [int(x) for x in input().split()]
nss_matrx = [[int(x) for x in input().split()] for y in range(row)]
final_matrix = []
sum_1 = -99999999999999999999999999999999

for x in range(row - 2):
    for y in range(col - 2):
        one = nss_matrx[x][y]
        two = nss_matrx[x][y + 1]
        three = nss_matrx[x][y + 2]
        four = nss_matrx[x + 1][y]
        five = nss_matrx[x + 1][y + 1]
        six = nss_matrx[x + 1][y + 2]
        seven = nss_matrx[x + 2][y]
        eight = nss_matrx[x + 2][y + 1]
        nine = nss_matrx[x + 2][y + 2]

        if (one + two + three + four + five + six + seven + eight + nine) > sum_1:
            final_matrix = [
                [one, two, three],
                [four, five, six],
                [seven, eight, nine]
            ]
            sum_1 = one + two + three + four + five + six + seven + eight + nine

print(f"Sum = {sum_1}")
print(*[str(x) for x in final_matrix[0]], sep=" ")
print(*[str(x) for x in final_matrix[1]], sep=" ")
print(*[str(x) for x in final_matrix[2]], sep=" ")
