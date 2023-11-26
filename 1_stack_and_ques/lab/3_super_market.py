from _collections import deque


def names(name):
    if name == cmd_end:
        return print(f"{len(names_lst)} people remaining.")
    elif name == cmd_paid:
        for _ in range(len(names_lst)):
            print(names_lst.popleft())
    else:
        names_lst.append(name)


cmd_end = "End"
cmd_paid = "Paid"
names_lst = deque()
name = ""

while name != cmd_end:
    name = input()
    names(name)
