def loading_bar(num):
    loading = ''
    dots = ''
    counter = 0
    for _ in range(num // 10):
        loading += "%"
        counter += 1
    for _ in range(10 - counter):
        dots += "."

    if number == 100:
        print(f"{number}% Complete!")
        print(f"[{loading}]")
    else:
        print(f"{number}% [{loading}{dots}]")
        print("Still loading...")


number = int(input())
times = 100 - number

loading_bar(number)
