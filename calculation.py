operator = input()
int_1 = int(input())
int_2 = int(input())


def calculation(operator, int_1, int_2):

    if operator == "multiply":
        result = int_1 * int_2
        print(result)
    elif operator == "divide":
        result = int_1 // int_2
        print(result)
    elif operator == "add":
        result = int_1 + int_2
        print(result)
    elif operator == "subtract":
        result = int_1 - int_2
        print(result)



calculation(operator,int_1,int_2)

