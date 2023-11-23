import random
import os
import players


def parse_file(filename):
    cards = {}
    card_count = 0
    invalid_ids = []
    f = open(filename, "r")
    idea = f.readline()
    if idea == "":
        print("Empty file given")
    else:
        duplicates = f.readline()
        i = 1
        while idea != "" and duplicates != "":
            duplicates = int(duplicates)
            if duplicates == 0:
                invalid_ids.append(i)
            cards[i] = [idea, duplicates]
            card_count += duplicates
            idea = f.readline()
            duplicates = f.readline()
            i += 1
    return cards, card_count, invalid_ids


def pick_card(cards, card_count, invalid_ids):
    card_id = random.randint(1, len(cards))
    while card_id in invalid_ids:
        card_id = random.randint(1, len(cards))
    card = cards[card_id]
    if card[1] != 0:
        card[1] -= 1
        card_count -= 1
        if card[1] == 0:
            invalid_ids.append(card_id)
    return card[0], invalid_ids, card_count


def main():
    filename = input("Give name of file containing card info:\n")
    cards, card_count, invalid_ids = parse_file(filename)

    draw = input("Press enter to draw a card.\n")
    while draw == "" and card_count > 0:
        card, invalid_ids, card_count = pick_card(cards, card_count, invalid_ids)
        parts = card.split("\\n")
        print("__________________________________________________________________________________________")
        for part in parts:
            print(part)
        print("----------")
        clear = input("Press enter to hide drawn card.\n")
        os.system('cls')
        print("----------")
        print(f"Cards left in the deck: {card_count}\n")
        print("__________________________________________________________________________________________")
        draw = input("Press enter to draw another card.\n")

if __name__ == "__main__":
    main()
