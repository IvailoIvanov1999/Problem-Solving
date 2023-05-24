nylon = 1.50
paint = 14.50
thinner = 5

needed_nylon = int(input())

price_nylon = (needed_nylon + 2) * nylon

needed_paint = int(input())

price_paint = (needed_paint+(needed_paint*0.10) )* paint

needed_thinner = int(input())

price_thinner = needed_thinner * thinner

hours = int(input())

all_sum = (price_nylon +price_paint + price_thinner) + 0.40

workers_price=(all_sum*0.30)*hours

final_price_everything=all_sum+workers_price


print(final_price_everything)
