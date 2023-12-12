from collections import deque

seats = input().split(", ")
nums_1 = deque(input().split(", "))
nums_2 = deque(input().split(", "))
seat_that_matches = []

rotations = 0
matches = 0

while rotations < 10:
    rotations += 1
    cur_n_1 = nums_1.popleft()
    cur_n_2 = nums_2.pop()

    char_to_search = chr(int(cur_n_1) + int(cur_n_2))

    cur_sym_to_search_1 = cur_n_1 + char_to_search
    cur_sym_to_search_2 = cur_n_2 + char_to_search
    if cur_sym_to_search_1 in seats:
        seat_that_matches.append(cur_sym_to_search_1)
        seats.remove(cur_sym_to_search_1)
        matches += 1
        if matches == 3:
            break
    elif cur_sym_to_search_2 in seats:
        seat_that_matches.append(cur_sym_to_search_2)
        seats.remove(cur_sym_to_search_2)
        matches += 1
        if matches == 3:
            break
    elif cur_sym_to_search_1 in seat_that_matches:
        continue
    elif cur_sym_to_search_2 in seat_that_matches:
        continue
    else:
        nums_1.append(cur_n_1)
        nums_2.appendleft(cur_n_2)

print(f"Seat matches: {', '.join(seat_that_matches)}")
print(f"Rotations count: {rotations}")
