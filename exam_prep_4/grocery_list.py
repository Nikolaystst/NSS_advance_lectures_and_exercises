def shop_from_grocery_list(budget, lst_to_buy, *args):
    bought = []
    for i in args:
        if i[0] not in lst_to_buy:
            continue
        elif i[0] in bought:
            continue
        elif budget < i[1]:
            break
        elif budget > 0 and budget >= i[1]:
            bought.append(i[0])
            budget -= i[1]
            lst_to_buy.remove(i[0])

    if not lst_to_buy:
        return f"Shopping is successful. Remaining budget: {budget:.2f}."
    else:
        return f"You did not buy all the products. Missing products: {', '.join(x for x in lst_to_buy)}."


print(shop_from_grocery_list(
    100,
    ["tomato", "cola"],
    ("cola", 5.8),
    ("tomato", 10.0),
    ("tomato", 20.45),
))

print(shop_from_grocery_list(
    100,
    ["tomato", "cola", "chips", "meat"],
    ("cola", 5.8),
    ("tomato", 10.0),
    ("meat", 22),
))

print(shop_from_grocery_list(
    100,
    ["tomato", "cola", "chips", "meat", "chocolate"],
    ("cola", 15.8),
    ("chocolate", 30),
    ("tomato", 15.85),
    ("chips", 50),
    ("meat", 22.99),
))
