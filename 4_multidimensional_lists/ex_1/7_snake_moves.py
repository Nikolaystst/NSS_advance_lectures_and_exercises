from collections import deque

rows, cols = [int(x) for x in input().split()]
word = list(input())
copy_of_word = deque(word)

for i in range(rows):
    while len(copy_of_word) < cols:
        copy_of_word.extend(word)

    if i % 2 == 0:
        print(*[copy_of_word.popleft() for x in range(cols)], sep="")
    else:
        print(*[copy_of_word.popleft() for x in range(cols)][::-1], sep="")
