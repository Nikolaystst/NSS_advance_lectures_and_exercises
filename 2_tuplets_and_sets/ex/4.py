nss_dict = {}

for i in list(input()):
    if i not in nss_dict.keys():
        nss_dict[i] = 0
    nss_dict[i] += 1

for key, val in sorted(nss_dict.items()):
    print(f"{key}: {val} time/s")
