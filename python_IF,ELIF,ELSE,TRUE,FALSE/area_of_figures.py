import math

figure = input()

if figure == "square":
    a = float(input())
    square_face = a * a
    print(f"{square_face:.3f}")

elif figure == "rectangle":
    a=float(input())
    b=float(input())
    rectangle_face=a * b
    print(f"{rectangle_face:.3f}")

elif figure == "circle":
    radius=float(input())
    circle_face=math.pi*(radius*radius)
    print(f"{circle_face:.3f}")

elif figure == "triangle":
    a=float(input())
    h_a=float(input())
    triangle_face=(a*h_a) / 2
    print(f"{triangle_face:.3f}")


