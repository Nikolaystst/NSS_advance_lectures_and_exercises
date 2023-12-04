import os

dir_name = os.path.dirname(os.path.abspath(__file__))

while True:
    command = input().split("-")

    if command[0] == "End":
        break

    elif command[0] == "Create":
        with open(os.path.join(dir_name, command[1]), "w") as file:
            pass

    elif command[0] == "Add":
        with open(os.path.join(dir_name, command[1]), "a") as file:
            file.write(f"{command[2]}\n")

    elif command[0] == "Replace":
        try:
            with open(os.path.join(dir_name, command[1]), "r+") as file:
                curent_file = file.read()
                line = curent_file.replace(command[2], command[3])
                file.seek(0)
                file.write(line)
        except FileNotFoundError:
            print("An error occurred")

    elif command[0] == "Delete":
        try:
            os.remove(os.path.join(dir_name, command[1]))
        except FileNotFoundError:
            print("An error occurred")
