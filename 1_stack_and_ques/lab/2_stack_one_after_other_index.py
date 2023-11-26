text = list(input())
lst_indexes = []
index = 0

for i in range(len(text)):
    ch = text[i]

    if ch == "(":
        index = i
        lst_indexes.append(index)
    elif ch == ")":
        print("".join(text[lst_indexes.pop(): i + 1]))
