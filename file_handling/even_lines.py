file_writing = open('text.txt', 'w')
file_writing.writelines("-I was quick to judge him, but it wasn't his fault.")
file_writing.writelines("\n-Is this some kind of joke?! Is it?")
file_writing.writelines("\n-Quick, hide here. It is safer.")

file_writing.close()

file_reading = open('text.txt', 'r').readlines()

ll = [file_reading[file] for file in range(len(file_reading)) if file % 2 == 0]
filtred_ll = []
for text in ll:
    for character in text:
        if character in ("-", ",", ".", "!", "?"):
            text = text.replace(character, '@')
    filtred_ll.append(text)

for i in range(len(filtred_ll)):
    splited_el = filtred_ll[i].strip().split()
    filtred_ll.pop(i)
    filtred_ll.insert(i,splited_el)

output_ll = []

for item in range(len(filtred_ll)):

    output_ll.append(filtred_ll[item][::-1])

for e in output_ll:
    print(*e)




