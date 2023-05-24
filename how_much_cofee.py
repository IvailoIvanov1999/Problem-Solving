cofee = 0
comand=''
while comand != "END":

    comand=input()

    if comand == "coding":
        cofee += 1
    elif comand == "CODING":
        cofee += 2

    elif comand == "dog":
        cofee += 1
    elif comand == "DOG":
        cofee += 2

    elif comand == "cat":
        cofee += 1
    elif comand == "CAT":
        cofee += 2

    elif comand == "movie":
        cofee += 1
    elif comand == "MOVIE":
        cofee += 2


if cofee > 5:
    print("You need extra sleep")
else:
    print(cofee)
