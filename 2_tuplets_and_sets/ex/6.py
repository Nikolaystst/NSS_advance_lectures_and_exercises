def ascii_func(name, num):
    return int(sum(ord(x) for x in name) / num)


odd_set = set()
even_set = set()
num = 1

for i in range(int(input())):
    name = ascii_func(input(), num)
    num += 1
    if name % 2 == 0:
        even_set.add(name)
    else:
        odd_set.add(name)

if sum(odd_set) == sum(even_set):
    print(*odd_set.union(even_set), sep=", ")
elif sum(odd_set) > sum(even_set):
    print(*odd_set.difference(even_set), sep=", ")
elif sum(odd_set) < sum(even_set):
    print(*odd_set.symmetric_difference(even_set), sep=", ")
