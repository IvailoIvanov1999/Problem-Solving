# import random
# import colorama
# from colorama import Fore,Style
# import sys,time
#
# colorama.init(autoreset=True)
#
# game_done = False
# counter_moves = 0
# one_time_only = 1
# action = None
# flag = False
# counter = 2
# all_combinations_allowed = []
# allowed_lanes = ["a", "b", "c"]
# allowed_columns = ["1", "2", "3"]
# allowed_chars = ["X", "O"]
# allowed_entry_commands = ["3", "1", "2", "4"]
#
# f_line = "| - | - | - |"
# s_line = "| - | - | - |"
# t_line = "| - | - | - |"
#
# def typewriter(message):
#     for ch in message:
#         sys.stdout.write(ch)
#         sys.stdout.flush()
#         time.sleep(0.03)
#     return ""
#
#
# def tic_tac_toe_field():
#     print("            1   2   3 ")
#     print("           ⬇  ⬇  ⬇ ")
#     print("           ―――――― ")
#     print(f"   a ➤   {f_line}")
#     print(f"   b ➤   {s_line}")
#     print(f"   c ➤   {t_line}")
#     print("           ―――――― ")
#
#
# def entry():
#     print(typewriter("   ――――――――――――――――――――――――――――"))
#     print(typewriter("   | Hello! Welcome in my Tic-Tac-Toe game ! :) |"))
#     print(typewriter("   |         Made by Ivailo Ivanov              |"))
#     print(typewriter("   ――――――――――――――――――――――――――――"))
#     print()
#     print(typewriter("       For | Player vs Player | press - 1"))
#     print(typewriter("          For | Player vs PC | press - 2"))
#     print(typewriter("             For | Rules | press - 3"))
#     print(typewriter("                For | Exit | press - 4"))
#
#     print()
#
#
# while True:
#     if game_done:
#         f_line = "| - | - | - |"
#         s_line = "| - | - | - |"
#         t_line = "| - | - | - |"
#         counter_moves = 0
#         one_time_only = 1
#         all_combinations_allowed = []
#     entry()
#
#     mode = input(Fore.LIGHTGREEN_EX + "Choose please : ")
#     print()
#
#     while mode not in allowed_entry_commands:
#         print()
#         print("Invalid input !")
#         print()
#         print("Choose between options - 1,2,3,4 !")
#         print()
#         mode = input("Choose please : ")
#
#     if mode == "1":
#         allowed_chars = ["X", "O"]
#         counter = 2
#         while True:
#             move = input(Fore.LIGHTCYAN_EX + "Choose which character you will be (X or O): ")
#             move = move.upper()
#             # check for valid character (symbol)
#             if move == "X":
#                 print()
#                 print(Fore.GREEN + "You choosed to play with =>  X  ")
#
#                 flag = True
#             elif move == "O":
#                 print()
#                 print(Fore.GREEN + "You choosed to play with =>  O  ")
#
#                 flag = True
#             else:
#                 print()
#                 print(Fore.RED+"Invalid character!")
#                 print()
#                 print("Please choose again.")
#                 print()
#                 continue
#             if flag:
#                 break
#
#         while True:
#             if one_time_only == 1:
#                 tic_tac_toe_field()
#                 one_time_only += 1
#                 print()
#                 print(
#                 Fore.LIGHTYELLOW_EX + "Example: a 1 - ('a' is lane,case sensitive , '1' is place to paste you character ,splited by only 1 space!)")
#                 print()
#             if counter % 2 == 0:
#                 action = input(Fore.GREEN + f"Player 1 ,choose place to paste - {move}: ").split(" ")
#                 if len(allowed_chars) > 1:
#                     allowed_chars.remove(move)
#             else:
#                 action = input(Fore.LIGHTRED_EX+f"Player 2 ,choose place to paste - {allowed_chars[0]}: ").split(" ")
#
#             try:
#                 lane_on_field = action[0]
#
#                 place_on_field = action[1]
#                 lane_on_field = lane_on_field.lower()
#
#             except IndexError:
#                 print()
#                 print(Fore.RED + "Invalid input.")
#                 continue
#
#             # check for valid line and index
#             if lane_on_field not in allowed_lanes:
#                 print()
#                 print(Fore.RED + f"Invalid lane to paste your character - {move}")
#                 print()
#                 print("Please choose valid lane on the field!")
#                 tic_tac_toe_field()
#                 continue
#             elif place_on_field not in allowed_columns:
#                 print()
#                 print(Fore.RED + f"Invalid place to paste your character - {move}")
#                 print()
#                 print("Please choose valid place on the field!")
#                 tic_tac_toe_field()
#                 continue
#             # first line
#
#             if lane_on_field == "a":
#                 if place_on_field == "3":
#                     if f_line[10] != "-":
#                         print("Already used,try again!")
#                         tic_tac_toe_field()
#                         continue
#                     else:
#                         if counter % 2 == 0:
#                             f_line = f_line[:10] + f'{move}' + f_line[11:]
#                         else:
#                             f_line = f_line[:10] + f'{allowed_chars[0]}' + f_line[11:]
#                     tic_tac_toe_field()
#                     counter += 1
#
#
#
#                 elif place_on_field == "2":
#                     if f_line[6] != "-":
#                         print("Already used,try again!")
#                         tic_tac_toe_field()
#                         continue
#                     else:
#                         if counter % 2 == 0:
#                             f_line = f_line[:6] + f'{move}' + f_line[7:]
#                         else:
#                             f_line = f_line[:6] + f'{allowed_chars[0]}' + f_line[7:]
#                     tic_tac_toe_field()
#                     counter += 1
#
#
#                 elif place_on_field == "1":
#                     if f_line[2] != "-":
#                         print("Already used,try again!")
#                         tic_tac_toe_field()
#                         continue
#                     else:
#                         if counter % 2 == 0:
#                             f_line = f_line[:2] + f'{move}' + f_line[3:]
#                         else:
#                             f_line = f_line[:2] + f'{allowed_chars[0]}' + f_line[3:]
#                     tic_tac_toe_field()
#                     counter += 1
#
#             # second line
#             elif lane_on_field == "b":
#                 if place_on_field == "3":
#                     if s_line[10] != "-":
#                         print("Already used,try again!")
#                         tic_tac_toe_field()
#                         continue
#                     else:
#                         if counter % 2 == 0:
#                             s_line = s_line[:10] + f'{move}' + s_line[11:]
#                         else:
#                             s_line = s_line[:10] + f'{allowed_chars[0]}' + s_line[11:]
#                     tic_tac_toe_field()
#                     counter += 1
#
#
#                 elif place_on_field == "2":
#                     if s_line[6] != "-":
#                         print("Already used,try again!")
#                         tic_tac_toe_field()
#                         continue
#                     else:
#                         if counter % 2 == 0:
#                             s_line = s_line[:6] + f'{move}' + s_line[7:]
#                         else:
#                             s_line = s_line[:6] + f'{allowed_chars[0]}' + s_line[7:]
#                     tic_tac_toe_field()
#                     counter += 1
#
#
#                 elif place_on_field == "1":
#                     if s_line[2] != "-":
#                         print("Already used,try again!")
#                         tic_tac_toe_field()
#                         continue
#                     else:
#                         if counter % 2 == 0:
#                             s_line = s_line[:2] + f'{move}' + s_line[3:]
#                         else:
#                             s_line = s_line[:2] + f'{allowed_chars[0]}' + s_line[3:]
#                     tic_tac_toe_field()
#                     counter += 1
#
#             # third line
#             elif lane_on_field == "c":
#                 if place_on_field == "3":
#                     if t_line[10] != "-":
#                         print("Already used,try again!")
#                         tic_tac_toe_field()
#                         continue
#                     else:
#                         if counter % 2 == 0:
#                             t_line = t_line[:10] + f'{move}' + t_line[11:]
#                         else:
#                             t_line = t_line[:10] + f'{allowed_chars[0]}' + t_line[11:]
#                     tic_tac_toe_field()
#                     counter += 1
#
#
#                 elif place_on_field == "2":
#                     if t_line[6] != "-":
#                         print("Already used,try again!")
#                         tic_tac_toe_field()
#                         continue
#                     else:
#                         if counter % 2 == 0:
#                             t_line = t_line[:6] + f'{move}' + t_line[7:]
#                         else:
#                             t_line = t_line[:6] + f'{allowed_chars[0]}' + t_line[7:]
#                     tic_tac_toe_field()
#                     counter += 1
#
#
#
#                 elif place_on_field == "1":
#                     if t_line[2] != "-":
#                         print("Already used,try again!")
#                         tic_tac_toe_field()
#                         continue
#                     else:
#                         if counter % 2 == 0:
#                             t_line = t_line[:2] + f'{move}' + t_line[3:]
#                         else:
#                             t_line = t_line[:2] + f'{allowed_chars[0]}' + t_line[3:]
#                     tic_tac_toe_field()
#                     counter += 1
#             # #       f_line = "| - | - | - |"
#             # #       s_line = "| - | - | - |"
#             #         t_line = "| - | - | - |"
#             # for player X
#             # lines check for winner
#             if f_line[2] == "X" and f_line[6] == "X" and f_line[10] == "X":
#                 print(Fore.GREEN + "Congratulations ! Player with 'X' is winner.")
#                 input("Press enter for / Main Menu /")
#                 game_done = True
#                 break
#             elif s_line[2] == "X" and s_line[6] == "X" and s_line[10] == "X":
#                 print(Fore.GREEN + "Congratulations ! Player with 'X' is winner.")
#                 input("Press enter for / Main Menu /")
#                 game_done = True
#                 break
#             elif t_line[2] == "X" and t_line[6] == "X" and t_line[10] == "X":
#                 print(Fore.GREEN + "Congratulations ! Player with 'X' is winner.")
#                 input("Press enter for / Main Menu /")
#                 game_done = True
#                 break
#                 # columns check for winner
#             elif f_line[2] == "X" and s_line[2] == "X" and t_line[2] == "X":
#                 print(Fore.GREEN + "Congratulations ! Player with 'X' is winner.")
#                 input("Press enter for / Main Menu /")
#                 game_done = True
#                 break
#             elif f_line[6] == "X" and s_line[6] == "X" and t_line[6] == "X":
#                 print(Fore.GREEN + "Congratulations ! Player with 'X' is winner.")
#                 input("Press enter for / Main Menu /")
#                 game_done = True
#                 break
#             elif f_line[10] == "X" and s_line[10] == "X" and t_line[10] == "X":
#                 print(Fore.GREEN + "Congratulations ! Player with 'X' is winner.")
#                 input("Press enter for / Main Menu /")
#                 game_done = True
#                 break
#                 # diagonals check for winner
#             elif f_line[2] == "X" and s_line[6] == "X" and t_line[10] == "X":
#                 print(Fore.GREEN + "Congratulations ! Player with 'X' is winner.")
#                 input("Press enter for / Main Menu /")
#                 game_done = True
#                 break
#             elif f_line[10] == "X" and s_line[6] == "X" and t_line[2] == "X":
#                 print(Fore.GREEN + "Congratulations ! Player with 'X' is winner.")
#                 input("Press enter for / Main Menu /")
#                 game_done = True
#                 break
#
#                 # for player 0
#                 # lines check for winner
#             if f_line[2] == "O" and f_line[6] == "O" and f_line[10] == "O":
#                 print(Fore.GREEN + "Congratulations ! Player with 'O' is winner.")
#                 input("Press enter for / Main Menu /")
#                 game_done = True
#                 break
#             elif s_line[2] == "O" and s_line[6] == "O" and s_line[10] == "O":
#                 print(Fore.GREEN + "Congratulations ! Player with 'O' is winner.")
#                 input("Press enter for / Main Menu /")
#                 game_done = True
#                 break
#             elif t_line[2] == "O" and t_line[6] == "O" and t_line[10] == "O":
#                 print(Fore.GREEN + "Congratulations ! Player with 'O' is winner.")
#                 input("Press enter for / Main Menu /")
#                 game_done = True
#                 break
#                 # columns check for winner
#             elif f_line[2] == "O" and s_line[2] == "O" and t_line[2] == "O":
#                 print(Fore.GREEN + "Congratulations ! Player with 'O' is winner.")
#                 input("Press enter for / Main Menu /")
#                 game_done = True
#                 break
#             elif f_line[6] == "O" and s_line[6] == "O" and t_line[6] == "O":
#                 print(Fore.GREEN + "Congratulations ! Player with 'O' is winner.")
#                 input("Press enter for / Main Menu /")
#                 game_done = True
#                 break
#             elif f_line[10] == "O" and s_line[10] == "O" and t_line[10] == "O":
#                 print(Fore.GREEN + "Congratulations ! Player with 'O' is winner.")
#                 input("Press enter for / Main Menu /")
#                 game_done = True
#                 break
#                 # diagonals check for winner
#             elif f_line[2] == "O" and s_line[6] == "O" and t_line[10] == "O":
#                 print(Fore.GREEN + "Congratulations ! Player with 'O' is winner.")
#                 input("Press enter for / Main Menu /")
#                 game_done = True
#                 break
#             elif f_line[10] == "O" and s_line[6] == "O" and t_line[2] == "O":
#                 print(Fore.GREEN + "Congratulations ! Player with 'O' is winner.")
#                 input("Press enter for / Main Menu /")
#                 game_done = True
#                 break
#
#             counter_moves += 1
#
#             # Draw
#             if counter_moves >= 9:
#                 print(Fore.YELLOW + "   D r a w !  ")
#                 input("Press enter for / Main Menu /")
#                 game_done = True
#                 break
#
#
#
#         continue
#
#
#
#
#
#
#     # PLayer vs PC
#
#     elif mode == "2":
#         flag_pc = False
#         counter = 2
#         allowed_chars = ["X", "O"]
#
#         while True:
#             move = input(Fore.LIGHTRED_EX + "Choose which character you will be (X or O): ")
#             move = move.upper()
#             # check for valid character (symbol)
#             if move == "X":
#                 print()
#                 print("You choosed to play with =>  X  ")
#
#                 flag = True
#             elif move == "O":
#                 print()
#                 print("You choosed to play with =>  O  ")
#
#                 flag = True
#             else:
#                 print()
#                 print(Fore.RED + "Invalid character!")
#                 print()
#                 print("Please choose again.")
#                 print()
#                 continue
#             if flag:
#                 break
#
#         while True:
#
#             if one_time_only == 1:
#                 tic_tac_toe_field()
#                 one_time_only += 1
#                 print()
#                 print(
#                 Fore.LIGHTYELLOW_EX +"Example: a 1 - ('a' is lane,case sensitive , '1' is place to paste you character ,splited by only 1 space!)")
#                 print()
#
#             if counter % 2 == 0:
#                 if one_time_only == 1:
#                     tic_tac_toe_field()
#
#                 action = input(Fore.LIGHTYELLOW_EX +f"Player 1 ,choose place to paste - {move}: ").split(" ")
#
#
#                 if len(allowed_chars) > 1:
#                     allowed_chars.remove(move)
#                 #######
#                 try:
#                     lane_on_field = action[0]
#
#                     place_on_field = action[1]
#                     lane_on_field = lane_on_field.lower()
#
#                 except IndexError:
#                     print()
#                     print(Fore.RED + "Invalid input.")
#                     continue
#
#                 # check for valid line and index
#                 if lane_on_field not in allowed_lanes:
#                     print()
#                     print(Fore.RED +f"Invalid lane to paste your character - {move}")
#                     print()
#                     print("Please choose valid lane on the field!")
#                     tic_tac_toe_field()
#                     continue
#                 elif place_on_field not in allowed_columns:
#                     print()
#                     print(Fore.RED +f"Invalid place to paste your character - {move}")
#                     print()
#                     print("Please choose valid place on the field!")
#                     tic_tac_toe_field()
#                     continue
#             else:
#
#                 while True:
#
#                     pc_move = random.randint(1, 9)
#
#                     if pc_move not in all_combinations_allowed:
#                         all_combinations_allowed.append(pc_move)
#                         flag_pc = True
#                     else:
#                         continue
#                     if flag_pc:
#                         break
#
#                     ###### PC LOGIC
#                 if pc_move == 1:
#                     lane_on_field = "a"
#                     place_on_field = "1"
#                 elif pc_move == 2:
#                     lane_on_field = "a"
#                     place_on_field = "2"
#                 elif pc_move == 3:
#                     lane_on_field = "a"
#                     place_on_field = "3"
#
#                 elif pc_move == 4:
#                     lane_on_field = "b"
#                     place_on_field = "1"
#                 elif pc_move == 5:
#                     lane_on_field = "b"
#                     place_on_field = "2"
#                 elif pc_move == 6:
#                     lane_on_field = "b"
#                     place_on_field = "3"
#
#                 elif pc_move == 7:
#                     lane_on_field = "c"
#                     place_on_field = "1"
#                 elif pc_move == 8:
#                     lane_on_field = "c"
#                     place_on_field = "2"
#                 elif pc_move == 9:
#                     lane_on_field = "c"
#                     place_on_field = "3"
#
#             if lane_on_field == "a":
#                 if place_on_field == "3":
#                     if f_line[10] != "-":
#                         if counter % 2 == 0:
#                             print("Already used,try again!")
#                             tic_tac_toe_field()
#                             continue
#                         else:
#                             continue
#                     else:
#                         if counter % 2 == 0:
#                             f_line = f_line[:10] + f'{move}' + f_line[11:]
#                         else:
#                             f_line = f_line[:10] +  f'{allowed_chars[0]}' + f_line[11:]
#                             print(Fore.LIGHTGREEN_EX +" | PC |  move :")
#                     tic_tac_toe_field()
#                     counter += 1
#
#                 elif place_on_field == "2":
#                     if f_line[6] != "-":
#                         if counter % 2 == 0:
#                             print("Already used,try again!")
#                             tic_tac_toe_field()
#                             continue
#                         else:
#                             continue
#                     else:
#                         if counter % 2 == 0:
#                             f_line = f_line[:6] + f'{move}' + f_line[7:]
#                         else:
#                             f_line = f_line[:6] + f'{allowed_chars[0]}' + f_line[7:]
#                             print(Fore.LIGHTGREEN_EX +" | PC |  move :")
#                     tic_tac_toe_field()
#                     counter += 1
#
#
#                 elif place_on_field == "1":
#                     if f_line[2] != "-":
#                         if counter % 2 == 0:
#                             print("Already used,try again!")
#                             tic_tac_toe_field()
#                             continue
#                         else:
#                             continue
#                     else:
#                         if counter % 2 == 0:
#                             f_line = f_line[:2] + f'{move}' + f_line[3:]
#                         else:
#                             f_line = f_line[:2] +  f'{allowed_chars[0]}' + f_line[3:]
#                             print(Fore.LIGHTGREEN_EX +" | PC |  move :")
#                     tic_tac_toe_field()
#                     counter += 1
#
#             elif lane_on_field == "b":
#                 if place_on_field == "3":
#                     if s_line[10] != "-":
#                         if counter % 2 == 0:
#                             print("Already used,try again!")
#                             tic_tac_toe_field()
#                             continue
#                         else:
#                             continue
#                     else:
#                         if counter % 2 == 0:
#                             s_line = s_line[:10] + f'{move}' + s_line[11:]
#                         else:
#                             s_line = s_line[:10] + f'{allowed_chars[0]}' + s_line[11:]
#                             print(Fore.LIGHTGREEN_EX +" | PC |  move :")
#                     tic_tac_toe_field()
#                     counter += 1
#
#                 elif place_on_field == "2":
#                     if s_line[6] != "-":
#                         if counter % 2 == 0:
#                             print("Already used,try again!")
#                             tic_tac_toe_field()
#                             continue
#                         else:
#                             continue
#                     else:
#                         if counter % 2 == 0:
#                             s_line = s_line[:6] + f'{move}' + s_line[7:]
#                         else:
#                             s_line = s_line[:6] + f'{allowed_chars[0]}' + s_line[7:]
#                             print(Fore.LIGHTGREEN_EX +" | PC |  move :")
#                     tic_tac_toe_field()
#                     counter += 1
#
#
#                 elif place_on_field == "1":
#                     if s_line[2] != "-":
#                         if counter % 2 == 0:
#                             print("Already used,try again!")
#                             tic_tac_toe_field()
#                             continue
#                         else:
#                             continue
#                     else:
#                         if counter % 2 == 0:
#                             s_line = s_line[:2] + f'{move}' + s_line[3:]
#                         else:
#                             s_line = s_line[:2] + f'{allowed_chars[0]}' + s_line[3:]
#                             print(Fore.LIGHTGREEN_EX +" | PC |  move :")
#                     tic_tac_toe_field()
#                     counter += 1
#
#             elif lane_on_field == "c":
#                 if place_on_field == "3":
#                     if t_line[10] != "-":
#                         if counter % 2 == 0:
#                             print("Already used,try again!")
#                             tic_tac_toe_field()
#                             continue
#                         else:
#                             continue
#                     else:
#                         if counter % 2 == 0:
#                             t_line = t_line[:10] + f'{move}' + t_line[11:]
#                         else:
#                             t_line = t_line[:10] + f'{allowed_chars[0]}' + t_line[11:]
#                             print(Fore.LIGHTGREEN_EX +" | PC |  move :")
#                     tic_tac_toe_field()
#                     counter += 1
#
#                 elif place_on_field == "2":
#                     if t_line[6] != "-":
#                         if counter % 2 == 0:
#                             print("Already used,try again!")
#                             tic_tac_toe_field()
#                             continue
#                         else:
#                             continue
#                     else:
#                         if counter % 2 == 0:
#                             t_line = t_line[:6] + f'{move}' + t_line[7:]
#                         else:
#                             t_line = t_line[:6] + f'{allowed_chars[0]}' + t_line[7:]
#                             print(Fore.LIGHTGREEN_EX +" | PC |  move :")
#                     tic_tac_toe_field()
#                     counter += 1
#
#
#                 elif place_on_field == "1":
#                     if t_line[2] != "-":
#                         if counter % 2 == 0:
#                             print("Already used,try again!")
#                             tic_tac_toe_field()
#                             continue
#                         else:
#                             continue
#                     else:
#                         if counter % 2 == 0:
#
#                             t_line = t_line[:2] + f'{move}' + t_line[3:]
#                         else:
#                             t_line = t_line[:2] + f'{allowed_chars[0]}' + t_line[3:]
#                             print(Fore.LIGHTGREEN_EX + " | PC |  move :")
#                     tic_tac_toe_field()
#                     counter += 1
#
#             if f_line[2] == "X" and f_line[6] == "X" and f_line[10] == "X":
#                 print(Fore.GREEN + "Congratulations ! Player with 'X' is winner.")
#                 input("Press enter for / Main Menu /")
#                 game_done = True
#                 break
#             elif s_line[2] == "X" and s_line[6] == "X" and s_line[10] == "X":
#                 print(Fore.GREEN + "Congratulations ! Player with 'X' is winner.")
#                 input("Press enter for / Main Menu /")
#                 game_done = True
#                 break
#             elif t_line[2] == "X" and t_line[6] == "X" and t_line[10] == "X":
#                 print(Fore.GREEN + "Congratulations ! Player with 'X' is winner.")
#                 input("Press enter for / Main Menu /")
#                 game_done = True
#                 break
#                 # columns check for winner
#             elif f_line[2] == "X" and s_line[2] == "X" and t_line[2] == "X":
#                 print(Fore.GREEN + "Congratulations ! Player with 'X' is winner.")
#                 input("Press enter for / Main Menu /")
#                 game_done = True
#                 break
#             elif f_line[6] == "X" and s_line[6] == "X" and t_line[6] == "X":
#                 print(Fore.GREEN + "Congratulations ! Player with 'X' is winner.")
#                 input("Press enter for / Main Menu /")
#                 game_done = True
#                 break
#             elif f_line[10] == "X" and s_line[10] == "X" and t_line[10] == "X":
#                 print(Fore.GREEN + "Congratulations ! Player with 'X' is winner.")
#                 input("Press enter for / Main Menu /")
#                 game_done = True
#                 break
#                 # diagonals check for winner
#             elif f_line[2] == "X" and s_line[6] == "X" and t_line[10] == "X":
#                 print(Fore.GREEN + "Congratulations ! Player with 'X' is winner.")
#                 input("Press enter for / Main Menu /")
#                 game_done = True
#                 break
#             elif f_line[10] == "X" and s_line[6] == "X" and t_line[2] == "X":
#                 print(Fore.GREEN + "Congratulations ! Player with 'X' is winner.")
#                 input("Press enter for / Main Menu /")
#                 game_done = True
#                 break
#
#                 # for player 0
#                 # lines check for winner
#             if f_line[2] == "O" and f_line[6] == "O" and f_line[10] == "O":
#                 print(Fore.GREEN + "Congratulations ! Player with 'O' is winner.")
#                 input("Press enter for / Main Menu /")
#                 game_done = True
#                 break
#             elif s_line[2] == "O" and s_line[6] == "O" and s_line[10] == "O":
#                 print(Fore.GREEN + "Congratulations ! Player with 'O' is winner.")
#                 input("Press enter for / Main Menu /")
#                 game_done = True
#                 break
#             elif t_line[2] == "O" and t_line[6] == "O" and t_line[10] == "O":
#                 print(Fore.GREEN + "Congratulations ! Player with 'O' is winner.")
#                 input("Press enter for / Main Menu /")
#                 game_done = True
#                 break
#                 # columns check for winner
#             elif f_line[2] == "O" and s_line[2] == "O" and t_line[2] == "O":
#                 print(Fore.GREEN + "Congratulations ! Player with 'O' is winner.")
#                 input("Press enter for / Main Menu /")
#                 game_done = True
#                 break
#             elif f_line[6] == "O" and s_line[6] == "O" and t_line[6] == "O":
#                 print(Fore.GREEN + "Congratulations ! Player with 'O' is winner.")
#                 input("Press enter for / Main Menu /")
#                 game_done = True
#                 break
#             elif f_line[10] == "O" and s_line[10] == "O" and t_line[10] == "O":
#                 print(Fore.GREEN + "Congratulations ! Player with 'O' is winner.")
#                 input("Press enter for / Main Menu /")
#                 game_done = True
#                 break
#                 # diagonals check for winner
#             elif f_line[2] == "O" and s_line[6] == "O" and t_line[10] == "O":
#                 print(Fore.GREEN + "Congratulations ! Player with 'O' is winner.")
#                 input("Press enter for / Main Menu /")
#                 game_done = True
#                 break
#             elif f_line[10] == "O" and s_line[6] == "O" and t_line[2] == "O":
#                 print(Fore.GREEN + "Congratulations ! Player with 'O' is winner.")
#                 input("Press enter for / Main Menu /")
#                 game_done = True
#                 break
#
#             counter_moves += 1
#
#             # Draw
#             if counter_moves >= 9:
#                 print(Fore.YELLOW + "   D r a w !  ")
#                 input("Press enter for / Main Menu /")
#                 game_done = True
#                 break
#
#         continue
#
#     # RULES
#     elif mode == "3":
#         print( Fore.LIGHTMAGENTA_EX +"            You choosed 'Rules'!")
#         print(
#             Fore.YELLOW +" You have to fill the free spaces on the board.If on column or line ,or diagonals have same characters as yours in every position and you match 3 same characters "
#                          "on theese lines ,you win ,in other case you lose.")
#         print( Fore.YELLOW + "  If neither player has won ,or lost ,then the game is 'Draw'.")
#         print()
#         game_done = True
#         input("To continue in / Main menu / press enter !")
#
#     # exit
#
#     elif mode == "4":
#         print(Fore.LIGHTCYAN_EX + "    G o o d b y e ! :)")
#         break


