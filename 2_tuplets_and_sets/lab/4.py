in_set = set()
rounds = int(input())

for i in range(rounds):
    in_out_coming, licence_plate = input().split(", ")
    if in_out_coming == "IN":
        in_set.add(licence_plate)
    elif in_out_coming == "OUT" and licence_plate in in_set:
        in_set.remove(licence_plate)

if in_set:
    print("\n".join(in_set))
else:
    print("Parking Lot is Empty")
