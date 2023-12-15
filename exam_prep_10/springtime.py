def start_spring(**dicts):
    result = []
    nss_dict = dict()

    for k, v in dicts.items():
        if v not in nss_dict.keys():
            nss_dict[v] = []
        nss_dict[v].append(k)

    nss_dict = dict(sorted(nss_dict.items(), key=lambda x: (-len(x[1]), x[0])))

    for k, v in nss_dict.items():
        result.append(f"{k}:")
        for type in sorted(v):
            result.append(f"-{type}")

    return "\n".join(result)


# example_objects = {"Water Lilly": "flower",
#                    "Swifts": "bird",
#                    "Callery Pear": "tree",
#                    "Swallows": "bird",
#                    "Dahlia": "flower",
#                    "Tulip": "flower"}
# print(start_spring(**example_objects))

# example_objects = {"Swallow": "bird",
#                    "Thrushes": "bird",
#                    "Woodpeckers": "bird",
#                    "Swallows": "bird",
#                    "Warblers": "bird",
#                    "Shrikes": "bird", }
# print(start_spring(**example_objects))
#
# example_objects = {"Magnolia": "tree",
#                    "Swallow": "bird",
#                    "Thrushes": "bird",
#                    "Pear": "tree",
#                    "Cherries": "tree",
#                    "Shrikes": "bird",
#                    "Butterfly": "insect"}
# print(start_spring(**example_objects))
