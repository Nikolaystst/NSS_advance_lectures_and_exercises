from _collections import deque

nss_deq = deque(input())
open_paranthese = []

while nss_deq:
    curent_symbol = nss_deq.popleft()

    if curent_symbol in "{([":
        open_paranthese.append(curent_symbol)
        continue

    if f"{open_paranthese.pop()}{curent_symbol}" in "{}[]()":
        continue
    elif not open_paranthese:
        print("NO")
        break
    elif f"{open_paranthese.pop()}{curent_symbol}" not in "{}[]()":
        print("NO")
        break


else:
    print("YES")
