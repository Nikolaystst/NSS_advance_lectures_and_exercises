from collections import deque

pizzas = deque(int(x) for x in input().split(", "))
pizzas_boys = deque(int(x) for x in input().split(", "))
total_pizza = 0

while pizzas and pizzas_boys:
    cur_piz = pizzas.popleft()
    if cur_piz > 10 or cur_piz <= 0:
        continue

    cur_boy = pizzas_boys.pop()

    if cur_piz > cur_boy:
        cur_piz -= cur_boy
        total_pizza += cur_boy
        pizzas.appendleft(cur_piz)
    elif cur_boy >= cur_piz:
        total_pizza += cur_piz

if not pizzas:
    print("All orders are successfully completed!")
    print(f"Total pizzas made: {total_pizza}")
    print(f"Employees: {', '.join(str(x) for x in pizzas_boys)}") if pizzas_boys else None
else:
    print("Not all orders are completed.")
    print(f"Orders left: {', '.join(str(x) for x in pizzas)}") if pizzas else None
