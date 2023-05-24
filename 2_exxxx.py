from math import ceil
from math import floor

days_count_santa_missing = int(input())

food_he_left_kgs = int(input())

food_for_day_1st_elen_kgs = float(input())

food_for_day_2nd_elen_kgs = float(input())

food_for_day_3rd_elen_kgs = float(input())

total_food_1st_elen = food_for_day_1st_elen_kgs * days_count_santa_missing
total_food_2nd_elen = food_for_day_2nd_elen_kgs * days_count_santa_missing
total_food_3rd_elen = food_for_day_3rd_elen_kgs * days_count_santa_missing


food_total = total_food_1st_elen + total_food_2nd_elen + total_food_3rd_elen

if food_total < food_he_left_kgs:
    food_left = food_he_left_kgs - food_total
    print(f'{floor(int(food_left))} kilos of food left.')

else:
    food_needed = ceil(food_total - food_he_left_kgs)

    print(f'{food_needed} more kilos of food are needed.')
