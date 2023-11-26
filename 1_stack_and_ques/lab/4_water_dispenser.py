from _collections import deque
total_lt = int(input())
names_lst = deque()

name = input()
while name != "Start":
    names_lst.append(name)
    name = input()

while True:
    command = input()
    if command == "End":
        break
    elif command.isdigit():
        command = int(command)
        if command <= total_lt:
            total_lt -= command
            print(f"{names_lst.popleft()} got water")
        else:
            print(f"{names_lst.popleft()} must wait")
    elif command.startswith("refill"):
        command = command.split()
        total_lt += int(command[1])

print(f"{total_lt} liters left")
