hour = int(input())
day_of_week = input()

if 10 <= hour < 18 and day_of_week!="Sunday":
    if day_of_week=="Monday"or"Tuesday"or"Wednesday"or"Thursday"or"Friday"or"Saturday":
        print("open")

else:
    print("closed")
