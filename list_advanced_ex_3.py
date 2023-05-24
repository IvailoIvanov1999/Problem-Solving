to_do_list = [0] * 10

notes = input()

while notes != "End":
    importance, task = notes.split('-')
    importance = int(importance)
    index = importance - 1
    to_do_list[index] = task
    notes = input()

print([el for el in to_do_list if el!=0])