projection_type = input()
rows = int(input())
columns = int(input())

# Premiere= 12.00lv
# Normal=7.50lv
# Discount=5.00lv

# code/logic
if projection_type == "Premiere":
    total_price = rows * columns * 12.00
    print(f'{total_price:.2f}' " leva")
if projection_type=="Normal":
    total_price=rows*columns*7.50
    print(f'{total_price:.2f}' " leva")
if projection_type=="Discount":
    total_price=rows*columns*5
    print(f'{total_price:.2f}' " leva")
