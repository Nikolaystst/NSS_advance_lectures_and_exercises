def naughty_or_nice_list(lst, *tupples, **dictionaries):
    nice = []
    naughty = []
    not_found = []
    kids_dict = dict()
    result = []
    for tupple_1 in lst:
        if tupple_1[0] not in kids_dict.keys():
            kids_dict[tupple_1[0]] = []
        kids_dict[tupple_1[0]].append(tupple_1[1])
    for tupple_1 in tupples:
        tupple_1 = tupple_1.split("-")
        num = int(tupple_1[0])
        kind = tupple_1[1]
        if num in kids_dict.keys() and len(kids_dict[num]) == 1:
            if kind == "Nice":
                nice.append(*kids_dict[num])
                del kids_dict[num]
            elif kind == "Naughty":
                naughty.append(*kids_dict[num])
                del kids_dict[num]
    name_of_kids = kids_dict.values()
    name_of_kids_2 = []
    for i in name_of_kids:
        for b in i:
            name_of_kids_2.append(b)
    for name, kind in dictionaries.items():
        if name in name_of_kids_2:
            if name_of_kids_2.count(name) == 1:
                if kind == "Nice":
                    nice.append(name)
                    for v in kids_dict.values():
                        if name in v:
                            v.remove(name)
                elif kind == "Naughty":
                    naughty.append(name)
                    for v in kids_dict.values():
                        if name in v:
                            v.remove(name)
    for v in kids_dict.values():
        for b in v:
            not_found.append(b)

    result.append(f"Nice: {', '.join(nice)}") if nice else None
    result.append(f"Naughty: {', '.join(naughty)}") if naughty else None
    result.append(f"Not found: {', '.join(not_found)}") if not_found else None

    return "\n".join(result)


print(naughty_or_nice_list([(3, "Amy"), (1, "Tom"), (7, "George"), (3, "Katy"), ], "3-Nice", "1-Naughty", Amy="Nice",
                           Katy="Naughty", ))

print(naughty_or_nice_list([(7, "Peter"), (1, "Lilly"), (2, "Peter"), (12, "Peter"), (3, "Simon"), ], "3-Nice",
                           "5-Naughty", "2-Nice", "1-Nice", ))

print(naughty_or_nice_list([(6, "John"), (4, "Karen"), (2, "Tim"), (1, "Merry"), (6, "Frank"), ], "6-Nice", "5-Naughty",
                           "4-Nice", "3-Naughty", "2-Nice", "1-Naughty", Frank="Nice", Merry="Nice", John="Naughty", ))
