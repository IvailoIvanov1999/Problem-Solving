cards = input().split()
count_shuffles = int(input())

for _ in range(count_shuffles):
    first_half = []
    second_half = []

    for idx in range(1, len(cards) - 1):

        card = cards[idx]
        if idx < len(cards) / 2:
            first_half.append(card)
        else:
            second_half.append(card)

    shuffled = []
    first_h = 0
    second_h = 0

    for idx in range(len(first_half) * 2):
        if idx % 2 == 0:
            shuffled.append(second_half[second_h])
            second_h += 1
        else:
            shuffled.append(first_half[first_h])
            first_h += 1
    cards = [cards[0]] + shuffled + [cards[-1]]

print(cards)
