size = int(input())

def rhombus(n):
    for i in range(size):
        spaces = n - i - 1
        symbol = i + 1
        print(" " * spaces + "* " * symbol)
    for i in range(size -2,-1,-1):
        spaces = n - i - 1
        symbol = i + 1
        print(spaces * " " + "* " * symbol)

rhombus(size)