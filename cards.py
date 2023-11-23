from random import randint


def sustainability_loop(game, player):
    pass


def diabetes(player):
    choice = input("A or B?\n")
    if choice == "A":
        num = randint(1, 20)
        if num >= 14:
            player.cnts += 3
        else:
            player.cnts -= 2
    if choice == "B":
        player.cnts -= 1
    if player.cnts < 0:
        player.cnts = 0


def union_strike(player):
    choice = input("A or B?\n")
    if choice == "A":
        num = randint(1, 20)
        if num >= 10:
            player.cnts += 2
        else:
            player.cnts -= 2
    if choice == "B":
        player.cnts += 1
    if player.cnts < 0:
        player.cnts = 0


def carcinogenicity(game, player):
    pass


def bond(game, player):
    pass


def ipr(game, player):
    pass


def regulations(game, player):
    pass


def sweat_analysis(game, player):
    pass


def critical_flaw(game, player):
    pass


def terrorism(game, player):
    pass


def structural_health_monitoring(game, player):
    pass


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
    pass


def fossil_fuels(game, player):
    pass


def production_location(game, player):
    pass


def budget(game, player):
    pass
