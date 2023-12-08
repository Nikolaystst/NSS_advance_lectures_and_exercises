def movie_organizer(*tuples):
    nss_dict = dict()
    final = []

    for tuple_1 in tuples:
        if not tuple_1[1] in nss_dict.keys():
            nss_dict[tuple_1[1]] = []

        nss_dict[tuple_1[1]].append(tuple_1[0])

    nss_dict = dict(sorted(nss_dict.items(), key=lambda x: (-len(x[1]), x[0], x[1])))
    for key, val in nss_dict.items():
        final.append(f"{key} - {len(val)}")
        for movie in sorted(val):
            final.append(f"* {movie}")

    return "\n".join(final)


print(movie_organizer(
    ("Avatar: The Way of Water", "Action"),
    ("House Of Gucci", "Drama"),
    ("Top Gun", "Action"),
    ("Ted", "Comedy"),
    ("Duck Soup", "Comedy"),
    ("The Dark Knight", "Action"),
    ("A Star Is Born", "Musicals"),
    ("The Warrior", "Action"),
    ("Like A Boss", "Comedy"),
    ("The Green Mile", "Drama"),
    ("21 Jump Street", "Comedy")
))

print(movie_organizer(
    ("The Godfather", "Drama"),
    ("The Hangover", "Comedy"),
    ("The Shawshank Redemption", "Drama"),
    ("The Pursuit of Happiness", "Drama"),
    ("The Hangover Part II", "Comedy")))

print(movie_organizer(
    ("The Matrix", "Sci-fi")))
