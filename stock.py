products = input().split()

in_stock = {}

searching_products = input().split()

for i in range(0, len(products), 2):
    key = products[i]
    value = products[i + 1]
    in_stock[key] = value
for product in searching_products:

    if product in in_stock:
        print(f"We have {in_stock[product]} of {product} left")

    else:
        print(f"Sorry, we don't have {product}")


