def shop_from_grocery_list(b,gr,*args):

    budget = int(b)
    ll_grocery = gr
    products_dict = {}
    stop = False
    for el in args:
        product_name = el[0]
        product_price = el[1]
        if product_name not in products_dict:
            if product_name in ll_grocery:
                if budget >= product_price:
                    budget -= product_price
                    products_dict[product_name] = product_price
                else:
                    stop = True
                    break
        if stop:
            break
    for k in products_dict:
        if k in ll_grocery:
            ll_grocery.remove(k)

    if not ll_grocery:
        return f"Shopping is successful. Remaining budget: {budget:.2f}."
    else:
        return f"You did not buy all the products. Missing products: {', '.join(ll_grocery)}."







print(shop_from_grocery_list(
    100,
    ["tomato", "cola", "chips", "meat", "chocolate"],
    ("cola", 15.8),
    ("chocolate", 30),
    ("tomato", 15.85),
    ("chips", 50),
    ("meat", 22.99),
))


