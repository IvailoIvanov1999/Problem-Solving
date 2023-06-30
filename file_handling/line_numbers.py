with open('text.txt', 'r') as file:
    file = file.readlines()

new_file = open('output.txt', 'w')
counter_lines = 0
for f in file:

    counter_letters = 0
    counter_punctuation_marks = 0
    counter_lines += 1
    if '\n' in f:
        f=f.replace('\n','')
    for ch in f:
        if ch.isalpha():
            counter_letters += 1
        elif ch in ("-", ",", ".", "!", "?","'"):
            counter_punctuation_marks += 1
    new_file.writelines(f"Line {counter_lines}: {f} ({counter_letters})({counter_punctuation_marks})\n")
