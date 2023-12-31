from _collections import deque

quantity_food = int(input())
orders = deque(int(x) for x in input().split())

print(max(orders))

for order in orders.copy():
    if quantity_food >= order:
        quantity_food -= order
        orders.popleft()
    else:
        print(f"Orders left: {' '.join([str(x) for x in orders])}")
        break
else:
    print("Orders complete")
