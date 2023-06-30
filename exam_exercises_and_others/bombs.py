from collections import deque

bomb_effect = deque([int(x) for x in input().split(', ')])
casings_bomb = [int(x) for x in input().split(', ')]

dict_bombs = {
    '40': ['Datura Bombs', 0],
    '60': ['Cherry Bombs', 0],
    '120': ['Smoke Decoy Bombs', 0]
}

filled = False

while True:
    counter = 0
    if not bomb_effect:
        break
    if not casings_bomb:
        break

    for k, v in dict_bombs.items():
        if dict_bombs[k][1] >= 3:
            counter += 1

    if counter == 3:
        filled = True
        break

    first_bomb_effect = bomb_effect.popleft()
    last_bomb_casing = casings_bomb.pop()

    sum_both = first_bomb_effect + last_bomb_casing

    if str(sum_both) in dict_bombs:
        dict_bombs[str(sum_both)][1] += 1
        continue
    else:
        last_bomb_casing -= 5
        bomb_effect.appendleft(first_bomb_effect)
        casings_bomb.append(last_bomb_casing)

if filled:
    print(f"Bene! You have successfully filled the bomb pouch!")
else:
    print("You don't have enough materials to fill the bomb pouch.")

if bomb_effect:
    print(f"Bomb Effects: {', '.join([str(x) for x in bomb_effect])}")
else:
    print("Bomb Effects: empty")

if casings_bomb:
    print(f"Bomb Casings: {', '.join([str(x) for x in casings_bomb])}")
else:
    print("Bomb Casings: empty")

output = ''

sorted_dict = sorted(dict_bombs.items(), key=lambda kvpt: kvpt[1][0])

for el in sorted_dict:
    output += f"{el[1][0]}: {str(el[1][1])}" + '\n'

print(output)
