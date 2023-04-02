import re
output = ""
pairs_found = []
mirror_words = []
counter = 0
string_input = input()

pattern = re.compile(r"(@|#)([A-Za-z]{3,})\1\1([A-Za-z]{3,})\1")

# regex = re.search(pattern,string_input)

for match in pattern.finditer(string_input, ):

    first_word = match.group(2)
    second_word = match.group(3)

    if match:
        counter += 1

        pairs_found.append(first_word)
        pairs_found.append(second_word)

if len(pairs_found) == 0:
    print("No word pairs found!")
else:
    print(f"{counter} word pairs found!")

for el_index in range(0,len(pairs_found),2):
    f_w = pairs_found[el_index]
    s_w = pairs_found[el_index+1]
    if f_w == s_w[::-1]:
        mirror_words.append(f_w)
        mirror_words.append(s_w)

if len(mirror_words) == 0:
    print("No mirror words!")
else:
    print("The mirror words are:")

    for i in range(0,len(mirror_words),2):

        output += (f"{mirror_words[i]} <=> {mirror_words[i+1]}, ")



print(output[:-2])





