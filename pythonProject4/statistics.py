comands = input()
products = {}
total_sum_values = 0

while comands != "statistics":

    product_input = comands.split(": ")
    key = product_input[0]
    value = int(product_input[1])

    if key not in products:
        products[key] = value
    else:
        products[key] += value

    total_sum_values += value
    comands = input()

print('Products in stock:')
for key, value in products.items():
    print(f"- {key}: {value}")

print(f"Total Products: {len(products.keys())}")

print(f"Total Quantity: {total_sum_values}")
