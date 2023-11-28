nss_tuple = tuple("{:.1f}".format(float(x)) for x in input().split())
nss_dict = {x: nss_tuple.count(x) for x in nss_tuple}

for key, val in nss_dict.items():
    print(f"{key} - {val} times")
