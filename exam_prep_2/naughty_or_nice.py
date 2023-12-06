def naughty_or_nice_list(lst, *args, **kwargs):
    nice = []
    naughty = []
    final = []

    def kids_location():
        if len(kids) == 1:
            nice.append(kids[0][1]) if kind_of_kid == "Nice" else naughty.append(kids[0][1])
            lst.remove(kids[0])

    for argument in args:
        num = int(argument.split("-")[0])
        kind_of_kid = argument.split("-")[1]
        kids = [tuple_1 for tuple_1 in lst if tuple_1[0] == num]
        kids_location()

    for name, kind_of_kid in kwargs.items():
        kids = [tuple_1 for tuple_1 in lst if tuple_1[1] == name]
        kids_location()

    if nice:
        final.append(f"Nice: {', '.join(nice)}")
    if naughty:
        final.append(f"Naughty: {', '.join(naughty)}")
    if lst:
        final.append(f"Not found: {', '.join([x[1] for x in lst])}")

    return "\n".join(final)


print(naughty_or_nice_list([(3, "Amy"), (1, "Tom"), (7, "George"), (3, "Katy")], "3-Nice", "1-Naughty", Amy="Nice",
                           Katy="Naughty"))

print(naughty_or_nice_list([(7, "Peter"), (1, "Lilly"), (2, "Peter"), (12, "Peter"), (3, "Simon")], "3-Nice",
                           "5-Naughty", "2-Nice", "1-Nice"))

print(naughty_or_nice_list([(6, "John"), (4, "Karen"), (2, "Tim"), (1, "Merry"), (6, "Frank")], "6-Nice", "5-Naughty",
                           "4-Nice", "3-Naughty", "2-Nice", "1-Naughty", Frank="Nice", Merry="Nice", John="Naughty"))
