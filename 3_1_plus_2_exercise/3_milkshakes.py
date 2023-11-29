from _collections import deque

choko = deque(int(x) for x in input().split(", "))
milk = deque(int(x) for x in input().split(", "))
shakes = 0

while shakes != 5 and choko and milk:
    current_choko = choko.pop()
    current_milk = milk.popleft()

    if current_choko <= 0 and current_milk <= 0:
        continue
    elif current_choko <= 0:
        milk.appendleft(current_milk)
        continue
    elif current_milk <= 0:
        choko.append(current_choko)
        continue

    if current_choko == current_milk:
        shakes += 1
    else:
        milk.append(current_milk)
        choko.append(current_choko - 5)

if shakes == 5:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")
print(f"Chocolate: {', '.join(str(x) for x in choko) or 'empty'}")
print(f"Milk: {', '.join(str(x) for x in milk) or 'empty'}")
