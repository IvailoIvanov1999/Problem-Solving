# VHOD
from math import floor

record_in_seconds = float(input())
distance_in_metres = float(input())
time_in_second_for_1_metre = float(input())

# IZHOD
ivan_swimed_metres_seconds = distance_in_metres * time_in_second_for_1_metre

water_resistance_ivan = int(floor(distance_in_metres / 15)) * 12.5

total_ivan_metres_distance = water_resistance_ivan + ivan_swimed_metres_seconds


if total_ivan_metres_distance < record_in_seconds:
    print(f"Yes, he succeeded! The new world record is {total_ivan_metres_distance:.2f} seconds.")
else:
    total_ivan_metres_distance >= record_in_seconds
    needed_seconds = total_ivan_metres_distance - record_in_seconds
    print (f"No, he failed! He was {needed_seconds:.2f} seconds slower.")
