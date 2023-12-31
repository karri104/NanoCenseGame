#######################################################################################################################
# Code created by karri104
#######################################################################################################################

from random import randint


# Responsible for distributing cnts to players depending on strikes and replicates.
def give_cnts(game, player, cnts):
    if not player.check_strike():
        player.cnts += cnts
        if len(game.replicates) != 0:
            for replicate in game.replicates:
                if not replicate.check_strike():
                    replicate.cnts += cnts
                else:
                    replicate.cnts += int(cnts / 2)
    else:
        player.cnts += int(cnts / 2)
        if len(game.replicates) != 0:
            for replicate in game.replicates:
                if not replicate.check_strike():
                    replicate.cnts += int(cnts / 2)
                else:
                    replicate.cnts += int(cnts / 4)
    game.replicates = []


# Randomly creates sustainability loops depending on current discard_pile size.
# Can currently only create one sustainability loop even though in the actual game you can create multiple
def sustainability_loop(player, game_type):
    # Generate random number to be used in calculating successes
    num = randint(1, 10000)
    # If no sustainability loop exists yet
    if len(player.discard_pile) >= 3 and len(player.sustainability_loop) == 0:
        # Percent thresholds for success depending on pile_size. 100 = 1%
        # e.g. 3500 means 35% of the time making a sustainability loop succeeds when discard_pile
        # has exactly 3 cards
        chances = [3500, 5000, 7500, 8750, 9375, 10000]
        # Creating a sustainability loop always works when there are at least 8 cards in discard_pile
        if len(player.discard_pile) >= 8:
            probability = 10000
        else:
            probability = chances[len(player.discard_pile) - 3]
        # If loop generation is successful, move a random amount of cards from discard_pile to sustainability_loop
        # Skip a turn otherwise.
        if num <= probability:
            player.loop = False
            used_cards = randint(3, len(player.discard_pile))
            for used_card in range(0, used_cards - 1):
                card_index = randint(0, len(player.discard_pile) - 1)
                card = player.discard_pile[card_index]
                player.sustainability_loop.append(card)
                del player.discard_pile[card_index]
        else:
            if game_type == "M":
                print("Didn't succeed in making a sustainability loops.\nYour turn is skipped. Try again next turn")
            player.loop = True
    # If a sustainability loop exists already. Works with same logic as normal creation. Just has different values.
    elif len(player.discard_pile) >= 1 and len(player.sustainability_loop) >= 3:
        chances = [50000, 7500, 8750, 9375, 10000]
        if len(player.discard_pile) >= 5:
            probability = 10000
        else:
            probability = chances[len(player.discard_pile)]
        if num <= probability:
            player.loop = False
            used_cards = randint(1, len(player.discard_pile))
            for used_card in range(0, used_cards - 1):
                card_index = randint(0, len(player.discard_pile) - 1)
                card = player.discard_pile[card_index]
                player.sustainability_loop.append(card)
                del player.discard_pile[card_index]
        else:
            if game_type == "M":
                print("Didn't succeed in making a sustainability loops.\nYour turn is skipped. Try again next turn")
            player.loop = True
    else:
        if game_type == "M":
            print("Didn't succeed in making a sustainability loops.\nYour turn is skipped. Try again next turn")
        player.loop = True

#################################
# Following functions contain the logic for different cards.
# These do not reflect current game balancing changes.
# Correct values and general functionality is outlined in Canva.
#################################


def diabetes(game, player):
    choice = input("A or B?\n")
    if choice == "A":
        num = randint(1, 20)
        if num >= 14:
            give_cnts(game, player, 3)
        else:
            if not player.check_immunity():
                player.cnts -= 3
    if choice == "B":
        if not player.check_immunity():
            player.cnts -= 1


def union_strike(game, player):
    choice = input("A or B?\n")
    if choice == "A":
        if not player.check_immunity():
            player.cnts -= 3
        for contestant in game.players:
            if contestant != player:
                contestant.strike += 2
    else:
        num = randint(1, 20)
        if num >= 10:
            pass
        else:
            if len(game.replicates) != 0:
                for replicate in game.replicates:
                    replicate.cnts += 1
                game.replicates = []
            for contestant in game.players:
                if contestant != player:
                    if not contestant.check_strike():
                        contestant.cnts += 1
                    else:
                        contestant.cnts += int(1 / 2)


def carcinogenicity(game, player):
    choice = input("A or B?\n")
    if choice == "A":
        for contestant in game.players:
            contestant.cnts -= 1
        if player.check_immunity():
            # NOTE: DO NOT ADD REPLICANT OR STRIKE TO THIS AS IT'S NOT ACTUALLY GIVING
            # CNTS RATHER JUST GIVING BACK THE CNT TAKEN AWAY IN ABOVE FOR LOOP
            player.cnts += 1
    else:
        num = randint(1, 20)
        if num >= 19:
            for contestant in game.players:
                if contestant != player:
                    contestant.cnts -= 2
        else:
            if not player.check_immunity():
                player.cnts -= 2


def bond(game, player):
    choice = input("A or B?\n")
    if choice == "A":
        num = randint(1, 20)
        if num >= 14:
            bests = [0, 0]
            ids = [0, 0]
            for i, contestant in enumerate(game.players):
                if contestant != player:
                    for j, best in enumerate(bests):
                        if contestant.cnts > best:
                            bests[j] = contestant.cnts
                            ids[j] = i
            game.players[ids[0]].cnts -= 2
            game.players[ids[1]].cnts -= 2
    else:
        pass


def ipr(game, player):
    choice = input("A or B?\n")
    if choice == "A":
        num = randint(1, 20)
        if num >= 10:
            best = 0
            index = 0
            for i, contestant in enumerate(game.players):
                if contestant != player:
                    if contestant.cnts > best:
                        best = contestant.cnts
                        index = i
            game.players[index].cnts -= 2
            give_cnts(game, player, 2)
        else:
            if not player.check_immunity():
                player.cnts -= 1
    else:
        if not player.check_immunity():
            player.cnts -= 1


def regulations(game, player):
    choice = input("A or B?\n")
    if choice == "A":
        num = randint(1, 20)
        if num >= 14:
            give_cnts(game, player, 2)
        else:
            if not player.check_immunity():
                player.cnts -= 2
    else:
        if not player.check_immunity():
            player.cnts -= 1


def sweat_analysis(game, player):
    choice = input("A or B?\n")
    num = randint(1, 20)
    if choice == "A":
        if num >= 8:
            give_cnts(game, player, 1)
        else:
            pass
    else:
        if num >= 15:
            give_cnts(game, player, 4)
        else:
            if not player.check_immunity():
                player.cnts -= 3


def critical_flaw(player):
    choice = input("A or B?\n")
    if choice == "A":
        player.immune = True
    else:
        player.replicate = True


def terrorism(game, player):
    choice = input("A or B?\n")
    if choice == "A":
        num = randint(1, 20)
        if num >= 4:
            give_cnts(game, player, 3)
        else:
            if not player.check_immunity():
                player.cnts -= 4
                player.skips += 2
    else:
        give_cnts(game, player, 1)


def structural_health_monitoring(game, player):
    choice = input("A or B?\n")
    num = randint(1, 20)
    if choice == "A":
        if num >= 10:
            give_cnts(game, player, 2)
        else:
            if not player.check_immunity():
                player.cnts -= 2
    else:
        if num >= 10:
            for competitor in game.players:
                if competitor != player:
                    competitor.cnts -= 2
        else:
            if len(game.replicates) != 0:
                for replicate in game.replicates:
                    replicate.cnts += 1
                game.replicates = []
            for contestant in game.players:
                if contestant != player:
                    if not contestant.check_strike():
                        contestant.cnts += 1
                    else:
                        contestant.cnts += int(1 / 2)


def student_recruitment(game, player):
    choice = input("A or B?\n")
    num = randint(1, 20)
    if choice == "A":
        if num >= 11:
            give_cnts(game, player, 3)
        else:
            if not player.check_immunity():
                player.cnts -= 2
    else:
        if num >= 5:
            give_cnts(game, player, 2)
        else:
            if not player.check_immunity():
                player.cnts -= 4


def recycling(player):
    if not player.check_immunity():
        player.cnts -= 1


def material_choices(player):
    give_cnts(game, player, 1)


def twitter(game, player):
    choice = input("A or B?\n")
    if choice == "A":
        num = randint(1, 20)
        if num >= 10:
            give_cnts(game, player, 3)
        else:
            if not player.check_immunity():
                player.cnts -= 3
    else:
        pass


def greenwashing(game, player):
    choice = input("A or B?\n")
    if choice == "A":
        num = randint(1, 20)
        if num >= 10:
            give_cnts(game, player, 3)
        else:
            if not player.check_immunity():
                player.cnts -= 3
    else:
        if not player.check_immunity():
            player.cnts -= 1


def temperature(game, player):
    choice = input("A or B?\n")
    num = randint(1, 20)
    if choice == "A":
        if num >= 10:
            give_cnts(game, player, 1)
        else:
            if not player.check_immunity():
                player.cnts -= 1
    else:
        if num >= 10:
            for competitor in game.players:
                if competitor != player:
                    competitor.cnts -= 1
        else:
            if len(game.replicates) != 0:
                for replicate in game.replicates:
                    if not replicate.check_strike():
                        replicate.cnts += 1
                    else:
                        replicate.cnts += int(1 / 2)
                game.replicates = []
            for contestant in game.players:
                if contestant != player:
                    if not contestant.check_strike():
                        contestant.cnts += 1
                    else:
                        contestant.cnts += int(1 / 2)


def increased_production(game, player):
    choice = input("A or B?\n")
    if choice == "A":
        num = randint(1, 20)
        if num >= 10:
            give_cnts(game, player, 3)
        else:
            if not player.check_immunity():
                player.cnts -= 3
    else:
        give_cnts(game, player, 1)


def water_pollution(game, player):
    choice = input("A or B?\n")
    if choice == "A":
        num = randint(1, 20)
        if num >= 10:
            give_cnts(game, player, 5)
        else:
            if not player.check_immunity():
                player.cnts -= 5
    else:
        pass


def cleaning(game, player):
    choice = input("A or B?\n")
    num = randint(1, 20)
    if choice == "A":
        if num < 10:
            if not player.check_immunity():
                player.cnts -= 1
    else:
        if num >= 19:
            give_cnts(game, player, 5)
        else:
            if not player.check_immunity():
                player.cnts -= 3


def aerosols(game, player):
    choice = input("A or B?\n")
    if choice == "A":
        num = randint(1, 20)
        if num >= 4:
            give_cnts(game, player, 1)
        else:
            if not player.check_immunity():
                player.cnts -= 1
    else:
        if not player.check_immunity():
            player.cnts -= 1


def enzymes(game, player):
    choice = input("A or B?\n")
    if choice == "A":
        num = randint(1, 20)
        if num == 20:
            give_cnts(game, player, 6)
        else:
            if not player.check_immunity():
                player.cnts -= 2
    else:
        if not player.check_immunity():
            player.cnts -= 1


def cnt_spray(game, player):
    choice = input("A or B?\n")
    if choice == "A":
        num = randint(1, 20)
        if num >= 10:
            give_cnts(game, player, 2)
        else:
            if not player.check_immunity():
                player.cnts -= 3
    else:
        give_cnts(game, player, 1)


def cnt_length(game, player):
    choice = input("A or B?\n")
    if choice == "A":
        give_cnts(game, player, 2)
        if not player.immune:
            player.skips += 1
    else:
        if not player.check_immunity():
            player.cnts -= 1


def mycotoxins(game, player):
    choice = input("A or B?\n")
    if choice == "A":
        num = randint(1, 20)
        if num >= 14:
            give_cnts(game, player, 3)
        else:
            if not player.check_immunity():
                player.cnts -= 2
    else:
        give_cnts(game, player, 1)


def customization(game, player):
    choice = input("A or B?\n")
    if choice == "A":
        give_cnts(game, player, 2)
        if not player.immune:
            player.skips += 1
    else:
        if not player.check_immunity():
            player.cnts -= 1


def gender_equality(game, player):
    choice = input("A or B?\n")
    if choice == "A":
        num = randint(1, 20)
        if num >= 10:
            give_cnts(game, player, 2)
        else:
            if not player.check_immunity():
                player.cnts -= 2
    if choice == "B":
        give_cnts(game, player, 1)


def bulletproof_vests(game, player):
    choice = input("A or B?\n")
    if choice == "A":
        pass
    else:
        num = randint(1, 20)
        if 1 <= num <= 5:
            if not player.check_immunity():
                player.cnts -= 2
        elif 6 <= num <= 10:
            if not player.check_immunity():
                player.cnts -= 1
        elif 11 <= num <= 15:
            give_cnts(game, player, 1)
        else:
            give_cnts(game, player, 2)


def fossil_fuels(game, player):
    give_cnts(game, player, 1)


def production_location(game, player):
    choice = input("A or B?\n")
    num = randint(1, 20)
    if choice == "A":
        if num >= 10:
            give_cnts(game, player, 2)
        else:
            if not player.check_immunity():
                player.cnts -= 2
    else:
        if num >= 10:
            give_cnts(game, player, 3)
        else:
            if not player.check_immunity():
                player.cnts -= 4


def budget(game, player):
    choice = input("A or B?\n")
    num = randint(1, 20)
    if choice == "A":
        if len(game.replicates) != 0:
            for replicate in game.replicates:
                replicate.cnts += 1
            game.replicates = []
        for contestant in game.players:
            if not contestant.check_strike():
                contestant.cnts += 1
            else:
                contestant.cnts += int(1 / 2)
    else:
        if num >= 17:
            give_cnts(game, player, 3)
        else:
            if not player.check_immunity():
                player.cnts -= int(player.cnts / 3)
