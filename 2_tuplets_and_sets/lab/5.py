rounds = int(input())
all_party = set()
coming_party = set()
not_coming_party = set()

for i in range(rounds):
    all_party.add(input())

while True:
    command = input()
    if command == "END":
        break
    coming_party.add(command)

not_coming_party = all_party.difference(coming_party)
print(len(not_coming_party))
print("\n".join(sorted(not_coming_party)))
