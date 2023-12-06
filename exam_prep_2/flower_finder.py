from collections import deque

words = {"rose": "rose", "tulip": "tulip", "lotus": "lotus", "daffodil": "daffodil"}

vowels = deque(input().split())
consonant = deque(input().split())
flag = False

while vowels and consonant:
    vow = vowels.popleft()
    cons = consonant.pop()

    for word in words.keys():
        words[word] = words[word].replace(vow, "")
        words[word] = words[word].replace(cons, "")

        if not words[word]:
            print(f"Word found: {word}")
            flag = True
            break

    if flag:
        break

if not flag:
    print("Cannot find any word!")

print(f"Vowels left: {' '.join(x for x in vowels)}") if vowels else None
print(f"Consonants left: {' '.join(x for x in consonant)}") if consonant else None
