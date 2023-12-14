def words_sorting(*args):
    word_dict = dict()
    for word in args:
        word_dict[word] = sum(ord(i) for i in word)

    if sum(word_dict.values()) % 2 == 1:
        return "\n".join(f"{k} - {v}" for k, v in sorted(word_dict.items(), key=lambda x: -x[1]))
    else:
        return "\n".join(f"{k} - {v}" for k, v in sorted(word_dict.items(), key=lambda x: x[0]))


print(words_sorting('escape', 'charm', 'mythology'))
print(words_sorting('escape', 'charm', 'eye'))
print(words_sorting('cacophony', 'accolade'))
