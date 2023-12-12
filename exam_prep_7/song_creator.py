def add_songs(*args):
    nss_dict = dict()
    final_return = []

    for tupple_1 in args:
        if tupple_1[0] not in nss_dict:
            nss_dict[tupple_1[0]] = []
        if tupple_1[1]:
            for word in tupple_1[1]:
                nss_dict[tupple_1[0]].append(word)

    for k, v in nss_dict.items():
        final_return.append(f"- {k}")
        for lines in v:
            final_return.append(lines)

    return "\n".join(final_return)

# print(add_songs(
#     ("Bohemian Rhapsody", []),
#     ("Just in Time",
#      ["Just in time, I found you just in time",
#       "Before you came, my time was running low",
#       "I was lost, the losing dice were tossed",
#       "My bridges all were crossed, nowhere to go"])
# ))

# print(add_songs(
#     ("Beat It", []),
#     ("Beat It",
#      ["Just beat it (beat it), beat it (beat it)",
#       "No one wants to be defeated"]),
#     ("Beat It", []),
#     ("Beat It",
#      ["Showin' how funky and strong is your fight",
#       "It doesn't matter who's wrong or right"]),
# ))

# print(add_songs(
#     ("Love of my life",
#      ["Love of my life, you've hurt me",
#       "You've broken my heart, and now you leave me",
#       "Love of my life, can't you see?",
#       "Bring it back, bring it back"]),
#     ("Beat It", []),
#     ("Love of my life",
#      ["Don't take it away from me",
#       "Because you don't know",
#       "What it means to me"]),
#     ("Dream On",
#      ["Every time that I look in the mirror"]),
# ))
