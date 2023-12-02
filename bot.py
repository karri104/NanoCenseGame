from cards import give_cnts
from random import randint


def find_best(game, player):
    # Check for current highest cnt count
    best = 0
    for contestant in game.players:
        if contestant.cnts > best and contestant != player:
            best = contestant.cnts
    return best


def diabetes(game, player):
    num = randint(1, 20)
    if num >= 14:
        give_cnts(game, player, 3)
    else:
        if not player.check_immunity():
            player.cnts -= 3


def union_strike(game, player):
    num = randint(1, 20)
    best = find_best(game, player)
    # Go for option A if player cnt is low or immune or other players have high cnts
    if player.cnts < 3 or best >= 9 or player.immune:
        if not player.check_immunity():
            player.cnts -= 3
        for contestant in game.players:
            if contestant != player:
                contestant.strike += 2
    # Go for safer option B else
    else:
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
    num = randint(1, 20)
    best = find_best(game, player)
    # Go for riskier option B if player has low cnts or immune and best has at least 2 cnts
    if (player.cnts <= 1 or player.immune) and best >= 2:
        if num >= 19:
            for contestant in game.players:
                if contestant != player:
                    contestant.cnts -= 2
        else:
            if not player.check_immunity():
                player.cnts -= 2
    # Go for safer option A else
    else:
        for contestant in game.players:
            contestant.cnts -= 1
        if player.check_immunity():
            # NOTE: DO NOT ADD REPLICANT OR STRIKE TO THIS AS IT'S NOT ACTUALLY GIVING
            # CNTS RATHER JUST GIVING BACK THE CNT TAKEN AWAY IN ABOVE FOR LOOP
            player.cnts += 1


def bond(game, player):
    num = randint(1, 20)
    best = find_best(game, player)
    # Go for riskier option A if own cnts are 1 or less or immune or if best has high cnts
    if (player.cnts <= 1 or player.immune or best >= 8) and best >= 2:
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
    # Option B else
    else:
        pass


def ipr(game, player):
    num = randint(1, 20)
    best = find_best(game, player)
    # Basically always take option A
    if best >= 2 or (best >= 1 and player.immune) or player.cnts <= 1:
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
    # Only take option B if everyone else has 0 cnts or 1 if player not immune
    else:
        if not player.check_immunity():
            player.cnts -= 1


def regulations(game, player):
    num = randint(1, 20)
    # Always do option A, option B seems like it would never be used.
    if num >= 14:
        give_cnts(game, player, 2)
    else:
        if not player.check_immunity():
            player.cnts -= 2


def sweat_analysis(game, player):
    num = randint(1, 20)
    best = find_best(game, player)
    # Do the riskier option B if player has low or high cnts or others have high cnts or player is immune
    if player.cnts < 4 or best >= 8 or player.cnts >= 9 or player.immune:
        if num >= 15:
            give_cnts(game, player, 4)
        else:
            if not player.check_immunity():
                player.cnts -= 3
    else:
        if num >= 8:
            give_cnts(game, player, 1)
        else:
            pass


def critical_flaw(player):
    num = randint(1, 2)
    if num == 1:
        player.immune = True
    else:
        player.replicate = True


def terrorism(game, player):
    num = randint(1, 20)
    # Always take option A
    if num >= 4:
        give_cnts(game, player, 3)
    else:
        if not player.check_immunity():
            player.cnts -= 4
            player.skips += 2


def structural_health_monitoring(game, player):
    num = randint(1, 20)
    best = find_best(game, player)
    # Go for option A if others aren't close to winning or you would win with a success
    if player.cnts >= 10 or best <= 8:
        if num >= 10:
            give_cnts(game, player, 2)
        else:
            if not player.check_immunity():
                player.cnts -= 2
    # Go for option B if others are close to winning
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
    pass


def recycling(game, player):
    pass


def material_choices(game, player):
    pass


def twitter(game, player):
    pass


def greenwashing(game, player):
    pass


def temperature(game, player):
    pass


def increased_production(game, player):
    pass


def water_pollution(game, player):
    pass


def cleaning(game, player):
    pass


def aerosols(game, player):
    pass


def enzymes(game, player):
    pass


def cnt_spray(game, player):
    pass


def cnt_length(game, player):
    pass


def mycotoxins(game, player):
    pass


def customization(game, player):
    pass


def gender_equality(game, player):
    pass


def bulletproof_vests(game, player):
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
    num = randint(1, 20)
    best = find_best(game, player)
    # Do the riskier option B if player has low or high cnts or others have high cnts or player is immune
    if player.cnts < 4 or best >= 8 or player.cnts >= 9 or player.immune:
        if num >= 10:
            give_cnts(game, player, 3)
        else:
            if not player.check_immunity():
                player.cnts -= 4
    # Do the less risky option A if we are in the "midgame"
    else:
        if num >= 10:
            give_cnts(game, player, 2)
        else:
            if not player.check_immunity():
                player.cnts -= 2


def budget(game, player):
    num = randint(1, 20)
    best = find_best(game, player)
    # Does riskier option B if player is immune, has low cnts or someone else has high cnts
    if player.cnts < 4 or best >= 8 or player.immune:
        if num >= 17:
            give_cnts(game, player, 3)
        else:
            if not player.check_immunity():
                player.cnts -= int(player.cnts / 3)
    # Does safer option A if in "midgame"
    else:
        if len(game.replicates) != 0:
            for replicate in game.replicates:
                replicate.cnts += 1
            game.replicates = []
        for contestant in game.players:
            if not contestant.check_strike():
                contestant.cnts += 1
            else:
                contestant.cnts += int(1 / 2)
