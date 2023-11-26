from _collections import deque

green_light = int(input())
free_window = int(input())
cars = deque()
counter = 0

while True:
    command = input()

    if command == "END":
        break
    elif command == "green":
        full_window = green_light + free_window
        while cars:
            if full_window <= free_window:
                break
            current_car = cars.popleft()
            counter += 1
            for i in current_car:
                full_window -= 1
                if full_window < 0:
                    print(f"A crash happened!\n{current_car} was hit at {i}.")
                    exit()

        continue
    else:
        cars.append(command)

print(f"Everyone is safe.\n{counter} total cars passed the crossroads.")
