nss_lst = [int(x) for x in input().split()]
target_num = int(input())

targets = set()
val_dict = {}

for b in nss_lst:
    if b in targets:
        targets.remove(b)
        pair = val_dict[b]
        del val_dict[b]
        print(f"{pair} + {b} = {target_num}")
    else:
        final_num = target_num - b
        targets.add(final_num)
        val_dict[final_num] = b
