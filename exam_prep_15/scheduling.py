cycles = [int(x) for x in input().split(", ")]
index = int(input())
index_2 = 0
min_1 = 999999999999999999999
count_cycles = 0
flag = False

while cycles and not flag:

    for i in range(len(cycles)):
        if cycles[i] < min_1:
            min_1 = cycles[i]
            index_2 = cycles.index(min_1)

    if index == index_2:
        count_cycles += min_1
        flag = True
    else:
        count_cycles += min_1
        cycles.pop(index_2)
        if index_2 < index:
            index -= 1

    min_1 = 999999999999999999999

print(count_cycles)
