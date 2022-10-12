def safe_print_list(my_list=[], x=0):
    length = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end="")
            length += 1
        except IndexError:
            print("")
            return length

    print("")
    return length
