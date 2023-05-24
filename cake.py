width = int(input())
length = int(input())

times_taking_counter = 0
final_piece_taken = 0
total = 0

cake_size = width * length

no_more_pieces = False

pieces_size = input()
while pieces_size != "STOP":
    pieces_size = int(pieces_size)

    cake_size -= pieces_size

    times_taking_counter += 1
    if cake_size <= 0:
        no_more_pieces = True
        break

    pieces_size = input()

if no_more_pieces:
    print(f'No more cake left! You need {abs(cake_size)} pieces more.')
else:
    print(f"{cake_size} pieces are left.")