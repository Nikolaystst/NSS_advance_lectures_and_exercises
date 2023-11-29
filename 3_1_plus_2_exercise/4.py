from _collections import deque

bees = deque(int(x) for x in input().split())
honey = deque(int(x) for x in input().split())
symbols = deque(x for x in input().split())

total_honey = 0
honey_func = {"+": lambda a, b: a + b,
              "-": lambda a, b: a - b,
              "*": lambda a, b: a * b,
              "/": lambda a, b: a / b}

while bees and honey:
    current_bee = bees.popleft()
    current_honey = honey.pop()

    if current_honey > current_bee:
        total_honey += abs(honey_func[symbols.popleft()](current_bee, current_honey))
    elif current_honey < current_bee:
        bees.appendleft(current_bee)

print(f"Total honey made: {total_honey}")

if bees:
    print(f"Bees left: {', '.join(str(x) for x in bees)}")

if honey:
    print(f"Nectar left: {', '.join(str(x) for x in honey)}")
