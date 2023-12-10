from collections import deque

textiles = deque(int(x) for x in input().split())
medicaments = [int(x) for x in input().split()]
nss_dict = {"Patch": 0, "Bandage": 0, "MedKit": 0}

while textiles and medicaments:
    current_textile = textiles.popleft()
    current_med = medicaments.pop()

    if current_med + current_textile == 30:
        nss_dict["Patch"] += 1
    elif current_med + current_textile == 40:
        nss_dict["Bandage"] += 1
    elif current_med + current_textile == 100:
        nss_dict["MedKit"] += 1
    elif current_med + current_textile > 100:
        nss_dict["MedKit"] += 1
        next_med = medicaments.pop()
        next_med += current_med + current_textile - 100
        medicaments.append(next_med)
    else:
        current_med += 10
        medicaments.append(current_med)

print("Textiles are empty.") if not textiles and medicaments else None
print("Medicaments are empty.") if not medicaments and textiles else None
print("Textiles and medicaments are both empty.") if not textiles and not medicaments else None

for key, val in sorted(nss_dict.items(), key=lambda x: (-x[1], x[0])):
    print(f"{key} - {val}") if val else None

print(f"Medicaments left: {', '.join(str(x) for x in medicaments[::-1])}") if medicaments else None
print(f"Textiles left: {', '.join(str(x) for x in textiles)}") if textiles else None
