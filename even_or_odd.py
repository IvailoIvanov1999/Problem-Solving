num=int(input())

for i in range(num):
    n=int(input())
    if n%2!=0:
        print(f"{n} is odd!")
        break
else:
    print("All numbers are even.")



