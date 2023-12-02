def concatenate(*args, **kwargs):
    final = "".join(args)

    for k, v in kwargs.items():
        final = final.replace(k, v)

    return final


print(concatenate("Soft", "UNI", "Is", "Grate", "!", UNI="Uni", Grate="Great"))
print(concatenate("I", " ", "Love", " ", "Cythons", C="P", s="", java='Java'))
