trip_price = float(input())
number_of_puzzles = int(input())
number_barbies = int(input())
number_of_teddy_bears = int(input())
number_of_minions = int(input())
number_of_trucks = int(input())

total_toys_count = number_of_puzzles + number_barbies + number_of_teddy_bears + number_of_minions + number_of_trucks
total = number_of_puzzles * 2.60
total += number_barbies * 3
total += number_of_teddy_bears * 4.10
total += number_of_minions * 8.20
total += number_of_trucks * 2

if total_toys_count >= 50:
    total -= total * 0.25
total -= total * 0.10

if total >= trip_price:
    print(f'Yes! {total - trip_price:.2f} lv left.')
else:
    print(f'Not enough money! {trip_price - total:.2f} lv needed.')


