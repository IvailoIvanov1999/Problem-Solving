type = input()

quantity = int(input())


def order(choose, quant):
    result = None
    if type == "coffee":
        result = 1.50 * quantity
    elif type == "coke":
        result = 1.40 * quantity
    elif type == "water":
        result = 1.00 * quantity
    elif type == "snacks":
        result = 2.00 * quantity
    return result

print(f'{order(type,quantity):.2f}')