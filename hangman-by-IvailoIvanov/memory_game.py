elements = input().split()
moves = 0
while True:
    numbers_input = input().split()
    moves += 1

    if numbers_input == "end":
        break

    numbers_input_integers = [int(x) for x in numbers_input]

    if numbers_input_integers[0] == numbers_input_integers[1]:
        elements.insert((len(elements) // 2), f'{moves}a')
        elements.insert((len(elements) // 2), f'{moves}a')

        print("Invalid input! Adding additional elements to the board")
        print(elements)

    if numbers_input_integers[0] > 0 and numbers_input_integers[0] < len(elements) or(
        numbers_input_integers[1] > 0 and numbers_input_integers[1] < len(elements)):
        elements.insert((len(elements) // 2), f'{moves}a')
        elements.insert((len(elements) // 2), f'{moves}a')

        print("Invalid input! Adding additional elements to the board")
        print(elements)

    elif numbers_input_integers[0] == elements[numbers_input_integers[0]] and numbers_input_integers[1] == elements[
        numbers_input_integers[1]]:
        elements.remove(numbers_input_integers[0])
        elements.remove(numbers_input_integers[1])

        print(f"Congrats! You have found matching elements - {elements[numbers_input_integers[0]]}!")
