import math

first_time = int(input())
second_time = int(input())
third_time = int(input())

total_time_seconds = (first_time + second_time + third_time)

seconds=total_time_seconds % 60

minutes_total = total_time_seconds // 60

minutes=math.floor(minutes_total)

if seconds<10:
     print(f'{minutes}:0{seconds}')
else:
    print(f'{minutes}:{seconds}')



