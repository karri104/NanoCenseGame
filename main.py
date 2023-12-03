from os import system, path
from players import Game, Player, Holder
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
    f.close()


# Picks a random card from the deck
def pick_card(game):
    i = randint(0, len(game.cards) - 1)
    card = game.cards[i]
    del game.cards[i]
    game.card_count -= 1
    return card


# Compiles data into more human readable form
def compile_data(compile_now, output_file, holder, player_count, end_reason, avg_points, avg_cnt_count, length, turns, avg_loop_card_count, avg_loop_count, avg_loop_length, avg_strikes, avg_skips):
    if compile_now:
        output_file.write(f"Player count: {player_count}\n")
        output_file.write(f"Game count: {holder.game_count}\n")
        output_file.write(f"Games that ended from cards running out: {holder.out_of_cards}\n")
        output_file.write(f"Games that ended from a player getting 12 CNT: {holder.winner}\n")
        output_file.write(f"Average points per game: {holder.total_points:.2f}\n")
        output_file.write(f"Average CNTs per game: {holder.total_cnts:.2f}\n")
        output_file.write(f"Average game length: {holder.total_length}min\n")
        output_file.write(f"Average turns per game: {holder.total_turns}\n")
        output_file.write(f"Average sustainability loop cards per player: {holder.total_loop_card_count:.2f}\n")
        output_file.write(f"Average turns skipped from failed sustainability loop formation: {holder.total_loop_count:.2f}\n")
        output_file.write(f"Average sustainability loop length: {holder.total_loop_length:.2f}\n")
        output_file.write(f"Average skips per player: {holder.total_skips:.2f}\n")
        output_file.write(f"Average strikes per player: {holder.total_strikes:.2f}\n")
        output_file.write("\n")
        output_file.write("\n")
        output_file.write("\n")
        holder.total_points = 0
        holder.total_cnts = 0
        holder.total_length = 0
        holder.total_turns = 0
        holder.total_loop_card_count = 0
        holder.total_loop_count = 0
        holder.total_loop_length = 0
        holder.total_strikes = 0
        holder.total_skips = 0
        holder.winner = 0
        holder.out_of_cards = 0
    else:
        if end_reason == "Out of cards":
            holder.out_of_cards += 1
        elif end_reason == "Player reached 12 CNT":
            holder.winner += 1
        holder.total_points = avg_points
        holder.total_cnts = avg_cnt_count
        holder.total_length = length
        holder.total_turns = turns
        holder.total_loop_card_count = avg_loop_card_count
        holder.total_loop_count = avg_loop_count
        holder.total_loop_length = avg_loop_length
        holder.total_strikes = avg_strikes
        holder.total_skips = avg_skips


# Processes game data to be used in game analysis
def process_data(game, reason, f, output_file, holder):
    # Get game id
    game_id = game.id

    # Calculate points for each player
    for player in game.players:
        if len(player.sustainability_loop) >= 4:
            length = len(player.sustainability_loop) - 4
            player.points = player.cnts + 1 + length * 0.5
        else:
            player.points = player.cnts

    # Get player count. Not used in analysis as this info is included in game_id. It is used in below calcs though.
    player_count = len(game.players)

    # Get game length in minutes
    length = game.turn * game.turn_length

    # Get number of turns in the game
    turns = game.turn

    # Get game end reason
    end_reason = reason

    # Get average cnts
    # Get average sustainability loop cards obtained
    # Get average turns skipped by failing to create a sustainability loop
    # Get average sustainability loop length
    # Get average points
    # Get average strikes
    # Get average skips
    total_cnt_count = 0
    total_loop_card_count = 0
    total_loop_count = 0
    total_loop_length = 0
    total_points = 0
    total_strikes = 0
    total_skips = 0
    for player in game.players:
        total_cnt_count += player.cnts
        total_loop_card_count += player.loop_card_count
        total_loop_count += player.loop_count
        total_loop_length += len(player.sustainability_loop)
        total_points += player.points
        total_strikes += player.strike_count
        total_skips += player.skip_count
    avg_cnt_count = total_cnt_count / player_count
    avg_loop_card_count = total_loop_card_count / player_count
    avg_loop_count = total_loop_count / player_count
    avg_loop_length = total_loop_length / player_count
    avg_points = total_points / player_count
    avg_strikes = total_strikes / player_count
    avg_skips = total_skips / player_count

    # Write above info to file
    f.write(f"{game_id: <12}\t{end_reason: <22}\t{avg_points:.2f}\t\t{avg_cnt_count:.2f}\t\t{length}\t\t{turns}\t\t{avg_loop_card_count:.2f}\t\t{avg_loop_count:.2f}\t\t{avg_loop_length:.2f}\t\t{avg_strikes:.2f}\t\t{avg_skips:.2f}\n")

    # Send info to info compiler
    compile_data(False, output_file, holder, player_count, end_reason, avg_points, avg_cnt_count, length, turns, avg_loop_card_count,
                 avg_loop_count, avg_loop_length, avg_strikes, avg_skips)


# Main
def main():
    # Determine if game will be played automatically by a bot or by hand using command line.
    game_type = input("Is the game manual or automatic? M/A:\n")
    # Game behaviour when game type is set to automatic.
    if game_type == "A":
        # Create output file
        output = "output.txt"
        exists = True
        i = 0
        while exists:
            i += 1
            output = f"output{i}.txt"
            exists = path.isfile(output)
        f = open(output, "a")
        f.write("Game_id\t\tEnd_reason\t\tAvg_points\tAvg_cnts\tGame_length\tGame_turns\tAvg_loop_cards\tAvg_loop_skips\tAvg_loop_length\tAvg_strikes\tAvg_skips\n")
        output_compiled = f"output{i}_compiled.txt"
        output_file = open(output_compiled, "a")
        # Determine the amount of games to be played per player amount.
        game_count = int(input("Give number of games to be simulated per playercount:\n"))
        holder = Holder()
        holder.game_count = game_count
        for i in range(3, 7):
            player_count = i
            for n in range(0, game_count):
                # Create Game object that will store info about the game.
                game = Game()
                game.id = f"game{i}-{n + 1}"
                for j in range(0, player_count):
                    player = Player()
                    player.change_name(f"player{j + 1}")
                    game.add_player(player)
                # Get file containing card info and create deck from it.
                parse_file("cards.txt", game)
                winner = False
                loop = True
                while loop:
                    for player in game.players:
                        # End game if no cards are left - else continue.
                        if game.card_count == 0:
                            # Print game end reason and start data processing for output
                            print(f"Game {n + 1} ended with {i} players. Cards ran out.")
                            process_data(game, "Out of cards", f, output_file, holder)
                            loop = False
                            break
                        elif game.card_count > 0:
                            # Checks if current player's turn should be skipped
                            if player.skips == 0:
                                # Checks for any active replicates for cnt calculation
                                game.check_replicates()
                                # Pick card and execute corresponding function
                                card = pick_card(game)
                                # Sustainability loop is separated from everything else as it has a fundamentally different
                                # effect on the game and is not added to a player's deck.
                                if card == "Sustainability loop" or player.loop:
                                    if card == "Sustainability loop":
                                        # Data used in analysis
                                        player.loop_card_count += 1
                                    if player.loop:
                                        # Data used in analysis
                                        player.loop_count += 1
                                        player.add_card(card)
                                    sustainability_loop(player, game_type)
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
                                        bot.recycling(player)
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
                                # If a player's turn was skipped, reduce remaining skips by one.
                                player.skips -= 1
                            if player.strike:
                                player.strike -= 1
                            # Resets player's cnts to 0 if they are negative
                            winner = game.check_cnts()
                        if winner:
                            # Print game end reason and start data processing for output
                            print(f"Game {n + 1} ended with {i} players. Player reached 12 CNT.")
                            process_data(game, "Player reached 12 CNT", f, output_file, holder)
                            loop = False
                            break
                    game.turn += 1
            compile_data(True, output_file, holder, player_count, None, None, None, None, None, None, None, None, None, None)
        f.close()
        output_file.close()
    # Game behaviour when game type is set to manual.
    elif game_type == "M":
        # Create Game object that will store info about the game.
        game = Game()
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
                        sustainability_loop(player, game_type)
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
                system('cls')
                print("----------")
                print(f"Cards left in the deck: {game.card_count}\n")
                print("__________________________________________________________________________________________")


if __name__ == "__main__":
    main()
