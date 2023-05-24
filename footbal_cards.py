cards_input = input().split()

sent_off_players_A = 0
sent_off_players_B = 0

off_players_A = []
off_players_B = []

should_terminate = False

for card in (cards_input):
    if card in off_players_A or card in off_players_B:
        continue
    cards = card.split("-")
    player_team = cards[0]
    player_number = cards[1]

    team_A = player_team == "A"

    if team_A:
        sent_off_players_A += 1
        off_players_A.append(card)

    else:
        sent_off_players_B += 1
        off_players_B.append(card)

    if len(off_players_A) > 4 or len(off_players_B) > 4:
        should_terminate = True
        break
print(f"Team A - {11 - (len(off_players_A))}; Team B - {11 - len(off_players_B)}")

if should_terminate:
    print("Game was terminated")
