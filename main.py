import random
import os
from players import Game, Player
import cards


def parse_file(filename, game):
    cards = []
    card_count = 0
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
            for i in range(0, duplicates):
                game.cards.append(parts)
            parts = idea.split("\\n")
            idea = f.readline()
            duplicates = f.readline()
            i += 1
    game.card_count = len(game.cards)


def pick_card(game):
    i = random.randint(0, len(game.cards) - 1)
    card = game.cards[i]
    del game.cards[i]
    game.card_count -= 1
    return card

def main():
    game = Game()
    name = input("Give player name. Continue with empty line:\n")
    while name != "":
        player = Player()
        player.change_name(name)
        game.add_player(player)
        name = input("Give player name. Continue with empty line:\n")

    filename = input("Give name of file containing card info:\n")
    parse_file(filename, game)
    print(game.cards)
    draw = input("Press enter to draw a card.\n")
    while draw == "" and game.card_count > 0:
        print("hi")
        for player in game.players:
            print("Player name:", player.name)
            if player.skips == 0:
                card = pick_card(game)
                print("Whole card", card)
                # Add card function calls here
                print("----------")
                clear = input("Press enter to hide drawn card.\n")
                os.system('cls')
                print("----------")
                print(f"Cards left in the deck: {game.card_count}\n")
                print("__________________________________________________________________________________________")
            else:
                player.skips -= 1
                print("----------")
                print(f"Your next {player.skips} will be skipped")
                print("----------")
        draw = input("Press enter to draw another card.\n")

if __name__ == "__main__":
    main()
