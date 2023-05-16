deposit_sum = float(input())
time_for_deposit = int(input())
year_percent = float(input())

per_year = deposit_sum * (year_percent / 100)
per_month = per_year / 12
all_sum =deposit_sum+time_for_deposit*per_month
print(all_sum)
