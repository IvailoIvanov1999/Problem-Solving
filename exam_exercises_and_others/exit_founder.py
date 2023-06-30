from collections import deque

tom_jerry = deque(input().split(', '))

matrix = [[x for x in input().split()] for _ in range(6)]

dict_for_rest = {
    'Tom': 0,
    "Jerry": 0
}

while True:
    coords_from_input = input()
    curr_player_row, curr_player_col = int(coords_from_input[1]), int(coords_from_input[4])

    current_player_name = tom_jerry.popleft()

    if dict_for_rest[current_player_name] == 1:
        dict_for_rest[current_player_name] = 0
        tom_jerry.append(current_player_name)
        continue

    if matrix[curr_player_row][curr_player_col] == "E":
        print(f"{current_player_name} found the Exit and wins the game!")
        break

    if matrix[curr_player_row][curr_player_col] == "T":
        print(f"{current_player_name} is out of the game! The winner is {tom_jerry[-1]}.")
        break

    if matrix[curr_player_row][curr_player_col] == "W":
        print(f"{current_player_name} hits a wall and needs to rest.")
        dict_for_rest[current_player_name] += 1
        tom_jerry.append(current_player_name)
        continue

    tom_jerry.append(current_player_name)
