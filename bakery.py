stocks = input().split()

bakery = {}

for i  in range (0,len(stocks),2):
    key = stocks[i]
    value = stocks[i+1]
    bakery[key]=int(value)

print(bakery)
