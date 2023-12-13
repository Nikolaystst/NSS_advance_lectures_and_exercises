from collections import deque

filled_boxes = 0

eggs = deque(int(x) for x in input().split(", "))
paper = deque(int(x) for x in input().split(", "))

while eggs and paper:
    cur_egg = eggs.popleft()

    if cur_egg == 13:
        paper_1 = paper.pop()
        paper_2 = paper.popleft()
        paper.appendleft(paper_1)
        paper.append(paper_2)
        continue

    if cur_egg <= 0:
        continue
    cur_pap = paper.pop()

    sum_p_e = cur_pap + cur_egg

    if sum_p_e <= 50:
        filled_boxes += 1

print(f"Great! You filled {filled_boxes} boxes.") if filled_boxes != 0 else print("Sorry! You couldn't fill any boxes!")

print(f"Eggs left: {', '.join(str(x) for x in eggs)}") if eggs else None
print(f"Pieces of paper left: {', '.join(str(x) for x in paper)}") if paper else None
