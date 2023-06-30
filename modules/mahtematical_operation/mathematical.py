def divide(num_1, num_2):
    num_1 = float(num_1)
    num_2 = int(num_2)
    result = num_1 / num_2
    return result


def multiply(num_1, num_2):
    num_1 = float(num_1)
    num_2 = int(num_2)
    result = num_1 * num_2
    return result


def substract(num_1, num_2):
    num_1 = float(num_1)
    num_2 = int(num_2)
    result = num_1 - num_2
    return result


def add(num_1, num_2):
    num_1 = float(num_1)
    num_2 = int(num_2)
    result = num_1 + num_2
    return result


def raising(num_1, num_2):
    num_1 = float(num_1)
    num_2 = int(num_2)
    result = num_1 ** num_2
    return result


dict_methods = {
    '/': divide,
    '*': multiply,
    '-': substract,
    '+': add,
    '^': raising
}


def result_calculation(expression):
    num_1, sign, num_2 = expression

    try:
        result = dict_methods[sign](num_1, num_2)
        return f'{result:.2f}'
    except KeyError:
        return "Invalid operator!!!"
