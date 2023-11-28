rounds = int(input())
nss_dict = {}

for i in range(rounds):
    command = input().split()
    name = command[0]
    grade = "{:.2f}".format(float(command[1]))
    if name not in nss_dict.keys():
        nss_dict[name] = []
    nss_dict[name].append(grade)


for key, val in nss_dict.items():
    print(f"{key} -> {' '.join(val)} (avg: {sum([float(x) for x in val]) / len(val):.2f})")
