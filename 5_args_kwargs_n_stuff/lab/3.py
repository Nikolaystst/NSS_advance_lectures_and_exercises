def sorting_cheeses(**kwargs):
    result = []
    sorted_kwargs = sorted(kwargs.items(), key=lambda kv: (-len(kv[1]), kv[0]))
    for key, val in sorted_kwargs:
        result.append(key)
        for i in sorted(val, reverse=True):
            result.append(i)
    return "\n".join([str(x) for x in result])



print(
    sorting_cheeses(
        Parmesan=[102, 120, 135],
        Camembert=[100, 100, 105, 500, 430],
        Mozzarella=[50, 125],
    )
)

print(sorting_cheeses(Parmigiano=[165, 215], Feta=[150, 515], Brie=[150, 125]))
