def operate(sign, *args):
    result = 0

    def divide(x, *args):
        result = x
        for value in args:
            result /= value
        return result

    def subtract(x,*args):
        result = x
        for values in args:
            result -= values
        return result





    if sign == "+":
        for el in args:
            result += el
        return result
    elif sign == "-":
        return subtract(*args)
    elif sign == "*":
        result = 1
        for el in args:
            result *= el
        return result
    elif sign == "/":
        return divide(*args)






print(operate("*", 3, 4))