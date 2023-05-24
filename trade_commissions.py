city = input()
sales = float(input())

# logic/code
if not (city== "Sofia" or city == "Varna" or city == "Plovdiv" ):
    print("error")
elif sales<0:
    print("error")


if city == "Sofia":
    if 0 <= sales <= 500:
        final_commission = sales * (5 / 100)
        print(f'{final_commission:.2f}')

    elif 500 < sales <= 1000:
        final_commission = sales * (7 / 100)
        print(f'{final_commission:.2f}')

    elif 1000 < sales <= 10000:
        final_commission = sales * (8 / 100)
        print(f'{final_commission:.2f}')

    elif sales > 10000:
        final_commission = sales * (12 / 100)
        print(f'{final_commission:.2f}')


elif city == "Varna":
    if 0 <= sales <= 500:
        final_commission = sales * (4.5 / 100)
        print(f'{final_commission:.2f}')
    elif 500 < sales <= 1000:
        final_commission = sales * (7.5 / 100)
        print(f'{final_commission:.2f}')
    elif 1000 < sales <= 10000:
        final_commission = sales * (10 / 100)
        print(f'{final_commission:.2f}')
    elif sales > 10000:
        final_commission = sales * (13 / 100)
        print(f'{final_commission:.2f}')

elif city == "Plovdiv":
    final_commission = 0
    if 0 <= sales <= 500:
        final_commission = sales * (5.5 / 100)
        print(f'{final_commission:.2f}')

    elif 500 < sales <= 1000:
        final_commission = sales * (8 / 100)
        print(f'{final_commission:.2f}')

    elif 1000 < sales <= 10000:
        final_commission = sales * (12 / 100)
        print(f'{final_commission:.2f}')

    elif sales > 10000:
        final_commission = sales * (14.5 / 100)
        print(f'{final_commission:.2f}')




