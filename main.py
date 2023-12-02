import sys
from random import randint
import os
from players import Game, Player
from cards import *
import bot


# Gets card information from given file and creates list of cards.
def parse_file(filename, game):
    f = open(filename, "r")
    idea = f.readline()
    if idea == "":
        print("Empty file given")
    else:
        duplicates = f.readline()
        while duplicates != "":
            duplicates = int(duplicates)
            for i in range(0, duplicates):
                game.cards.append(idea.strip("\n"))
            idea = f.readline()
            duplicates = f.readline()
    game.card_count = len(game.cards)


# Picks a random card from the deck
def pick_card(game):
    i = randint(0, len(game.cards) - 1)
    card = game.cards[i]
    del game.cards[i]
    game.card_count -= 1
    return card

# Main
def main():
    # Create Game object that will store info about the game.
    game = Game()
    # Determine if game will be played automatically by a WIP bot or by hand using command line.
    game_type = input("Is the game manual or automatic? M/A:\n")
    # Game behaviour when game type is set to automatic.
    if game_type == "A":
        # Determine amount of players and create Player objects for each.
        player_count = int(input("Give number of players:\n"))
        for i in range(0, player_count):
            player = Player()
            player.change_name(f"player{i + 1}")
            game.add_player(player)
        # Get file containing card info and create deck from it.
        filename = input("Give name of file containing card info:\n")
        parse_file(filename, game)
        # End game if no cards are left - else continue.
        for player in game.players:
            if game.card_count == 0:
                sys.exit("Game Over. Cards ran out.")
            elif game.card_count > 0:
                # Checks if current player's turn should be skipped
                if player.skips == 0:
                    # Checks for any active replicates for cnt calculation
                    game.check_replicates()
                    print("Current player:", player.name)
                    print("----------")
                    # Pick card and execute corresponding function
                    card = pick_card(game)
                    print("Card:", card)
                    # Sustainability loop is separated from everything else as it has a fundamentally different effect
                    # on the game and is not added to a player's deck.
                    if card == "Sustainability loop" or player.loop:
                        if player.loop:
                            player.add_card(card)
                        sustainability_loop(player)
                    else:
                        # Currently these functions do nothing as the logic of the bot has not been implemented.
                        player.add_card(card)
                        if card == "Diabetes":
                            bot.diabetes(game, player)
                        if card == "Union strike":
                            bot.union_strike(game, player)
                        if card == "Carcinogenicity":
                            bot.carcinogenicity(game, player)
                        if card == "007":
                            bot.bond(game, player)
                        if card == "IPR":
                            bot.ipr(game, player)
                        if card == "Regulations":
                            bot.regulations(game, player)
                        if card == "Sweat analysis":
                            bot.sweat_analysis(game, player)
                        if card == "Critical flaw":
                            bot.critical_flaw(player)
                        if card == "Terrorism":
                            bot.terrorism(game, player)
                        if card == "Structural health monitoring":
                            bot.structural_health_monitoring(game, player)
                        if card == "Student recruitment":
                            bot.student_recruitment(game, player)
                        if card == "Recycling":
                            bot.recycling(game, player)
                        if card == "Material choices":
                            bot.material_choices(game, player)
                        if card == "X (Twitter)":
                            bot.twitter(game, player)
                        if card == "Greenwashing":
                            bot.greenwashing(game, player)
                        if card == "Temperature":
                            bot.temperature(game, player)
                        if card == "Increased production":
                            bot.increased_production(game, player)
                        if card == "Water pollution":
                            bot.water_pollution(game, player)
                        if card == "Cleaning":
                            bot.cleaning(game, player)
                        if card == "Aerosols":
                            bot.aerosols(game, player)
                        if card == "Enzymes":
                            bot.enzymes(game, player)
                        if card == "CNT Spray":
                            bot.cnt_spray(game, player)
                        if card == "CNT Length":
                            bot.cnt_length(game, player)
                        if card == "Mycotoxins":
                            bot.mycotoxins(game, player)
                        if card == "Customization":
                            bot.customization(game, player)
                        if card == "Gender equality":
                            bot.gender_equality(game, player)
                        if card == "Bulletproof vests":
                            bot.bulletproof_vests(game, player)
                        if card == "Fossil fuels":
                            bot.fossil_fuels(game, player)
                        if card == "Production location":
                            bot.production_location(game, player)
                        if card == "Budget":
                            bot.budget(game, player)
                else:
                    # If a player's turn was skipped, reduce remaining skips by one and inform players.
                    player.skips -= 1
                    print("----------")
                    print(f"Your next {player.skips} turns will be skipped")
                    print("----------")
                # Reduce remaining turns with strike if player has strike active.
                if player.strike:
                    player.strike -= 1
                # Resets player's cnts to 0 if they are negative
                game.check_cnts()
                # Give information about a player's game state
                print(f"Player {player.name} CNTs:", player.cnts)
                print(f"Discard_pile for {player.name}:\n{player.discard_pile}")
                print(f"Sustainability loop for {player.name}:\n{player.sustainability_loop}")
                print(f"Cards left in the deck: {game.card_count}\n")
                print("__________________________________________________________________________________________")
    # Game behaviour when game type is set to manual.
    elif game_type == "M":
        # Get player information one by one and create Player objects.
        name = input("Give player name. Continue with empty line:\n")
        while name != "":
            player = Player()
            player.change_name(name)
            game.add_player(player)
            name = input("Give player name. Continue with empty line:\n")
        # Get file containing card info and create deck.
        filename = input("Give name of file containing card info:\n")
        parse_file(filename, game)
        draw = input("Press enter to start game:\n")
        # Game progresses currently identically as in the automatic execution except cards actually have effects here.
        while draw == "" and game.card_count > 0:
            for player in game.players:
                if player.skips == 0:
                    game.check_replicates()
                    print("Current player:", player.name)
                    draw = input("Press enter to draw a card.\n")
                    print("----------")
                    card = pick_card(game)
                    print("Card:", card)
                    if card == "Sustainability loop" or player.loop:
                        if player.loop and card != "Sustainability loop":
                            player.add_card(card)
                        sustainability_loop(player)
                    else:
                        player.add_card(card)
                        if card == "Diabetes":
                            diabetes(game, player)
                        if card == "Union strike":
                            union_strike(game, player)
                        if card == "Carcinogenicity":
                            carcinogenicity(game, player)
                        if card == "007":
                            bond(game, player)
                        if card == "IPR":
                            ipr(game, player)
                        if card == "Regulations":
                            regulations(game, player)
                        if card == "Sweat analysis":
                            sweat_analysis(game, player)
                        if card == "Critical flaw":
                            critical_flaw(player)
                        if card == "Terrorism":
                            terrorism(game, player)
                        if card == "Structural health monitoring":
                            structural_health_monitoring(game, player)
                        if card == "Student recruitment":
                            student_recruitment(game, player)
                        if card == "Recycling":
                            recycling(player)
                        if card == "Material choices":
                            material_choices(player)
                        if card == "X (Twitter)":
                            twitter(game, player)
                        if card == "Greenwashing":
                            greenwashing(game, player)
                        if card == "Temperature":
                            temperature(game, player)
                        if card == "Increased production":
                            increased_production(game, player)
                        if card == "Water pollution":
                            water_pollution(game, player)
                        if card == "Cleaning":
                            cleaning(game, player)
                        if card == "Aerosols":
                            aerosols(game, player)
                        if card == "Enzymes":
                            enzymes(game, player)
                        if card == "CNT Spray":
                            cnt_spray(game, player)
                        if card == "CNT Length":
                            cnt_length(game, player)
                        if card == "Mycotoxins":
                            mycotoxins(game, player)
                        if card == "Customization":
                            customization(game, player)
                        if card == "Gender equality":
                            gender_equality(game, player)
                        if card == "Bulletproof vests":
                            bulletproof_vests(game, player)
                        if card == "Fossil fuels":
                            fossil_fuels(game, player)
                        if card == "Production location":
                            production_location(game, player)
                        if card == "Budget":
                            budget(game, player)
                else:
                    player.skips -= 1
                    print("----------")
                    print(f"Your next {player.skips} turns will be skipped")
                    print("----------")
                if player.strike:
                    player.strike -= 1
                game.check_cnts()
                print(f"Player {player.name} CNTs:", player.cnts)
                print(f"Discard_pile for {player.name}:\n{player.discard_pile}")
                print(f"Sustainability loop for {player.name}:\n{player.sustainability_loop}")
                print("----------")
                # Clear command line between turns to keep it clean
                input("Press enter to hide drawn card.\n")
                os.system('cls')
                print("----------")
                print(f"Cards left in the deck: {game.card_count}\n")
                print("__________________________________________________________________________________________")

if __name__ == "__main__":
    main()
