def potato_hot_game(lst):
    the_step_of_pop = int(input())
    counter = the_step_of_pop

    while lst:
        if len(lst) == 1:
            print(f"Last is {lst[0]}")
            break
        the_step_of_pop = (the_step_of_pop % len(lst)) - 1
        print(f"Removed {lst[the_step_of_pop]}")
        lst.pop(the_step_of_pop)
        if the_step_of_pop == -1:
            the_step_of_pop += 1
        the_step_of_pop += counter


kids_list = input().split()
potato_hot_game(kids_list)
