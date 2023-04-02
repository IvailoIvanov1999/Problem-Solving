n = int(input())
registered = {}

for _ in range(n):
    information = input().split()

    if len(information) == 3:
        for items in information:
            key = information[1]
            value = information[2]


        if key not in registered:
            registered[key] = value
            print(f"{key} registered {value} successfully")
        else:
            print(f"ERROR: already registered with plate number {registered[key]}")

    else:
        for items in information:
            key = information[1]

        if key not in registered.keys():
            print(f"ERROR: user {key} not found")
        else:

            print(f"{key} unregistered successfully")
            registered.pop(key)



for k, v in registered.items():
    print(f"{k} => {registered[k]}")
