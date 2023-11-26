from datetime import datetime, timedelta
from _collections import deque

robots_dict = {x.split('-')[0]: [int(x.split('-')[1]), 0] for x in input().split(";")}
time_of_start = datetime.strptime(input(), "%H:%M:%S")
jobs = deque()

while True:
    job = input()

    if job == "End":
        break

    jobs.append(job)

while jobs:
    time_of_start += timedelta(0, 1)
    current_job = jobs.popleft()

    robots_dict = {x[0]: [x[1][0], x[1][1] - 1] if x[1][1] != 0 else x[1] for x in robots_dict.items()}
    free_robots = list(filter(lambda x: x[1][1] == 0, robots_dict.items()))

    if not free_robots:
        jobs.append(current_job)
        continue

    robots_dict[free_robots[0][0]][1] = free_robots[0][1][0]
    print(f"{free_robots[0][0]} - {current_job} [{time_of_start.strftime('%H:%M:%S')}]")
