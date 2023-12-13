def shopping_cart(*tuples):
    nss_dict = {"Pizza": [], "Dessert": [], "Soup": []}
    result = []

    for tuple_123 in tuples:
        if tuple_123 == "Stop":
            break

        if tuple_123[0] == "Soup" and len(nss_dict[tuple_123[0]]) < 3:
            if tuple_123[1] not in nss_dict[tuple_123[0]]:
                nss_dict[tuple_123[0]].append(tuple_123[1])
        elif tuple_123[0] == "Pizza" and len(nss_dict[tuple_123[0]]) < 4:
            if tuple_123[1] not in nss_dict[tuple_123[0]]:
                nss_dict[tuple_123[0]].append(tuple_123[1])
        elif tuple_123[0] == "Dessert" and len(nss_dict[tuple_123[0]]) < 2:
            if tuple_123[1] not in nss_dict[tuple_123[0]]:
                nss_dict[tuple_123[0]].append(tuple_123[1])

    nss_dict = dict(sorted(nss_dict.items(), key=lambda x: (-len(x[1]), x[0])))
    for k, v in nss_dict.items():
        result.append(f"{k}:")
        for product in sorted(v):
            result.append(f" - {product}")

    return "No products in the cart!" if result == ['Dessert:', 'Pizza:', 'Soup:'] else "\n".join(result)


print(shopping_cart(
    ('Pizza', 'ham'),
    ('Soup', 'carrots'),
    ('Pizza', 'cheese'),
    ('Pizza', 'flour'),
    ('Dessert', 'milk'),
    ('Pizza', 'mushrooms'),
    ('Pizza', 'tomatoes'),
    'Stop',
))

print(shopping_cart(
    ('Pizza', 'ham'),
    ('Dessert', 'milk'),
    ('Pizza', 'ham'),
    'Stop',
))

print(shopping_cart(
    'Stop',
    ('Pizza', 'ham'),
    ('Pizza', 'mushrooms'),
))

