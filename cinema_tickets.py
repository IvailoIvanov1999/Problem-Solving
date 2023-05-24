days_of_week = input()

# code/logic
if days_of_week == "Monday" or days_of_week == "Tuesday" or days_of_week == "Friday":
    print("12")
elif days_of_week == "Wednesday" or days_of_week == "Thursday":
    print("14")
elif days_of_week == "Saturday" or days_of_week == "Sunday":
    print("16")
