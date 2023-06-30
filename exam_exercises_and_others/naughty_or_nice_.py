def naughty_or_nice_list(ll, *args, **kwargs):
    counter = 0
    ll_from_args = []
    dict_digits = {}
    dict_kids = {"Naughty": [], "Nice": []}
    dict_check_how_many_times = {}
    for item in args:
        ll_from_args.append(item)
    for elem in ll:
        n = elem[0]
        if n not in dict_digits:
            dict_digits[n] = 0
        dict_digits[n] += 1
    for lists in ll_from_args:
        splited_lists = lists.split('-')
        n = int(splited_lists[0])
        which = splited_lists[1]
        if n in dict_digits:
            if dict_digits[n] == 1:
                for element in ll:
                    if element[0] == 1:
                        dict_kids[which].append(element[1])
                        ll.remove(element)

    print(ll)
    print(dict_kids)
    for tpl in ll:
        name = tpl[1]
        if name not in dict_check_how_many_times:
            dict_check_how_many_times[name] = 0
        dict_check_how_many_times[name] += 1





print(naughty_or_nice_list(
    [
        (3, "Amy"),
        (1, "Tom"),
        (7, "George"),
        (3, "Katy"),
    ],
    "3-Nice",
    "1-Naughty",
    Amy="Nice",
    Katy="Naughty",
))
