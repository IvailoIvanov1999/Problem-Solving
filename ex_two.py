import re

n = int(input())

pattern = r"^(\$|\%)([A-Z][a-z]{2,})\1: \[(\d+)\]\|\[(\d+)\]\|\[(\d+)\]\|$"

patern_digits = r"\d+"

for _ in range(n):

    input_text = input()

    regex = re.findall(pattern, input_text)





    if not regex:
        print("Valid message not found!")
    else:
        open_regex_ready = [el for el in regex[0]]
        open_regex_ready.pop(0)
        open_regex_joined = ",".join(open_regex_ready)

        digits_in_regex = re.findall(patern_digits,open_regex_joined)

        chars_to_print = chr(int(digits_in_regex[0]))+chr(int(digits_in_regex[1]))+chr(int(digits_in_regex[2]))
        print(f"{open_regex_ready[0]}: {chars_to_print}")
