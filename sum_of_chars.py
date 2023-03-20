number = int(input())
all_sum=0
for _ in range(number):
    character = input()

    new_char = ord(character)
    all_sum+=new_char

print(f"The sum equals: {all_sum}")
