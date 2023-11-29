from collections import deque

nss_deq = deque(input().split())
main_colors = ["red", "yellow", "blue"]
secondary_colors = ["orange", "purple", "green"]
two_in_one_colors = {"orange": {"red", "yellow"}, "purple": {"red", "blue"}, "green": {"yellow", "blue"}}
final_colors = []

while nss_deq:
    start_word = nss_deq.popleft() if nss_deq else None
    end_word = nss_deq.pop() if nss_deq else None

    word_1 = start_word + end_word if end_word else start_word
    word_2 = end_word + start_word if end_word else start_word

    if word_1 in main_colors or word_1 in secondary_colors:
        final_colors.append(word_1)
        continue
    elif word_2 in main_colors or word_2 in secondary_colors:
        final_colors.append(word_2)
        continue
    else:
        start_word = start_word[:-1]
        end_word = end_word[:-1] if end_word else None
        nss_deq.insert(int(len(nss_deq) / 2), start_word) if start_word else None
        nss_deq.insert(int(len(nss_deq) / 2), end_word) if end_word else None

for color in set(final_colors).intersection(two_in_one_colors.keys()):
    if not two_in_one_colors[color].issubset(final_colors):
        final_colors.remove(color)

print(final_colors)
