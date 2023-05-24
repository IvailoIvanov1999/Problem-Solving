number= int (input())
counter=1
bigger_than_mynumber=False

while True:
    for r in range (1,number+1):
        for n in range (1, r+1):

            if counter > number:
                    bigger_than_mynumber = True
                    break
            print(str(counter)+ " ", end='')
            counter+=1
        if bigger_than_mynumber:
            break
        print()



