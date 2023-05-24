def start_spring(**kwargs):
    new_dict = {}
    for k, v in kwargs.items():
        if v not in new_dict:
            new_dict[v] = []

        new_dict[v].append(k)

    new_dict = sorted(new_dict.items(), key=lambda kvpt: (-len(kvpt[1]), kvpt[0]))

    final_sorting = {}

    to_print = ""

    for item in new_dict:
        key = item[0]
        value = sorted(item[1])
        final_sorting[key] = value

    for ke,va in final_sorting.items():
        to_print += f"{ke}:\n-"
        to_print += '\n-'.join(va) + "\n"

    return to_print

example_objects = {"Swallow": "bird",
                   "Thrushes": "bird",
                   "Woodpeckers": "bird",
                   "Swallows": "bird",
                   "Warblers": "bird",
                   "Shrikes": "bird",}
print(start_spring(**example_objects))
