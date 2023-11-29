from functools import reduce

nss_lst = [x for x in input().split()]
idx = 0

funcs_map = {
    "+": lambda x: reduce(lambda a, b: int(a) + int(b), nss_lst[:x]),
    "-": lambda x: reduce(lambda a, b: int(a) - int(b), nss_lst[:x]),
    "*": lambda x: reduce(lambda a, b: int(a) * int(b), nss_lst[:x]),
    "/": lambda x: reduce(lambda a, b: int(a) / int(b), nss_lst[:x])
}

while idx < len(nss_lst):
    current_symbol = nss_lst[idx]

    if current_symbol in "+-*/":
        what_to_insert = funcs_map[current_symbol](idx)
        nss_lst = nss_lst[idx + 1:]
        nss_lst.insert(0, int(what_to_insert))
        idx = 0

    idx += 1

print(*nss_lst)
