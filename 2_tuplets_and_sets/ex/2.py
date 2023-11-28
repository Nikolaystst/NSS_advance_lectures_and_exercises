command = input().split()
st_set = set()
nd_set = set()
for i in range(int(command[0])):
    st_set.add(int(input()))
for b in range(int(command[1])):
    nd_set.add(int(input()))

print(*st_set.intersection(nd_set), sep="\n")