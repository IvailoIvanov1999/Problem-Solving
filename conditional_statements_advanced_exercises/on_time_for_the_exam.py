# input
hour_exam = int(input())
minute_exam = int(input())

hour_of_arrival = int(input())
minute_of_arrival = int(input())

exam_all_minutes = hour_exam * 60 + minute_exam
arrival_all_minutes = hour_of_arrival * 60 + minute_of_arrival

# code
difference_minutes = abs(exam_all_minutes - arrival_all_minutes)

if exam_all_minutes < arrival_all_minutes:
    print("Late")

    if difference_minutes < 60:
        print(f"{difference_minutes} minutes after the start")

    elif difference_minutes >= 60:
        print(f'{difference_minutes // 60}:{difference_minutes % 60:02d} hours after the start')


elif arrival_all_minutes == exam_all_minutes or difference_minutes <= 30:
    print("On time")

    if difference_minutes > 0:
        print(f'{difference_minutes} minutes before the start ')

else:
    print("Early")

    if difference_minutes   < 60:
        print(f'{difference_minutes} minutes before the start')
    elif difference_minutes  >= 60:
        print(f'{difference_minutes//60}:{difference_minutes%60:02d} hours before the start')


# output
