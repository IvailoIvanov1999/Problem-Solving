while True:
    products = {}
    command = input().split(": ")

    product = command[0]
    if command[0] == "statistics":
        print(f"Products in stock:")
        for (productss, quantity) in products.items():
            print(f"- {productss}: {quantity}")

        print(f'Total Products: {len(products.keys())}')
        print(f"Total Quantity: {sum(products.values())}")

        break

    value = int(command[1])

    if product not in products:
        products[product] = 0
    products[product] += value
