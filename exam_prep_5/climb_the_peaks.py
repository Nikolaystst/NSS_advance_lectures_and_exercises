from collections import deque

food_portion = [int(x) for x in input().split(", ")]
stamina = deque(int(x) for x in input().split(", "))
conq_hills = []
hills = [["Kamenitza", 70], ["Polezhan", 60], ["Banski Suhodol", 100], ["Kutelo", 90], ["Vihren", 80]]

while food_portion and stamina:
    cur_f_p = food_portion.pop()
    cur_sta = stamina.popleft()

    if cur_sta + cur_f_p >= hills[-1][1]:
        curent_hill = hills.pop()[0]
        conq_hills.append(curent_hill)
        if not hills:
            print("Alex did it! He climbed all top five Pirin peaks in one week -> @FIVEinAWEEK")
            break

if hills:
    print("Alex failed! He has to organize his journey better next time -> @PIRINWINS")

print("Conquered peaks:") if conq_hills else None
print("\n".join(conq_hills)) if conq_hills else None
