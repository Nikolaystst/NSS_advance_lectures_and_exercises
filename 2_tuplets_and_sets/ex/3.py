nss_set = set()
for i in range(int(input())):
    for b in input().split():
        nss_set.add(b)

print(*nss_set, sep="\n")
