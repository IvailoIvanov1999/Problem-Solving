from math import ceil

# User Input

series_name = input()
episode_lenght = int(input())
lunch_break = int(input())

# logic
lunch_time = lunch_break / 8
rest_time = lunch_break / 4

time_to_watch = lunch_break - lunch_time - rest_time

# Output
if time_to_watch >= episode_lenght:
    print(f"You have enough time to watch {series_name} and left "
          f"with {ceil(time_to_watch - episode_lenght)} minutes free time.")
else:
    print(f"You don't have enough time to watch {series_name}, you need {ceil(episode_lenght - time_to_watch)} "
          f"more minutes.")