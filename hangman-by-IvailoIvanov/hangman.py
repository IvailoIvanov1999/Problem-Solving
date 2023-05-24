import random


def hangman_lifes(index_life=0):
    if index_life == 10:
        print('         _____ ')
        print('         |   | ')
        print('         O   | ')
        print('        /|\  | ')
        print('        / \  | ')
        print('             | ')
        print('     ________|_')
        return
    if index_life == 9:
        print('         _____ ')
        print('         |   | ')
        print('         O   | ')
        print('        /|\  | ')
        print('        /    | ')
        print('             | ')
        print('     ________|_')
        return
    if index_life == 8:
        print('         _____ ')
        print('         |   | ')
        print('         O   | ')
        print('        /|\  | ')
        print('             | ')
        print('             | ')
        print('     ________|_')
        return
    if index_life == 7:
        print('         _____ ')
        print('         |   | ')
        print('         O   | ')
        print('        /|   | ')
        print('             | ')
        print('             | ')
        print('     ________|_')
        return
    if index_life == 6:
        print('         _____ ')
        print('         |   | ')
        print('         O   | ')
        print('         |   | ')
        print('             | ')
        print('             | ')
        print('     ________|_')
        return
    if index_life == 5:
        print('         _____ ')
        print('         |   | ')
        print('         O   | ')
        print('             | ')
        print('             | ')
        print('             | ')
        print('     ________|_')
        return
    if index_life == 4:
        print('         _____ ')
        print('         |   | ')
        print('             | ')
        print('             | ')
        print('             | ')
        print('             | ')
        print('     ________|_')
        return
    if index_life == 3:
        print('         _____ ')
        print('             | ')
        print('             | ')
        print('             | ')
        print('             | ')
        print('             | ')
        print('     ________|_')
        return
    if index_life == 2:
        print('               ')
        print('             | ')
        print('             | ')
        print('             | ')
        print('             | ')
        print('             | ')
        print('     ________|_')
        return
    if index_life == 1:
        print('               ')
        print('               ')
        print('               ')
        print('               ')
        print('               ')
        print('               ')
        print('     ________|_')
        return


print('____________________')
print('|      Hangman     |')
print('|  by IvailoIvanov |')
print('____________________')

print("*************************************")
print("*     Game content only nouns       *")
print("*************************************")
print("*  1. Easy [max.4 letters words]    *")
print("*  2. Medium [6 letters words]      *")
print("*  3. Hard  [8 letters words]       *")
print("*  4. Expert [12 letters words]     *")
print("*  5. Rules                         *")
print("*  6. Exit                          *")
print("*************************************")


def easy_level():
    # 4 letters words
    easy_level_words = ["book", "pen", "car", "dice", "face", "mask", "cost", "palm", "aloe", "game", "barn", "bake",
                        "base", "cafe", "joke", "lady", "mass", "olio", "onyx", "open"]

    randomized_easy_word = random.choice(easy_level_words)

    return randomized_easy_word


def medium_level():
    # 6 letters words
    medium_level_words = ["doctor", "friend", "banker", "police", "market", "school", "policy", "office", "person",
                          "course", "system", "petrol", "raffle", "vacuum"]
    randomized_medium_level = random.choice(medium_level_words)

    return randomized_medium_level


def hard_level():
    # 8 letters words
    hard_level_words = ["interest", "position", "industry", "research", "minister", "evidence", "question", "language",
                        "business", "magazine", "elephant", "notebook"]

    randomized_hard_words = random.choice(hard_level_words)

    return randomized_hard_words


def expert_level():
    # 12 letters words
    expert_level_words = ["unemployment", "organisation", "conversation", "relationship", "introduction",
                          "contribution", "organization", "distribution", "construction", "grandmother", "magnetomotor"]
    randomized_expert_words = random.choice(expert_level_words)

    return randomized_expert_words


# def evaluate():
#     if player_letters == None or len(player_letters) != 1 or (player_letters in result) or (guess in missed):
#         return None, False

print()
print()
command = input("*Choose command: ")
guessed_letters = []
used_letters = []

if command == "1":
    print()
    print("* You choosed - | Easy level | *")
    print()
    for _ in range(len(easy_level())):
        # print(f"{guessed_letters}")
        print("_ ", end="")
    print("  --> 4 letters word !")

    rndm_word = easy_level()

    while True:
        player_letters = input("Guess the word: ").lower()

        if player_letters in rndm_word:
            guessed_letters.append(player_letters)
            used_letters.append(player_letters)
        else:
            used_letters.append(player_letters)

        if player_letters in used_letters:
            print(f'Used letters: {", ".join(used_letters)}')
            print(f'Dont use used letters ! :)')


    print()
    print(" ".join(guessed_letters))
    print(f'{"_ " * len(rndm_word)}', end="")
    print()
    print()
    print(f"guesed -{guessed_letters}")
    print()
    print(player_letters)

    print(f"rndm--{rndm_word}")
    print()
