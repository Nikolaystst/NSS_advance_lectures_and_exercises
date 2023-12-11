def forecast(*tuples):
    nss_dict = {"Sunny": [], "Cloudy": [], "Rainy": []}
    final = []

    for tuple_1 in tuples:
        nss_dict[tuple_1[1]].append(tuple_1[0])

    for key, val in nss_dict.items():
        for cities in sorted(val):
            final.append(f"{cities} - {key}")

    return "\n".join(final)


# print(forecast(
#     ("Sofia", "Sunny"),
#     ("London", "Cloudy"),
#     ("New York", "Sunny")))
#
# print(forecast(
#     ("Beijing", "Sunny"),
#     ("Hong Kong", "Rainy"),
#     ("Tokyo", "Sunny"),
#     ("Sofia", "Cloudy"),
#     ("Peru", "Sunny"),
#     ("Florence", "Cloudy"),
#     ("Bourgas", "Sunny")))
#
# print(forecast(
#     ("Tokyo", "Rainy"),
#     ("Sofia", "Rainy")))
