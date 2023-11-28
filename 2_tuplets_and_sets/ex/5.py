def range_func(input_1):
    left, right = input_1.split("-")
    first_range = set(range(int(left.split(",")[0]), int(left.split(",")[1]) + 1))
    second_range = set(range(int(right.split(",")[0]), int(right.split(",")[1]) + 1))
    return first_range.intersection(second_range)


longest_intersection = set()

for i in range(int(input())):
    current_set = range_func(input())

    if len(current_set) > len(longest_intersection):
        longest_intersection = current_set

print(f"Longest intersection is {[x for x in longest_intersection]} with length {len(longest_intersection)}")
