import random
import os
from players import Game, Player


def parse_file(filename, game):
    cards = {}
    card_count = 0
    invalid_ids = []
    f = open(filename, "r")
    idea = f.readline()
    if idea == "":
        print("Empty file given")
    else:
        parts = idea.split("\\n")
        duplicates = f.readline()
        i = 1
        while idea != [] and duplicates != "":
            duplicates = int(duplicates)
            if duplicates == 0:
                invalid_ids.append(i)
            parts = idea.split("\\n")
            cards[i] = [parts, duplicates]
            card_count += duplicates
            idea = f.readline()
            duplicates = f.readline()
            i += 1
    game.cards = cards
    game.card_count = card_count
    game.invalid_ids = invalid_ids


def pick_card(game):
    card_id = random.randint(1, len(game.cards))
    while card_id in game.invalid_ids:
        card_id = random.randint(1, len(game.cards))
    card = game.cards[card_id]
    if card[1] != 0:
        card[1] -= 1
        game.card_count -= 1
        if card[1] == 0:
            game.invalid_ids.append(card_id)
    return card

def main():
    game = Game()
    name = input("Give player name. Continue with empty line:\n")
    while name != "":
        player = Player(name)
        game.add_player(player)
        name = input("Give player name. Continue with empty line:\n")

    filename = input("Give name of file containing card info:\n")
    parse_file(filename, game)

    draw = input("Press enter to draw a card.\n")
    while draw == "" and game.card_count > 0:
        card = pick_card(game)
        print("__________________________________________________________________________________________")
        for part in card[0]:
            print(part)
        print("----------")
        clear = input("Press enter to hide drawn card.\n")
        os.system('cls')
        print("----------")
        print(f"Cards left in the deck: {game.card_count}\n")
        print("__________________________________________________________________________________________")
        draw = input("Press enter to draw another card.\n")

if __name__ == "__main__":
    main()
