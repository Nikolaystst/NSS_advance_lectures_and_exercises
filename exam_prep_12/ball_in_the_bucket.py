SIZE = 6

matrix_1 = [[x for x in input().split()] for y in range(SIZE)]
points = 0

for i in range(3):
    coords = [int(x) for x in input().strip("()").split(", ")]

    if 0 > coords[0] or coords[0] >= SIZE or 0 > coords[1] or coords[1] >= SIZE:
        continue

    if matrix_1[coords[0]][coords[1]] == "B":
        matrix_1[coords[0]][coords[1]] = "0"
        for num in range(6):
            if matrix_1[num][coords[1]].isdigit():
                points += int(matrix_1[num][coords[1]])

if points < 100:
    print(f"Sorry! You need {100 - points} points more to win a prize.")
elif 100 <= points <= 199:
    print(f"Good job! You scored {points} points, and you've won Football.")
elif 200 <= points <= 299:
    print(f"Good job! You scored {points} points, and you've won Teddy Bear.")
elif points >= 300:
    print(f"Good job! You scored {points} points, and you've won Lego Construction Set.")

# for i in matrix_1:
#     print(i)
