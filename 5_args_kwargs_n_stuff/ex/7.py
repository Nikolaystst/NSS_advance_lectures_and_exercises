def grocery_store(**dicts):
    result = sorted(dicts.items(), key=lambda k: (-k[1], -len(k[0]), k[0]))
    return "\n".join([f"{x}: {y}" for x, y in result])


print(grocery_store(bread=5, pasta=12, eggs=12, ))
print(grocery_store(bread=2, pasta=2, eggs=20, carrot=1, ))
