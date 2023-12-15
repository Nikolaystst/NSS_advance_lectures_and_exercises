def shopping_list(budget, **dict_1):
    final = []
    product = 0
    if budget < 100:
        return "You do not have enough budget."

    for k, v in dict_1.items():
        if product == 5:
            break

        if budget >= v[0] * v[1]:
            final.append(f"You bought {k} for {v[0] * v[1]:.2f} leva.")
            product += 1
            budget -= v[0] * v[1]

    return "\n".join(final)


print(shopping_list(100,
                    microwave=(70, 2),
                    skirts=(15, 4),
                    coffee=(1.50, 10),
                    ))

print(shopping_list(20,
                    jeans=(19.99, 1),
                    ))

print(shopping_list(104,
                    cola=(1.20, 2),
                    candies=(0.25, 15),
                    bread=(1.80, 1),
                    pie=(10.50, 5),
                    tomatoes=(4.20, 1),
                    milk=(2.50, 2),
                    juice=(2, 3),
                    eggs=(3, 1),
                    ))
