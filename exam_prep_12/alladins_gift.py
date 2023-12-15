from collections import deque

materials = deque(int(x) for x in input().split())
magic_lvl = deque(int(x) for x in input().split())
nss_dict = dict()
set_1 = {"Gemstone", "Porcelain Sculpture"}
set_2 = {"Gold", "Diamond Jewellery"}

while materials and magic_lvl:
    cur_mat = materials.pop()
    cur_magic = magic_lvl.popleft()

    if cur_mat + cur_magic < 100:
        if (cur_mat + cur_magic) % 2 == 0:
            cur_mat *= 2
            cur_magic *= 3
        else:
            cur_mat *= 2
            cur_magic *= 2

    sum_1 = cur_mat + cur_magic

    if sum_1 >= 500:
        sum_1 /= 2

    if 100 <= sum_1 <= 199:
        if "Gemstone" not in nss_dict.keys():
            nss_dict["Gemstone"] = 0
        nss_dict["Gemstone"] += 1
    elif 200 <= sum_1 <= 299:
        if "Porcelain Sculpture" not in nss_dict.keys():
            nss_dict["Porcelain Sculpture"] = 0
        nss_dict["Porcelain Sculpture"] += 1
    elif 300 <= sum_1 <= 399:
        if "Gold" not in nss_dict.keys():
            nss_dict["Gold"] = 0
        nss_dict["Gold"] += 1
    elif 400 <= sum_1 <= 499:
        if "Diamond Jewellery" not in nss_dict.keys():
            nss_dict["Diamond Jewellery"] = 0
        nss_dict["Diamond Jewellery"] += 1

if set_1.issubset(set(nss_dict.keys())) or set_2.issubset(set(nss_dict.keys())):
    print("The wedding presents are made!")
else:
    print("Aladdin does not have enough wedding presents.")
print(f"Materials left: {', '.join(str(x) for x in materials)}") if materials else None
print(f"Magic left: {', '.join(str(x) for x in magic_lvl)}") if magic_lvl else None

for k, v in sorted(nss_dict.items(), key=lambda x: x[0]):
    print(f"{k}: {v}")
