def even_odd(*args):
    num_sss = ""
    command = args[-1]

    if command == "even":
        num_sss = [x for x in args[:(len(args)-1)] if x % 2 == 0]
    else:
        num_sss = [x for x in args[:(len(args)-1)] if x % 2 != 0]


    return num_sss


print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))
