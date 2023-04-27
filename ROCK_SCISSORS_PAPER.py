import random
import colorama
from colorama import Fore

colorama.init(autoreset=True)

win_counter = 0
lose_counter = 0
draw_counter = 0

while True:
    rock = 'Rock'
    paper = 'Paper'
    scissors = 'Scissors'

    # For rock ,insert (r),for paper ,insert (p),for scissors ,insert (s)

    player_move = input('Choose [r]-->rock, [p]-->paper, [s]-->scissors: ')

    if player_move == 'r':
        player_move = rock
    elif player_move == 's':
        player_move = scissors
    elif player_move == 'p':
        player_move = paper

    else:
        raise SystemExit('Invalid Input. Try again...')

    random_number = random.randint(1, 3)

    pc_move = ''

    if random_number == 1:
        pc_move = 'Scissors'
    elif random_number == 2:
        pc_move = 'Rock'
    elif random_number == 3:
        pc_move = 'Paper'
    print(f"The computer chose {pc_move}.")

    if player_move == pc_move:
        draw_counter += 1
        print(Fore.YELLOW + 'Draw')
    elif player_move == rock and pc_move == scissors or player_move == paper and pc_move == rock or \
            player_move == scissors and pc_move == paper:
        win_counter += 1
        print(Fore.GREEN + 'You Win')
    else:
        lose_counter += 1
        print(Fore.RED + 'You Lose')

    print(f'You Win: {win_counter} | You Lose: {lose_counter} | Draws: {draw_counter}')