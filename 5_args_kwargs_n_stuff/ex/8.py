def age_assignment(*tuple_1, **dict_1):
    result = dict()

    for key, value in dict_1.items():
        for name in tuple_1:
            if name.startswith(key):
                result[name] = value

    result = sorted(result.items(), key=lambda x: x[0])

    return "\n".join(f"{key} is {value} years old." for key, value in result)


print(age_assignment("Peter", "George", G=26, P=19))
print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))
