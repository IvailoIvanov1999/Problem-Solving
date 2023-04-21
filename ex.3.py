path_input = input()

path_input = path_input[::-1]

el_tank_extensions = ""
file_name = ""

cntr_symbol = 0

char_counter = 0

for el in path_input:
    el_tank_extensions += el
    char_counter += 1
    if el == ".":
        break

for f_n in path_input[char_counter:]:
    if f_n == "\\":
        cntr_symbol += 1

        if cntr_symbol >= 1:
            break
    else:
        file_name += f_n

print(f"File name: {file_name[::-1]}")
el_tank_extensions = el_tank_extensions.replace(".","")
print(f"File extension: {el_tank_extensions[::-1]}")
