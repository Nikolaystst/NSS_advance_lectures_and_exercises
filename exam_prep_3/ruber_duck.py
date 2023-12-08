from collections import deque

programers_time = deque(int(x) for x in input().split())
task_time = deque(int(x) for x in input().split())

darth = 0
thor = 0
big_blue = 0
small_yellow = 0

while programers_time and task_time:
    current_p_task = programers_time.popleft()
    current_task = task_time.pop()

    total = current_task * current_p_task

    if 0 <= total <= 60:
        darth += 1
    elif 61 <= total <= 120:
        thor += 1
    elif 121 <= total <= 180:
        big_blue += 1
    elif 181 <= total <= 240:
        small_yellow += 1
    else:
        current_task -= 2
        programers_time.append(current_p_task)
        task_time.append(current_task)

print("Congratulations, all tasks have been completed! Rubber ducks rewarded:")
print(f"Darth Vader Ducky: {darth}")
print(f"Thor Ducky: {thor}")
print(f"Big Blue Rubber Ducky: {big_blue}")
print(f"Small Yellow Rubber Ducky: {small_yellow}")
