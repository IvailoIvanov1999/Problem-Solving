folowers_dict = {}

while True:
    commands = input().split(": ")

    move = commands[0]

    if move == "Log out":
        break

    username = commands[1]

    if move == "New follower":
        if username in folowers_dict:
            continue
        else:
            # likes   #comments
            folowers_dict[username] = [int(0), int(0)]

    elif move == "Like":
        count_likes = int(commands[2])
        if username not in folowers_dict:
            folowers_dict[username] = [count_likes, int(0)]
        else:
            folowers_dict[username][0] += count_likes

    elif move == "Comment":
        if username not in folowers_dict:
            folowers_dict[username] = [int(0), int(1)]
        else:
            folowers_dict[username][1] += int(1)

    elif move == "Blocked":
        if username not in folowers_dict:
            print(f"{username} doesn't exist.")
        else:
            del folowers_dict[username]

print(f"{len(folowers_dict)} followers")

for k in folowers_dict:
    total_like_coments = sum(folowers_dict[k])
    print(f"{k}: {total_like_coments}")
