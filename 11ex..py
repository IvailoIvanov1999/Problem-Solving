data = input()
side_b_players = {}
playe_by_side = {}

while data != "Lumpawaroo":

    if "|" in data:
        text_input = data.split(" | ")
        f_side = text_input[0]
        f_user = text_input[1]

        if f_side not in playe_by_side:
            playe_by_side[f_side] = []

        if f_user not in side_b_players:
            side_b_players[f_user] = f_side
            playe_by_side[f_side].append(f_user)

    else:
        text_input_2 = data.split(" -> ")
        f_user = text_input_2[0]
        f_side = text_input_2[1]

        if f_side not in playe_by_side:
            playe_by_side[f_side] = []

        playe_by_side[f_side].append(f_user)

        if f_user in side_b_players:
            old_side = side_b_players[f_user]
            playe_by_side[old_side].remove(f_user)
            side_b_players[f_user] = f_side
        else:
            side_b_players[f_user] = f_side

        print(f"{f_user} joins the {f_side} side!")

    data = input()

for k, v in playe_by_side.items():
    if len(v) == 0:
        continue

    print(f"Side: {k}, Members: {len(playe_by_side[k])}")
    for el in v:
        print(f"! {el}")
