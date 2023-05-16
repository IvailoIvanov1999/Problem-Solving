import sys
number=int(input())

maximum_number=-sys.maxsize
minimum_number=sys.maxsize

for num in range (number):
    num=int(input())
    if num > maximum_number:
        maximum_number=num
    if num < minimum_number:
        minimum_number=num

print (f'Max number: {maximum_number}')
print (f'Min number: {minimum_number}')
