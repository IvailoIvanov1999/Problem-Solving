first_number = int(input())
second_number = int(input())
third_number = int(input())

while True:
    for f in range(2,first_number+1,2):
        for s in range (2,second_number+1):
            for t in range (2,third_number+1,2):
                if s==2 or s==3 or s==5 or s==7:
                    print (f"{f} {s} {t}")
    break


