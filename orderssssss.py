order_dict = {}
flag = False

while True:
    if flag:
        break
    data = input().split()

    for i in range(0, len(data), 3):

        key = data[i]
        if key == "buy":
            flag = True
            break
        value = float(data[i + 1])
        quantity = float(data[i + 2])

        if key not in order_dict:
            order_dict[key] = [value, quantity]
        else:
            order_dict[key][1] += quantity
            if value != order_dict[key][0]:
                order_dict[key][0] = value

for k, v in order_dict.items():

    for p in range(0, len(v), 2):
        price = v[p]
        quan = v[p + 1]
        result = price * quan

    print(f'{k} -> {result:.2f}')
