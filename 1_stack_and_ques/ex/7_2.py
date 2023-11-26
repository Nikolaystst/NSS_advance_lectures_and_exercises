from datetime import datetime, timedelta
from _collections import deque

robots_dictionary = {x.split("-")[0]: [int(x.split("-")[1]), 0] for x in input().split(";")}
current_time = datetime.strptime(input(), "%H:%M:%S")
details_list = deque()

while True:
    detail = input()

    if detail == "End":
        break

    details_list.append(detail)

while details_list:
    current_time += timedelta(0, 1)
    current_detail = details_list.popleft()

    robots_dictionary = {x[0]: [x[1][0], x[1][1] - 1] if x[1][1] != 0 else x[1] for x in robots_dictionary.items()}
    free_robots = list(filter(lambda x: x[1][1] == 0, robots_dictionary.items()))

    if not free_robots:
        details_list.append(current_detail)
        continue

    robots_dictionary[free_robots[0][0]][1] = free_robots[0][1][0]
    print(f"{free_robots[0][0]} - {current_detail} [{current_time.strftime('%H:%M:%S')}]")
