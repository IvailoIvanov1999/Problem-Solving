import random
import colorama
from colorama import Fore

colorama.init(autoreset=True)

pc_number = random.randint(1, 100)

counter_number_of_tries = 0

while True:
    player_number = input(Fore.MAGENTA + "Choose a number between 1-100 : ")

    if player_number == "end" or player_number == "END":
        print(Fore.LIGHTGREEN_EX + "G o o d b y e ! Thanks for playing my game :)")
        break

    if not player_number.isdigit():
        print(Fore.RED + "Invalid input...Enter positive integer number please !")
        continue

    player_number = int(player_number)

    if player_number > 100 or player_number < 1 :
        print(Fore.RED + "Invalid input... Try again !")
        print(Fore.CYAN + "Please choose integer number between 1-100.")
        continue

    if player_number == pc_number:
        print(Fore.GREEN + f"Yesss,the number is {pc_number} !")
        print(Fore.YELLOW + f"You guessed the number {counter_number_of_tries} times")
        break

    elif player_number > pc_number:
        print(Fore.LIGHTGREEN_EX + "Choose a lower number .")
        counter_number_of_tries += 1
        print(f">>> Number of attempts :{counter_number_of_tries} <<< ")

    elif player_number < pc_number:
        print(Fore.LIGHTGREEN_EX + "Choose a higher number .")
        counter_number_of_tries += 1
        print(f">>> Number of attempts : {counter_number_of_tries} <<< ")
