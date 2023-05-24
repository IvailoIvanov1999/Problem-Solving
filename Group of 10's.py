numbers = list(map(int, input().split(", ")))

first = 10
previous = 0

while True:
    group = [int(i) for i in numbers if previous < i <= first]
    print(f"Group of {first}'s: {group}")
    if first >= max(numbers):
        break
    first += 10
    previous += 10