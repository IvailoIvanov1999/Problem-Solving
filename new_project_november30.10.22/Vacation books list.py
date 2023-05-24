pages_number = int(input())
pages = int(input())
day = int(input())

pages_per_hour = pages_number // pages

hours_for_day = pages_per_hour // day

print(hours_for_day)
