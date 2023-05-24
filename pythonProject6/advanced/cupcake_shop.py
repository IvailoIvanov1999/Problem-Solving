def stock_availability(inventory, sell_or_delivery, *args):
    new_ll = []
    if sell_or_delivery == "delivery":
        for el in args:
            inventory.append(el)
        new_ll = inventory

    elif sell_or_delivery == "sell":
        if not args:
            inventory.pop(0)
            new_ll = inventory

        else:
            for el in args:
                if el in (0, 1, 2, 3, 4, 5, 6, 7, 8, 9):
                    el = int(el)
                    for i in range(el):
                        inventory.pop(0)
                    new_ll = inventory
                else:
                    inventory = [x for x in inventory if x != el]
                    new_ll = inventory
    return new_ll


print(stock_availability(["choco", "vanilla", "banana"], "delivery", "caramel", "berry"))
print(stock_availability(["chocolate", "vanilla", "banana"], "delivery", "cookie", "banana"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", 3))
print(stock_availability(["chocolate", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["cookie", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", "cookie"))
