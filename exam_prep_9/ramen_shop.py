from collections import deque

bow_ramen = deque(int(x) for x in input().split(", "))
customers = deque(int(x) for x in input().split(", "))

while bow_ramen and customers:
    cur_bow = bow_ramen.pop()
    cur_cust = customers.popleft()

    if cur_bow == cur_cust:
        continue
    elif cur_bow > cur_cust:
        cur_bow -= cur_cust
        bow_ramen.append(cur_bow)
    elif cur_bow < cur_cust:
        cur_cust -= cur_bow
        customers.appendleft(cur_cust)

if not customers:
    print("Great job! You served all the customers.")
    print(f"Bowls of ramen left: {', '.join(str(x) for x in bow_ramen)}") if bow_ramen else None
else:
    print("Out of ramen! You didn't manage to serve all customers.")
    print(f"Customers left: {', '.join(str(x) for x in customers)}")
