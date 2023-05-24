num_as_str = input()





def sum_digits():
    even_sum = 0
    odd_sum = 0
    for i in (num_as_str):
        number = int(i)
        if number % 2 == 0:
            even_sum += number
        else:
            odd_sum += number
    return (f"Odd sum = {odd_sum}, Even sum = {even_sum}")

print(sum_digits())