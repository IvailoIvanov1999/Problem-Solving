def list_manipulator(ll_number, *args):
    ll = ll_number
    numbers_from_argss = list(args[2:])

    if args[0] == "add":
        if args[1] == "beginning":
            while numbers_from_argss:
                for i in range(len(numbers_from_argss)):
                    ll.insert(i, numbers_from_argss.pop(0))




        elif args[1] == "end":
            while numbers_from_argss:

                ll.append(numbers_from_argss.pop(0))



    elif args[0] == "remove":
        if args[1] == "beginning":
            if len(numbers_from_argss) >= 1:
                for items in range(numbers_from_argss[0]):
                    ll.pop(0)
            else:
                ll.pop(0)



        elif args[1] == "end":
            if len(numbers_from_argss) >= 1:
                for items in range(numbers_from_argss[0]):
                    ll.pop(-1)
            else:
                ll.pop()

    return ll



print(list_manipulator([1, 2, 3], "add", "beginning", 20, 30, 40))

