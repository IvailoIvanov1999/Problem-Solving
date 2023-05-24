def factorial(num1, num2):
    num1_result = 1
    num2_result = 1
    result = 1
    for n1 in range(1,num1+1):
        num1_result *= n1
    for n2 in range(1,num2+1):
        num2_result *= n2

    result = num1_result // num2_result
    return result


number_1 = int(input())

number_2 = int(input())

print(f'{factorial(number_1,number_2):.2f}')