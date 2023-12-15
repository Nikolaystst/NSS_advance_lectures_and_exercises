from collections import deque


def best_list_pureness(*args):
    deque_1 = deque(args[0])
    deque_2 = deque_1.copy()
    rotations = args[1]
    pureness = -9999999999999999
    rotation = 0
    for i in range(rotations + 1):
        deque_2 = deque_1.copy()
        currnet_pureness = 0
        index = 0
        while deque_2:
            currnet_pureness += deque_2.popleft() * index
            index += 1
        if currnet_pureness > pureness:
            pureness = currnet_pureness
            rotation = i
        deque_1.rotate()

    return f"Best pureness {pureness} after {rotation} rotations"


test = ([4, 3, 2, 6], 4)
result = best_list_pureness(*test)
print(result)
test = ([7, 9, 2, 5, 3, 4], 3)
result = best_list_pureness(*test)
print(result)
test = ([1, 2, 3, 4, 5], 10)
result = best_list_pureness(*test)
print(result)
