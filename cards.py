from random import randint


def sustainability_loop(player):
    pile_size = len(player.discard_pile)
    num = randint(1, 10000)
    if pile_size >= 3 and len(player.sustainability_loop) == 0:
        chances = [3500, 5000, 7500, 8750, 9375, 10000]
        probability = chances[pile_size - 1]
        if num <= probability:
            player.loop = False
            used_cards = randint(3, pile_size)
            for used_card in range(0, used_cards):
                card_index = randint(0, len(player.discard_pile) - 1)
                card = player.discard_pile[card_index]
                del player.discard_pile[card_index]
                player.sustainability_loop.append(card)
        else:
            print("Didn't succeed in making a sustainability loops.\nYour turn is skipped. Try again next turn")
            player.loop = True
    elif pile_size >= 1 and len(player.sustainability_loop) >= 3:
        chances = [50000, 7500, 8750, 9375, 10000]
        probability = chances[pile_size - 1]
        if num <= probability:
            player.loop = False
            used_cards = randint(1, pile_size)
            for used_card in range(0, used_cards):
                card_index = randint(0, len(player.discard_pile) - 1)
                card = player.discard_pile[card_index]
                del player.discard_pile[card_index]
                player.sustainability_loop.append(card)
        else:
            print("Didn't succeed in making a sustainability loops.\nYour turn is skipped. Try again next turn")
            player.loop = True
    else:
        print("Didn't succeed in making a sustainability loops.\nYour turn is skipped. Try again next turn")
        player.loop = True

def diabetes(game, player):
    choice = input("A or B?\n")
    if choice == "A":
        num = randint(1, 20)
        if num >= 14:
            if not player.check_strike():
                player.cnts += 3
                if len(game.replicates) != 0:
                    for replicate in game.replicates:
                        if not replicate.check_strike():
                            replicate.cnts += 3
                        else:
                            replicate.cnts += int(3 / 2)
                    game.replicates = []
            else:
                player.cnts += int(3 / 2)
                if len(game.replicates) != 0:
                    for replicate in game.replicates:
                        if not replicate.check_strike():
                            replicate.cnts += int(3 / 2)
                        else:
                            replicate.cnts += int(3 / 4)
                    game.replicates = []
        else:
            if not player.check_immunity():
                player.cnts -= 2
    if choice == "B":
        if not player.check_immunity():
            player.cnts -= 1


def union_strike(game, player):
    choice = input("A or B?\n")
    if choice == "A":
        if not player.check_immunity():
            player.cnts -= 3
        for contestant in game.players:
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
                if contestant == player:
                    pass
                else:
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
            # NOTE: DO NOT ADD REPLICANT TO THIS AS IT'S NOT ACTUALLY GIVING CNTS
            # RATHER JUST GIVING BACK THE CNT TAKEN AWAY IN ABOVE FOR LOOP
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
            if not player.check_strike():
                player.cnts += 2
                if len(game.replicates) != 0:
                    for replicate in game.replicates:
                        if not replicate.check_strike():
                            replicate.cnts += 2
                        else:
                            replicate.cnts += int(2 / 2)
                    game.replicates = []
            else:
                player.cnts += int(2 / 2)
                if len(game.replicates) != 0:
                    for replicate in game.replicates:
                        if not replicate.check_strike():
                            replicate.cnts += int(2 / 2)
                        else:
                            replicate.cnts += int(2 / 4)
                    game.replicates = []
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
        if num >= 4:
            if not player.check_strike():
                player.cnts += 1
                if len(game.replicates) != 0:
                    for replicate in game.replicates:
                        if not replicate.check_strike():
                            replicate.cnts += 1
                        else:
                            replicate.cnts += int(1 / 2)
                    game.replicates = []
            else:
                player.cnts += int(1 / 2)
                if len(game.replicates) != 0:
                    for replicate in game.replicates:
                        if not replicate.check_strike():
                            replicate.cnts += int(1 / 2)
                        else:
                            replicate.cnts += int(1 / 4)
                    game.replicates = []
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
        if num >= 12:
            if not player.check_strike():
                player.cnts += 1
                if len(game.replicates) != 0:
                    for replicate in game.replicates:
                        if not replicate.check_strike():
                            replicate.cnts += 1
                        else:
                            replicate.cnts += int(1 / 2)
                    game.replicates = []
            else:
                player.cnts += int(1 / 2)
                if len(game.replicates) != 0:
                    for replicate in game.replicates:
                        if not replicate.check_strike():
                            replicate.cnts += int(1 / 2)
                        else:
                            replicate.cnts += int(1 / 4)
                    game.replicates = []
        else:
            pass
    else:
        if num >= 19:
            if not player.check_strike():
                player.cnts += 4
                if len(game.replicates) != 0:
                    for replicate in game.replicates:
                        if not replicate.check_strike():
                            replicate.cnts += 4
                        else:
                            replicate.cnts += int(4 / 2)
                    game.replicates = []
            else:
                player.cnts += int(4 / 2)
                if len(game.replicates) != 0:
                    for replicate in game.replicates:
                        if not replicate.check_strike():
                            replicate.cnts += int(4 / 2)
                        else:
                            replicate.cnts += int(4 / 4)
                    game.replicates = []
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
            if not player.check_strike():
                player.cnts += 3
                if len(game.replicates) != 0:
                    for replicate in game.replicates:
                        if not replicate.check_strike():
                            replicate.cnts += 3
                        else:
                            replicate.cnts += int(3 / 2)
                    game.replicates = []
            else:
                player.cnts += int(3 / 2)
                if len(game.replicates) != 0:
                    for replicate in game.replicates:
                        if not replicate.check_strike():
                            replicate.cnts += int(3 / 2)
                        else:
                            replicate.cnts += int(3 / 4)
                    game.replicates = []
        else:
            if not player.check_immunity():
                player.cnts -= 4
                player.skips += 2
    else:
        if not player.check_strike():
            player.cnts += 1
            if len(game.replicates) != 0:
                for replicate in game.replicates:
                    if not replicate.check_strike():
                        replicate.cnts += 1
                    else:
                        replicate.cnts += int(1 / 2)
                game.replicates = []
        else:
            player.cnts += int(1 / 2)
            if len(game.replicates) != 0:
                for replicate in game.replicates:
                    if not replicate.check_strike():
                        replicate.cnts += int(1 / 2)
                    else:
                        replicate.cnts += int(1 / 4)
                game.replicates = []


def structural_health_monitoring(game, player):
    choice = input("A or B?\n")
    num = randint(1, 20)
    if choice == "A":
        if num >= 10:
            if not player.check_strike():
                player.cnts += 2
                if len(game.replicates) != 0:
                    for replicate in game.replicates:
                        if not replicate.check_strike():
                            replicate.cnts += 2
                        else:
                            replicate.cnts += int(2 / 2)
                    game.replicates = []
            else:
                player.cnts += int(2 / 2)
                if len(game.replicates) != 0:
                    for replicate in game.replicates:
                        if not replicate.check_strike():
                            replicate.cnts += int(2 / 2)
                        else:
                            replicate.cnts += int(2 / 4)
                    game.replicates = []
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
                    if not replicate.check_strike():
                        replicate.cnts += 2
                    else:
                        replicate.cnts += int(2 / 2)
                game.replicates = []
            for contestant in game.players:
                if contestant != player:
                    if not contestant.check_strike():
                        contestant.cnts += 2
                    else:
                        contestant.cnts += int(2 / 2)


def student_recruitment(game, player):
    choice = input("A or B?\n")
    num = randint(1, 20)
    if choice == "A":
        if num >= 11:
            if not player.check_strike():
                player.cnts += 3
                if len(game.replicates) != 0:
                    for replicate in game.replicates:
                        if not replicate.check_strike():
                            replicate.cnts += 3
                        else:
                            replicate.cnts += int(3 / 2)
                    game.replicates = []
            else:
                player.cnts += int(3 / 2)
                if len(game.replicates) != 0:
                    for replicate in game.replicates:
                        if not replicate.check_strike():
                            replicate.cnts += int(3 / 2)
                        else:
                            replicate.cnts += int(3 / 4)
                    game.replicates = []
        else:
            if not player.check_immunity():
                player.cnts -= 2
    else:
        if num >= 5:
            if not player.check_strike():
                player.cnts += 2
                if len(game.replicates) != 0:
                    for replicate in game.replicates:
                        if not replicate.check_strike():
                            replicate.cnts += 2
                        else:
                            replicate.cnts += int(2 / 2)
                    game.replicates = []
            else:
                player.cnts += int(2 / 2)
                if len(game.replicates) != 0:
                    for replicate in game.replicates:
                        if not replicate.check_strike():
                            replicate.cnts += int(2 / 2)
                        else:
                            replicate.cnts += int(2 / 4)
                    game.replicates = []
        else:
            if not player.check_immunity():
                player.cnts -= 4


def recycling(player):
    if not player.check_immunity():
        player.cnts -= 1


def material_choices(player):
    if not player.check_immunity():
        player.cnts -= 1


def twitter(game, player):
    choice = input("A or B?\n")
    if choice == "A":
        num = randint(1, 20)
        if num >= 10:
            if not player.check_strike():
                player.cnts += 3
                if len(game.replicates) != 0:
                    for replicate in game.replicates:
                        if not replicate.check_strike():
                            replicate.cnts += 3
                        else:
                            replicate.cnts += int(3 / 2)
                    game.replicates = []
            else:
                player.cnts += int(3 / 2)
                if len(game.replicates) != 0:
                    for replicate in game.replicates:
                        if not replicate.check_strike():
                            replicate.cnts += int(3 / 2)
                        else:
                            replicate.cnts += int(3 / 4)
                    game.replicates = []
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
            if not player.check_strike():
                player.cnts += 3
                if len(game.replicates) != 0:
                    for replicate in game.replicates:
                        if not replicate.check_strike():
                            replicate.cnts += 3
                        else:
                            replicate.cnts += int(3 / 2)
                    game.replicates = []
            else:
                player.cnts += int(3 / 2)
                if len(game.replicates) != 0:
                    for replicate in game.replicates:
                        if not replicate.check_strike():
                            replicate.cnts += int(3 / 2)
                        else:
                            replicate.cnts += int(3 / 4)
                    game.replicates = []
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
            if not player.check_strike():
                player.cnts += 1
                if len(game.replicates) != 0:
                    for replicate in game.replicates:
                        if not replicate.check_strike():
                            replicate.cnts += 1
                        else:
                            replicate.cnts += int(1 / 2)
                    game.replicates = []
            else:
                player.cnts += int(1 / 2)
                if len(game.replicates) != 0:
                    for replicate in game.replicates:
                        if not replicate.check_strike():
                            replicate.cnts += int(1 / 2)
                        else:
                            replicate.cnts += int(1 / 4)
                    game.replicates = []
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
            if not player.check_strike():
                player.cnts += 3
                if len(game.replicates) != 0:
                    for replicate in game.replicates:
                        if not replicate.check_strike():
                            replicate.cnts += 3
                        else:
                            replicate.cnts += int(3 / 2)
                    game.replicates = []
            else:
                player.cnts += int(3 / 2)
                if len(game.replicates) != 0:
                    for replicate in game.replicates:
                        if not replicate.check_strike():
                            replicate.cnts += int(3 / 2)
                        else:
                            replicate.cnts += int(3 / 4)
                    game.replicates = []
        else:
            if not player.check_immunity():
                player.cnts -= 3
    else:
        if not player.check_strike():
            player.cnts += 1
            if len(game.replicates) != 0:
                for replicate in game.replicates:
                    if not replicate.check_strike():
                        replicate.cnts += 1
                    else:
                        replicate.cnts += int(1 / 2)
                game.replicates = []
        else:
            player.cnts += int(1 / 2)
            if len(game.replicates) != 0:
                for replicate in game.replicates:
                    if not replicate.check_strike():
                        replicate.cnts += int(1 / 2)
                    else:
                        replicate.cnts += int(1 / 4)
                game.replicates = []


def water_pollution(game, player):
    choice = input("A or B?\n")
    if choice == "A":
        num = randint(1, 20)
        if num >= 10:
            if not player.check_strike():
                player.cnts += 5
                if len(game.replicates) != 0:
                    for replicate in game.replicates:
                        if not replicate.check_strike():
                            replicate.cnts += 5
                        else:
                            replicate.cnts += int(5 / 2)
                    game.replicates = []
            else:
                player.cnts += int(5 / 2)
                if len(game.replicates) != 0:
                    for replicate in game.replicates:
                        if not replicate.check_strike():
                            replicate.cnts += int(5 / 2)
                        else:
                            replicate.cnts += int(5 / 4)
                    game.replicates = []
        else:
            if not player.check_immunity():
                player.cnts -= 5
    else:
        pass


def cleaning(game, player):
    choice = input("A or B?\n")
    num = randint(1, 20)
    if choice == "A":
        if num < 4:
            if not player.check_immunity():
                player.cnts -= 1
    else:
        if num >= 19:
            if not player.check_strike():
                player.cnts += 1
                if len(game.replicates) != 0:
                    for replicate in game.replicates:
                        if not replicate.check_strike():
                            replicate.cnts += 1
                        else:
                            replicate.cnts += int(1 / 2)
                    game.replicates = []
            else:
                player.cnts += int(1 / 2)
                if len(game.replicates) != 0:
                    for replicate in game.replicates:
                        if not replicate.check_strike():
                            replicate.cnts += int(1 / 2)
                        else:
                            replicate.cnts += int(1 / 4)
                    game.replicates = []
        else:
            if not player.check_immunity():
                player.cnts -= 3


def aerosols(game, player):
    choice = input("A or B?\n")
    if choice == "A":
        num = randint(1, 20)
        if num >= 4:
            if not player.check_strike():
                player.cnts += 1
                if len(game.replicates) != 0:
                    for replicate in game.replicates:
                        if not replicate.check_strike():
                            replicate.cnts += 1
                        else:
                            replicate.cnts += int(1 / 2)
                    game.replicates = []
            else:
                player.cnts += int(1 / 2)
                if len(game.replicates) != 0:
                    for replicate in game.replicates:
                        if not replicate.check_strike():
                            replicate.cnts += int(1 / 2)
                        else:
                            replicate.cnts += int(1 / 4)
                    game.replicates = []
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
            if not player.check_strike():
                player.cnts += 6
                if len(game.replicates) != 0:
                    for replicate in game.replicates:
                        if not replicate.check_strike():
                            replicate.cnts += 6
                        else:
                            replicate.cnts += int(6 / 2)
                    game.replicates = []
            else:
                player.cnts += int(6 / 2)
                if len(game.replicates) != 0:
                    for replicate in game.replicates:
                        if not replicate.check_strike():
                            replicate.cnts += int(6 / 2)
                        else:
                            replicate.cnts += int(6 / 4)
                    game.replicates = []
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
            if not player.check_strike():
                player.cnts += 2
                if len(game.replicates) != 0:
                    for replicate in game.replicates:
                        if not replicate.check_strike():
                            replicate.cnts += 2
                        else:
                            replicate.cnts += int(2 / 2)
                    game.replicates = []
            else:
                player.cnts += int(2 / 2)
                if len(game.replicates) != 0:
                    for replicate in game.replicates:
                        if not replicate.check_strike():
                            replicate.cnts += int(2 / 2)
                        else:
                            replicate.cnts += int(2 / 4)
                    game.replicates = []
        else:
            if not player.check_immunity():
                player.cnts -= 3
    else:
        if not player.check_strike():
            player.cnts += 1
            if len(game.replicates) != 0:
                for replicate in game.replicates:
                    if not replicate.check_strike():
                        replicate.cnts += 1
                    else:
                        replicate.cnts += int(1 / 2)
                game.replicates = []
        else:
            player.cnts += int(1 / 2)
            if len(game.replicates) != 0:
                for replicate in game.replicates:
                    if not replicate.check_strike():
                        replicate.cnts += int(1 / 2)
                    else:
                        replicate.cnts += int(1 / 4)
                game.replicates = []


def cnt_length(game, player):
    choice = input("A or B?\n")
    if choice == "A":
        if not player.check_strike():
            player.cnts += 2
            if len(game.replicates) != 0:
                for replicate in game.replicates:
                    if not replicate.check_strike():
                        replicate.cnts += 2
                    else:
                        replicate.cnts += int(2 / 2)
                game.replicates = []
        else:
            player.cnts += int(2 / 2)
            if len(game.replicates) != 0:
                for replicate in game.replicates:
                    if not replicate.check_strike():
                        replicate.cnts += int(2 / 2)
                    else:
                        replicate.cnts += int(2 / 4)
                game.replicates = []
        player.skips += 1
    else:
        if not player.check_immunity():
            player.cnts -= 1


def mycotoxins(game, player):
    choice = input("A or B?\n")
    if choice == "A":
        num = randint(1, 20)
        if num >= 14:
            if not player.check_strike():
                player.cnts += 3
                if len(game.replicates) != 0:
                    for replicate in game.replicates:
                        if not replicate.check_strike():
                            replicate.cnts += 3
                        else:
                            replicate.cnts += int(3 / 2)
                    game.replicates = []
            else:
                player.cnts += int(3 / 2)
                if len(game.replicates) != 0:
                    for replicate in game.replicates:
                        if not replicate.check_strike():
                            replicate.cnts += int(3 / 2)
                        else:
                            replicate.cnts += int(3 / 4)
                    game.replicates = []
        else:
            if not player.check_immunity():
                player.cnts -= 2
    else:
        if not player.check_strike():
            player.cnts += 1
            if len(game.replicates) != 0:
                for replicate in game.replicates:
                    if not replicate.check_strike():
                        replicate.cnts += 1
                    else:
                        replicate.cnts += int(1 / 2)
                game.replicates = []
        else:
            player.cnts += int(1 / 2)
            if len(game.replicates) != 0:
                for replicate in game.replicates:
                    if not replicate.check_strike():
                        replicate.cnts += int(1 / 2)
                    else:
                        replicate.cnts += int(1 / 4)
                game.replicates = []


def customization(game, player):
    choice = input("A or B?\n")
    if choice == "A":
        if not player.check_strike():
            player.cnts += 2
            if len(game.replicates) != 0:
                for replicate in game.replicates:
                    if not replicate.check_strike():
                        replicate.cnts += 2
                    else:
                        replicate.cnts += int(2 / 2)
                game.replicates = []
        else:
            player.cnts += int(2 / 2)
            if len(game.replicates) != 0:
                for replicate in game.replicates:
                    if not replicate.check_strike():
                        replicate.cnts += int(2 / 2)
                    else:
                        replicate.cnts += int(2 / 4)
                game.replicates = []
        player.skips += 1
    else:
        if not player.check_immunity():
            player.cnts -= 1


def gender_equality(game, player):
    choice = input("A or B?\n")
    if choice == "A":
        num = randint(1, 20)
        if num >= 10:
            if not player.check_strike():
                player.cnts += 2
                if len(game.replicates) != 0:
                    for replicate in game.replicates:
                        if not replicate.check_strike():
                            replicate.cnts += 2
                        else:
                            replicate.cnts += int(2 / 2)
                    game.replicates = []
            else:
                player.cnts += int(2 / 2)
                if len(game.replicates) != 0:
                    for replicate in game.replicates:
                        if not replicate.check_strike():
                            replicate.cnts += int(2 / 2)
                        else:
                            replicate.cnts += int(2 / 4)
                    game.replicates = []
        else:
            if not player.check_immunity():
                player.cnts -= 2
    if choice == "B":
        if not player.check_strike():
            player.cnts += 1
            if len(game.replicates) != 0:
                for replicate in game.replicates:
                    if not replicate.check_strike():
                        replicate.cnts += 1
                    else:
                        replicate.cnts += int(1 / 2)
                game.replicates = []
        else:
            player.cnts += int(1 / 2)
            if len(game.replicates) != 0:
                for replicate in game.replicates:
                    if not replicate.check_strike():
                        replicate.cnts += int(1 / 2)
                    else:
                        replicate.cnts += int(1 / 4)
                game.replicates = []


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
            if not player.check_strike():
                player.cnts += 1
                if len(game.replicates) != 0:
                    for replicate in game.replicates:
                        if not replicate.check_strike():
                            replicate.cnts += 1
                        else:
                            replicate.cnts += int(1 / 2)
                    game.replicates = []
            else:
                player.cnts += int(1 / 2)
                if len(game.replicates) != 0:
                    for replicate in game.replicates:
                        if not replicate.check_strike():
                            replicate.cnts += int(1 / 2)
                        else:
                            replicate.cnts += int(1 / 4)
                    game.replicates = []
        else:
            if not player.check_strike():
                player.cnts += 2
                if len(game.replicates) != 0:
                    for replicate in game.replicates:
                        if not replicate.check_strike():
                            replicate.cnts += 2
                        else:
                            replicate.cnts += int(2 / 2)
                    game.replicates = []
            else:
                player.cnts += int(2 / 2)
                if len(game.replicates) != 0:
                    for replicate in game.replicates:
                        if not replicate.check_strike():
                            replicate.cnts += int(2 / 2)
                        else:
                            replicate.cnts += int(2 / 4)
                    game.replicates = []


def fossil_fuels(game, player):
    if not player.check_strike():
        player.cnts += 1
        if len(game.replicates) != 0:
            for replicate in game.replicates:
                if not replicate.check_strike():
                    replicate.cnts += 1
                else:
                    replicate.cnts += int(1 / 2)
            game.replicates = []
    else:
        player.cnts += int(1 / 2)
        if len(game.replicates) != 0:
            for replicate in game.replicates:
                if not replicate.check_strike():
                    replicate.cnts += int(1 / 2)
                else:
                    replicate.cnts += int(1 / 4)
            game.replicates = []


def production_location(game, player):
    choice = input("A or B?\n")
    num = randint(1, 20)
    if choice == "A":
        if num >= 10:
            if not player.check_strike():
                player.cnts += 2
                if len(game.replicates) != 0:
                    for replicate in game.replicates:
                        if not replicate.check_strike():
                            replicate.cnts += 2
                        else:
                            replicate.cnts += int(2 / 2)
                    game.replicates = []
            else:
                player.cnts += int(2 / 2)
                if len(game.replicates) != 0:
                    for replicate in game.replicates:
                        if not replicate.check_strike():
                            replicate.cnts += int(2 / 2)
                        else:
                            replicate.cnts += int(2 / 4)
                    game.replicates = []
        else:
            if not player.check_immunity():
                player.cnts -= 2
    else:
        if num >= 10:
            if not player.check_strike():
                player.cnts += 3
                if len(game.replicates) != 0:
                    for replicate in game.replicates:
                        if not replicate.check_strike():
                            replicate.cnts += 3
                        else:
                            replicate.cnts += int(3 / 2)
                    game.replicates = []
            else:
                player.cnts += int(3 / 2)
                if len(game.replicates) != 0:
                    for replicate in game.replicates:
                        if not replicate.check_strike():
                            replicate.cnts += int(3 / 2)
                        else:
                            replicate.cnts += int(3 / 4)
                    game.replicates = []
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
            if not player.check_strike():
                player.cnts += 3
                if len(game.replicates) != 0:
                    for replicate in game.replicates:
                        if not replicate.check_strike():
                            replicate.cnts += 3
                        else:
                            replicate.cnts += int(3 / 2)
                    game.replicates = []
            else:
                player.cnts += int(3 / 2)
                if len(game.replicates) != 0:
                    for replicate in game.replicates:
                        if not replicate.check_strike():
                            replicate.cnts += int(3 / 2)
                        else:
                            replicate.cnts += int(3 / 4)
                    game.replicates = []
        else:
            if not player.check_immunity():
                player.cnts -= int(player.cnts / 3)
