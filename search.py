num_of_inputs = int(input())

key_word = input()

list_create = []


for i in range(num_of_inputs):
    input_words = input()

    list_create.append(input_words)

print(list_create)

for el in range(len(list_create) - 1, -1, -1):
    elements = list_create[el]
    if key_word not in elements:
        list_create.remove(elements)


print(list_create)
