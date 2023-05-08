def even_odd_filter(**kwargs):
    dict = {}
    result = ""
    d_sorted = {}
    for key, value in kwargs.items():

        if key == "odd":
            odd_nums = [x for x in value if x % 2 != 0]
            dict[key] = odd_nums
        else:
            even_nums = [x for x in value if x % 2 == 0]
            dict[key] = even_nums
    result = sorted(dict.items(), key=lambda kvpt: -len(kvpt[1]))

    for el in result:
        key_d = el[0]
        value_d = el[1]
        d_sorted[key_d] = value_d



    return d_sorted



print(even_odd_filter(
    odd=[2, 2, 30, 44, 10, 5],
))
