def sorting_cheeses(**kwargs):
    sorted_cheeses = sorted(kwargs.items(),key=lambda kvpt: (-len(kvpt[1]),kvpt[0]))
    result = ""
    for elem,quantity in sorted_cheeses:
        result += elem + "\n"
        sortedddd = sorted(quantity,reverse=True)
        result += "\n".join([str(x) for x in sortedddd]) + "\n"

    return result




print(
    sorting_cheeses(
        Parmigiano=[165, 215],
        Feta=[150, 515],
        Brie=[150, 125]
    )
)
