nss_list = [x.split() for x in input().split("|")[::-1]]
[print(*f, sep=" ", end=" ") for f in nss_list if f]
