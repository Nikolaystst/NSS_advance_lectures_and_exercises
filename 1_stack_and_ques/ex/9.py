from _collections import deque
shot_cost = int(input())
magazine_size = int(input())
current_mag_size = magazine_size
bullets = [int(x) for x in input().split()]
locks = deque(int(x) for x in input().split())
money = int(input())

for i in range(len(bullets.copy())):
    current_bullet = bullets.pop()
    money -= shot_cost
    if current_bullet <= locks.copy().popleft():
        locks.popleft()
        print("Bang!")
        if not locks:
            current_mag_size -= 1
            if current_mag_size == 0 and bullets:
                print("Reloading!")
                current_mag_size = magazine_size
            print(f"{len(bullets)} bullets left. Earned ${money}")
            exit()
    else:
        print("Ping!")
    current_mag_size -= 1
    if not bullets:
        break
    if current_mag_size == 0:
        print("Reloading!")
        current_mag_size = magazine_size

print(f"Couldn't get through. Locks left: {len(locks)}")
