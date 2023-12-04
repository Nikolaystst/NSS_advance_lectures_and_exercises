import os
import string

dir_name = os.path.dirname(os.path.abspath(__file__))
file_name = os.path.join(dir_name, "text.txt")
output_file = os.path.join(dir_name, "output.txt")

with open(file_name, "r") as file:
    line_1 = file.readlines()

output = open(output_file, "w")

for line in range(len(line_1)):
    count_alpha = 0
    count_symbols = 0
    for symb_1 in line_1[line]:
        if symb_1.isalpha():
            count_alpha += 1
        elif symb_1 in string.punctuation:
            count_symbols += 1

    output.write(f"Line {line + 1}: {line_1[line][:-1]} ({count_alpha})({count_symbols})\n")

output.close()
