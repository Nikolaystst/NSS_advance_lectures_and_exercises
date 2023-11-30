nss_matrix = [[y for y in input()] for x in range(int(input()))]
searched_symbol = input()

for x in range(len(nss_matrix)):
    for y in range(len(nss_matrix)):
        current_symbol = nss_matrix[x][y]
        if current_symbol == searched_symbol:
            print(f"({x}, {y})")
            quit()

print(f"{searched_symbol} does not occur in the matrix")
