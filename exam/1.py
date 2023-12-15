from collections import deque

tools = deque(int(x) for x in input().split())
substances = deque(int(x) for x in input().split())
challange = [int(x) for x in input().split()]

while tools and substances and challange:
    current_tool = tools.popleft()
    current_substances = substances.pop()

    result = current_tool * current_substances

    if result in challange:
        challange.remove(result)
        continue
    elif result not in challange:
        current_tool += 1
        tools.append(current_tool)
        current_substances -= 1
        if current_substances == 0:
            continue
        else:
            substances.append(current_substances)

if not tools or not substances:
    if challange:
        print("Harry is lost in the temple. Oblivion awaits him.")

if not challange:
    print("Harry found an ostracon, which is dated to the 6th century BCE.")

print(f"Tools: {', '.join(str(x) for x in tools)}") if tools else None
print(f"Substances: {', '.join(str(x) for x in substances)}") if substances else None
print(f"Challenges: {', '.join(str(x) for x in challange)}") if challange else None
