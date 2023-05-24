texxt=input()

# a=1
# e=2
# i=3
# o=4
# u=5
counter=0

for letter in texxt:
    if letter=="a":
        counter+=1
    elif letter=="e":
        counter+=2
    elif letter=="i":
        counter+=3
    elif letter=="o":
        counter+=4
    elif letter=="u":
        counter+=5

print(f"{counter}")


