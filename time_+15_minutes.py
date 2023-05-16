# vhod
input_hours = int(input())
input_minutes = int(input())

# logic
all_minutes = (input_hours * 60) + input_minutes
all_minutes += 15

hours=all_minutes//60
minutes=all_minutes%60

if hours >23:
    hours=0
# output

print(f'{hours}:{minutes:02d}')

