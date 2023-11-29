set_1 = set(int(x) for x in input().split())
set_2 = set(int(x) for x in input().split())

funct_lambda = {
    "Add First": lambda x: [set_1.add(i) for i in x],
    "Add Second": lambda x: [set_2.add(i) for i in x],
    "Remove First": lambda x: [set_1.discard(i) for i in x],
    "Remove Second": lambda x: [set_2.discard(i) for i in x],
    "Check Subset": lambda: print(True) if set_1.issubset(set_2) or set_2.issubset(set_1) else print(False),
}

for _ in range(int(input())):
    given_command = input().split()
    to_do = given_command[0] + " " + given_command[1]
    lst = [int(x) for x in given_command[2:]] if len(given_command) > 2 else None
    funct_lambda[to_do](lst) if lst else funct_lambda[to_do]()

print(*sorted(set_1), sep=", ")
print(*sorted(set_2), sep=", ")
