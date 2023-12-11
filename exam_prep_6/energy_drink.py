from collections import deque

mg_caffeine = [int(x) for x in input().split(", ")]
drinks = deque(int(x) for x in input().split(", "))

max_caffeine = 300

while mg_caffeine and drinks:
    cur_caf = mg_caffeine.pop()
    cur_drk = drinks.popleft()

    sum_1 = cur_drk * cur_caf

    if sum_1 <= max_caffeine:
        max_caffeine -= sum_1
    else:
        drinks.append(cur_drk)
        max_caffeine += 30
        if max_caffeine > 300:
            max_caffeine = 300

print(f"Drinks left: {', '.join([str(x) for x in drinks])}") if drinks else print(
    "At least Stamat wasn't exceeding the maximum caffeine.")
print(f"Stamat is going to sleep with {300 - max_caffeine} mg caffeine.")
