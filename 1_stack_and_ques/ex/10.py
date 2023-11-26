from _collections import deque

cups_capacity = deque(int(x) for x in input().split())
bottles_capacity = deque(int(x) for x in input().split())
wasted_water = 0
raise_1 = False

while True:
    if not cups_capacity:
        print(f"Bottles: {' '.join([str(x) for x in bottles_capacity])}")
        break
    elif not bottles_capacity:
        print(f"Cups: {' '.join([str(x) for x in cups_capacity])}")
        break

    if not raise_1:
        current_cup = cups_capacity.popleft()
    current_bottle = bottles_capacity.pop()

    if current_bottle > current_cup:
        wasted_water += (current_bottle - current_cup)
        raise_1 = False
    elif current_bottle < current_cup:
        current_cup -= current_bottle
        raise_1 = True
    else:
        raise_1 = False
        continue

print(f"Wasted litters of water: {wasted_water}")
