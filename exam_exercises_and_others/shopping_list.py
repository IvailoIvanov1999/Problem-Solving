def shopping_list(b, **kwargs):
    budget = b
    products_bought_dict = {}
    dict_prod = kwargs

    if budget < 100:
        return "You do not have enough budget."

    output = ''
    counter = len(dict_prod)
    for k, v in dict_prod.items():
        total_price = v[0] * v[1]

        if len(products_bought_dict) >= 5:
            return output

        elif len(products_bought_dict) < 5 and counter <= 0:
            return output

        if budget >= total_price:
            products_bought_dict[k] = total_price
            budget -= total_price
            output += f'You bought {k} for {total_price:.2f} leva.' + "\n"
            counter -= 1

    return output

print(shopping_list(104,
                    cola=(1.20, 2),
                    candies=(0.25, 15),
                    bread=(1.80, 1),
                    pie=(10.50, 5),
                    tomatoes=(4.20, 1),
                    milk=(2.50, 2),
                    juice=(2, 3),
                    eggs=(3, 1),
                    ))
