import os


def whats_inside_dir(dir_name, lvl=0):
    for files in os.listdir(dir_name):
        file = os.path.join(dir_name, files)

        if os.path.isfile(file):
            end_1 = file.split(".")[-1]

            if end_1 not in directory_name_dict.keys():
                directory_name_dict[end_1] = []

            directory_name_dict[end_1].append(file.split("\\")[-1])  # for windows

            # directory_name_dict[end_1].append(file.split("//")[-1])
            # other OS

        elif os.path.isdir(file) and lvl == 0:
            whats_inside_dir(file, lvl=1)


directory_name = os.path.dirname(os.path.abspath(__file__))
directory_name_dict = dict()
whats_inside_dir(directory_name)

with open(os.path.join(directory_name, "report.txt"), "w") as final_file:
    for key in sorted(directory_name_dict.keys()):
        final_file.write(f".{key}\n")
        for vals in sorted(directory_name_dict[key]):
            final_file.write(f"- - - {vals}\n")
