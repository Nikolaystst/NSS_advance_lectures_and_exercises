def palindrome(word, index):

    if len(word[index:-1 -index]) // 2 == 0:
        return f"{word} is a palindrome"

    if word[0 + index] != word[-1 - index]:
        return f"{word} is not a palindrome"

    return palindrome(word, index + 1)


print(palindrome("abcba", 0))
print(palindrome("peter", 0))
