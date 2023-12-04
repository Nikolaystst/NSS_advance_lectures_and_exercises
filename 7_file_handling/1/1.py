import os

sym = ["-", ",", ".", "!", "?"]
new_sym = "@"

dir_name = os.path.dirname(os.path.abspath(__file__))
file_name = os.path.join(dir_name, "text.txt")

with open(file_name, "r") as file:
    file_inside = file.readlines()

    for i in range(0, len(file_inside), 2):
        for y in sym:
            file_inside[i] = file_inside[i].replace(y, new_sym)

        new_line = file_inside[i].split()[::-1]
        print(" ".join(new_line))
