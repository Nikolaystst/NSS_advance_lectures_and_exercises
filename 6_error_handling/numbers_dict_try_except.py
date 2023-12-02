numbers_dictionary = {}
flag = True

while True:
    number_as_string = input()

    if number_as_string == "Search":
        break

    try:
        number = int(input())
        numbers_dictionary[number_as_string] = number
    except ValueError:
        print("The variable number must be an integer")

while flag:
    searched = input()

    if searched == "Remove":
        while flag:
            searched = input()

            if searched == "End":
                flag = False
                break

            try:
                del numbers_dictionary[searched]
            except KeyError:
                print("Number does not exist in dictionary")

    if not flag:
        break

    print(numbers_dictionary[searched]) if numbers_dictionary.get(searched) else print(
        "Number does not exist in dictionary")

print(numbers_dictionary)

# one
# 1
# two
# 2
# Search
# one
# Remove
# two
# End


# one
# two
# Search
# Remove
# End


# one
# 1
# Search
# one
# Remove
# two
# End
