n1 = int(input())
n2 = int(input())
symboll = input()

if symboll == "+" or symboll == "-" or symboll == "*":
    if symboll == "+":
        calculation = n1 + n2

    elif symboll == "-":
        calculation = n1 - n2

    elif symboll == "*":
        calculation = n1 * n2

    if (calculation % 2) == 0:
        type = "even"

    elif (calculation % 2) != 0:
        type = "odd"

    print(f"{n1} {symboll} {n2} = {calculation} - {type}")

elif symboll == "/" :
    if n2 == 0:
        print(f"Cannot divide {n1} by zero")

    elif n2!=0 and symboll=="/":
        calculation =n1/ n2
        print(f"{n1} / {n2} = {calculation:.2f}")


elif symboll == "%":
    if n2 == 0:
        print(f"Cannot divide {n1} by zero")
    elif n2 !=0 and symboll=="%":
        calculation = n1 % n2
        print(f"{n1} % {n2} = {calculation}")




