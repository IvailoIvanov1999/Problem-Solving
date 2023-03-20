number = int(input())



for digits in range(1, number + 1):
    num_as_string = str(digits)
    calculator_num = 0
    flag = False

    #Calculation sum of digits

    for char in num_as_string:
        calculator_num += int(char)

    if calculator_num == 5 or calculator_num == 7 or calculator_num == 11:
        flag = True

    print(f'{digits} -> {flag}')
