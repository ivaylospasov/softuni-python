deck_of_cards = input().split()
shuffle_count = int(input())

print(deck_of_cards)


for turn in range(shuffle_count):
    shuffled_deck = []
    first_half = deck_of_cards[:len(deck_of_cards) // 2]
    second_half = deck_of_cards[len(deck_of_cards) // 2:]
    for index in range(len(deck_of_cards) // 2):
        shuffled_deck.append(first_half[index])
        shuffled_deck.append(second_half[index])
    deck_of_cards = shuffled_deck

print(deck_of_cards)
