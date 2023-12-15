from collections import deque

fireworks = deque(int(x) for x in input().split(", "))
explosive_power = deque(int(x) for x in input().split(", "))
cross = 0
palm = 0
willow = 0
flag = False

while fireworks and explosive_power:

    cur_fire = fireworks.popleft()
    cur_explosion = explosive_power.pop()

    if cur_fire <= 0:
        explosive_power.append(cur_explosion)
        continue
    elif cur_explosion <= 0:
        fireworks.appendleft(cur_fire)
        continue

    sum_1 = cur_fire + cur_explosion

    if sum_1 % 3 == 0 and sum_1 % 5 == 0:
        cross += 1
    elif sum_1 % 3 == 0:
        palm += 1
    elif sum_1 % 5 == 0:
        willow += 1
    else:
        cur_fire -= 1
        fireworks.append(cur_fire)
        explosive_power.append(cur_explosion)

    if cross >= 3 and palm >= 3 and willow >= 3:
        flag = True
        break

if flag:
    print("Congrats! You made the perfect firework show!")
elif not flag:
    print("Sorry. You can't make the perfect firework show.")

print(f"Firework Effects left: {', '.join(str(x) for x in fireworks)}") if fireworks else None
print(f"Explosive Power left: {', '.join(str(x) for x in explosive_power)}") if explosive_power else None
print(f"Palm Fireworks: {palm}")
print(f"Willow Fireworks: {willow}")
print(f"Crossette Fireworks: {cross}")
