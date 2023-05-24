number_input = [int(x) for x in input().split()]

even_num_list = []

even_list=[]
def even_numbers(x):
    if x % 2 == 0:
        return True



final_evens = filter(even_numbers, number_input)
for n in final_evens:

    even_list.append(n)
print(even_list)
